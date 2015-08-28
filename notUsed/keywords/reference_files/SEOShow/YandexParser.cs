using HtmlAgilityPack;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using xNet.Net;

namespace SEOShow
{
    public class YandexParser: IParser
    {

        CookieDictionary cookie;
        HttpRequest request;
        HttpResponse response;
        HtmlAgilityPack.HtmlDocument doc;
        
        string content;             //содержимое страницы
        
        string key_captcha = "";
        string return_path_captcha = "";
        string url_captcha = "";
        string xPathCaptcha = "//div[@class='b-captcha']";
        string xPathImageCaptcha = "//td[@class='b-captcha__layout__l']//img";
        string xPathSiteURL = "//div[@class='serp-list']//span[@class='serp-url__item']//a[1]";

        public YandexParser(string name)
        { 
            Name = name;
            
            CookieDictionary cookie = new CookieDictionary();
            request  = new HttpRequest();
            request.Cookies = cookie;
            urlPoisk = @"http://yandex.ru/yandsearch?text=";
            urlCheckCaptcha = @"http://yandex.ru/checkcaptcha";

            request.UserAgent = HttpHelper.OperaUserAgent();
        }

        public override void LoadPage(string zapros)
        {
            string url = urlPoisk + HttpHelper.UrlEncode(zapros) + "&p=" + 0 + "&numdoc=" + CountOnPage+"&lr="+region;
            HttpResponse response = request.Get(urlPoisk + zapros + "&p=" + 0 + "&rnd=28111&numdoc=" + CountOnPage + "&lr=" + region);
            // Принимаем тело сообщения в виде строки.
            content = response.ToString();

            CheckCaptcha();
        }

        public override MemoryStream GetCaptchaImage()
        {
            doc = new HtmlAgilityPack.HtmlDocument();
            HtmlNodeCollection nodes;
            doc.LoadHtml(content);
            nodes = doc.DocumentNode.SelectNodes(xPathCaptcha);

            HtmlNodeCollection inputs = nodes[0].SelectNodes("//input");
            key_captcha = inputs[0].GetAttributeValue("value", "false").Replace("&amp", "");
            return_path_captcha = inputs[1].GetAttributeValue("value", "false").Replace("&amp;", "&"); ;

            //Парсим страницу на получение тэга <img>, в котором прописана капча
            HtmlNode image = doc.DocumentNode.SelectSingleNode(xPathImageCaptcha);
            //Получаем URL капчи (путь по которому её можно скачать)
            url_captcha = image.GetAttributeValue("src", "true");

            //Скачиваем картинку с удаленного адреса в MemoryStream
            MemoryStream stream = request.Get(url_captcha).ToMemoryStream();
            return stream;
        }


        public override void SendCaptha(string captchaText)
        {
            request.AddUrlParam("key", HttpHelper.UrlEncode(key_captcha));
            request.AddUrlParam("retpath", HttpHelper.UrlEncode(return_path_captcha));
            request.AddUrlParam("rep", HttpHelper.UrlEncode(captchaText));
            response = request.Get(urlCheckCaptcha);
            content = response.ToString();
        }


        public override bool CheckCaptcha()
        {
            doc = new HtmlAgilityPack.HtmlDocument();
            HtmlNodeCollection nodes;
            doc.LoadHtml(content);

            //Парсим страницу на наличие капчи
            nodes = doc.DocumentNode.SelectNodes(xPathCaptcha);
            if (nodes != null)
            {

                NeedCaptcha = true;
            }
            else
            {
                NeedCaptcha = false;               
            }
            return NeedCaptcha;
        }

        public List<string> ParseSitesURL()
        {
            HtmlNodeCollection nodes = doc.DocumentNode.SelectNodes(xPathSiteURL);
            int count = 0;
            int pos = 0;
            if (nodes == null)
                return null;
            List<string> sites = new List<string>();
            foreach (HtmlNode node in nodes)
            {
                count++;
                sites.Add(node.InnerText);
            }

            return sites;
        }

    }
}
