using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using xNet.Net;

namespace SEOShow
{
    abstract public class IParser
    {        
        protected string _name;    //Имя парсера
        public string Name
        {
            get {return _name;}
            set {_name = value;}
        }

        protected string _site;    //Имя искомого сайта
        public string Site
        {
            get { return _site; }
            set { _site = value; }
        }

        int _region = 63;        //Регион для поиска  по умолчанию =0
        public int region
        {
            get { return _region; }
            set { _region = value; }
        }
        
        string _urlPoisk;
        public string urlPoisk
        {
            get { return _urlPoisk; }
            set { _urlPoisk = value; }
        }

        string _urlCheckCaptcha;
        public string urlCheckCaptcha
        {
            get { return _urlCheckCaptcha; }
            set { _urlCheckCaptcha = value; }
        }

        bool _needCatcha = false;
        public bool NeedCaptcha
        {
            get { return _needCatcha; }
            set { _needCatcha = value; }
        }


        int _countOnPage = 50;       //Количество записей на странице поисковика
        public int CountOnPage
        {
            get { return _countOnPage; }
            set { _countOnPage = value; }
        }

        abstract public void LoadPage(string zapros);     //Загрузка страницы поисковика

        abstract public bool CheckCaptcha();            //Проверяем на наличие капчи на странице

        abstract public MemoryStream GetCaptchaImage();

        abstract public void SendCaptha(string captchaText);

        //abstract public void LoadPage(int page = 0);
    }
}
