using HtmlAgilityPack;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using xNet.Net;

namespace SEOShow
{
    public partial class Form1 : Form
    {
        CookieDictionary cookie = new CookieDictionary();
        HttpRequest request = new HttpRequest();

        public Form1()
        {
            InitializeComponent();
            request.Cookies = cookie;
            request.Cookies.Add("clid", "9582");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            rtbYandex.Clear();
            int page = 0;
            string zapros = @"http://yandex.ru/yandsearch?text=" + HttpHelper.UrlEncode(tbZapros.Text) + "&p=" + page + "&rnd=28111&numdoc=50&lr=0";
            string content = "";
            string key_captcha = "";
            string return_path_captcha = "";
            string url_captcha = "";


            

            
            
            request.UserAgent = HttpHelper.IEUserAgent();

            // Отправляем запрос.
            request.Referer = HttpHelper.UrlEncode(zapros);
            HttpResponse response = request.Get(zapros);
            // Принимаем тело сообщения в виде строки.
            content = response.ToString();

            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            HtmlNodeCollection nodes;
            doc.LoadHtml(content);

            //Парсим страницу на наличие капчи
            nodes = doc.DocumentNode.SelectNodes("//div[@class='b-captcha']");
            //И если капча есть переходим к её обработке
            if (nodes != null)
            {
                HtmlNodeCollection inputs = nodes[0].SelectNodes("//input");
                key_captcha = inputs[0].GetAttributeValue("value", "false").Replace("&amp", "");
                return_path_captcha = inputs[1].GetAttributeValue("value", "false").Replace("&amp;", "&"); ;

                //Парсим страницу на получение тэга <img>, в котором прописана капча
                HtmlNode image = doc.DocumentNode.SelectSingleNode("//td[@class='b-captcha__layout__l']//img");
                //Получаем URL капчи (путь по которому её можно скачать)
                url_captcha = image.GetAttributeValue("src", "true");

                //Скачиваем картинку с удаленного адреса в MemoryStream
                MemoryStream stream = request.Get(url_captcha).ToMemoryStream();
                //Создаем форму ввода капчи
                FormCaptcha formCaptcha = new FormCaptcha();
                //Отображаем в PictureBox картинку с MemoryStream
                formCaptcha.pictureBox1.Image = Image.FromStream(stream);
                //Отображаем форму ввода капчи для пользователя
                formCaptcha.ShowDialog();

                request.AddUrlParam("key", HttpHelper.UrlEncode(key_captcha));
                request.AddUrlParam("retpath", HttpHelper.UrlEncode(return_path_captcha));
                request.AddUrlParam("rep", HttpHelper.UrlEncode(formCaptcha.tbPassword.Text));

                //request.AddHeader("Host","yandex.ru");
                response = request.Get(@"http://yandex.ru/checkcaptcha");
                doc.LoadHtml(response.ToString());

            }



            //Парсим страницу на блоки со ссылками
            nodes = doc.DocumentNode.SelectNodes("//div[@class='serp-list']//span[@class='serp-url__item']//a[1]");
            int count = 0;
            int pos = 0;
            if (nodes == null)
                return;
            foreach (HtmlNode node in nodes)
            {
                count++;
                rtbYandex.AppendText(count + ". " + node.InnerText + "\n");
                if ("http://".ToUpper() + node.InnerText.ToUpper() == tbSite.Text.ToUpper())
                {
                    rtbYandex.Select(pos, node.InnerText.Length + 3);
                    rtbYandex.SelectionColor = Color.Red;
                }
                pos += node.InnerText.Length + 1 + (Convert.ToString(count) + ". ").Length;
            }


        }

        private void button2_Click(object sender, EventArgs e)
        {
            YandexParser parser = new YandexParser("Yandex");

            parser.LoadPage(tbZapros.Text);

            parser.CheckCaptcha();

            while (parser.NeedCaptcha)
            {
                FormCaptcha formCaptcha = new FormCaptcha();
                formCaptcha.pictureBox1.Image = Image.FromStream(parser.GetCaptchaImage());
                formCaptcha.ShowDialog();
                if (formCaptcha.tbPassword.Text != "")
                {
                    parser.SendCaptha(formCaptcha.tbPassword.Text);
                    parser.CheckCaptcha();
                }
            }
            List<string> sites = new List<string>();
            sites = parser.ParseSitesURL();
            int pos = 0;
            if (sites != null)
            {
                for (int x = 0; x <= sites.Count - 1; x++)
                {
                    rtbYandex.AppendText(x+1 + ". " + sites[x] + "\n");
                    if ("http://".ToUpper() + sites[x].ToUpper() == tbSite.Text.ToUpper())
                    {
                        rtbYandex.Select(pos, sites[x].Length + 3);
                        rtbYandex.SelectionColor = Color.Red;
                    }
                    pos += sites[x].Length + 1 + (Convert.ToString(x) + ". ").Length;
                }

            }


        }
    }
}
