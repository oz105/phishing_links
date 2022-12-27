import unittest

from src.phishing import is_phishing



class MyTestCase(unittest.TestCase):

    brands = {"Google": "http://www.google.com",
              "Netflix": "http://www.netflix.com",
              "Paypal": "http://www.paypal.com",
              "Walla": "http://www.walla.co.il",
              "Amazon": "http://www.amazon.com",
              "Yahoo": "http://www.yahoo.com",
              "Microsoft": "http://www.microsoft.com",
              "Ebay": "http://www.ebay.com",
              "Wikipedia": "http://www.wikipedia.org",
              "Alibaba": "http://www.alibaba.com",
              "Gmail": "http://www.gmail.com",
              "Ynet": "https://www.ynet.co.il",
              "Sport5": "https://www.sport5.co.il",
              "Looklike": "https://looklike.co.il",
              "Galita-fashion": "https://galita-fashion.co.il",
              "Stepin": 'https://www.stepin.co.il',
              "Github": 'https://www.github.com'
              }

    """ Checking urls that appear in the list and should not be phishing. """
    def test_url_ok(self):
        self.assertEqual(False, is_phishing(self.brands, 'https://www.ebay.com/itm/353932565748?var=623308078135'))
        self.assertEqual(False, is_phishing(self.brands, 'https://playbyplay.sport5.co.il/?GameID=125439&FLNum=16'))
        self.assertEqual(False, is_phishing(self.brands, 'https://www.ynet.co.il/news/article/r1dwk00dfo#autoplay'))
        self.assertEqual(False, is_phishing(self.brands, 'https://es.wikipedia.org/wiki/Wikipedia:Portada'))
        self.assertEqual(False, is_phishing(self.brands, 'https://www.paypal.com/bizsignup'))
        self.assertEqual(False, is_phishing(self.brands, 'https://news.walla.co.il/item/3548182'))
        self.assertEqual(False, is_phishing(self.brands, 'https://looklike.co.il/product/mika-skirt'))
        self.assertEqual(False, is_phishing(self.brands, 'https://looklike.co.il/product-category/new-arrivel-%d7%a9%d7%9e%d7%9c%d7%95%d7%aa-%d7%98%d7%95%d7%a4%d7%99%d7%9d-%d7%94%d7%95%d7%a8%d7%a1%d7%99%d7%9d-%d7%95%d7%a2%d7%95%d7%93/'))
        self.assertEqual(False, is_phishing(self.brands, 'https://galita-fashion.co.il/collections/evening-sale-up-to-80'))
        self.assertEqual(False, is_phishing(self.brands, 'https://www.stepin.co.il/%D7%99%D7%9C%D7%93%D7%99%D7%9D/%D7%91%D7%A0%D7%99%D7%9D/%D7%9E%D7%92%D7%A4%D7%95%D7%A0%D7%99%D7%9D'))
        self.assertEqual(False, is_phishing(self.brands, 'https://www.stepin.co.il/catalog/product/view/id/23814/s/m8560365249/category/5646/'))



    def test_typo(self):

        self.assertEqual(True, is_phishing(self.brands, 'https://netfix.com'))
        self.assertEqual(True, is_phishing(self.brands, 'https://netflixx.com'))
        self.assertEqual(True, is_phishing(self.brands, 'https://googlee.com'))
        self.assertEqual(True, is_phishing(self.brands, 'https://amazonn.net'))
        self.assertEqual(True, is_phishing(self.brands, 'https://amazonn.com'))
        self.assertEqual(True, is_phishing(self.brands, 'http://www.yaho.com'))
        self.assertEqual(True, is_phishing(self.brands, 'https://aamazon.com'))
        self.assertEqual(True, is_phishing(self.brands, 'http://www.wala.co.il'))
        self.assertEqual(True, is_phishing(self.brands, 'http://www.waalla.co.il'))
        self.assertEqual(True, is_phishing(self.brands, 'http://www.wallaa.co.il'))
        self.assertEqual(True, is_phishing(self.brands, 'https://www.gitlub.com'))
        self.assertEqual(True, is_phishing(self.brands, 'https://neetflix.com'))




    def test_subdomain(self):
        self.assertEqual(True, is_phishing(self.brands, 'https://www.amazon.com.secure.getinon-mail.com/Technology-Ventures-Enterprise-Thomas-Byers/dp/0073523429'))
        self.assertEqual(True, is_phishing(self.brands, 'https://www.paypal.com.seurit.alret.confi-man-secure.com/signin'))
        self.assertEqual(True, is_phishing(self.brands, 'https://www.walla.co.il.photo.com/signin'))
        self.assertEqual(True, is_phishing(self.brands, 'https://www.google.com.photo.images.search.com/signin'))
        self.assertEqual(True, is_phishing(self.brands, 'https://google.com.photo.images.search.com/signin'))
        self.assertEqual(True, is_phishing(self.brands, 'https://www.microsoft.com.office365.ru'))
        self.assertEqual(True, is_phishing(self.brands, 'https://microsoft.com.office365.ru'))

    def test_mixed(self):
        self.assertEqual(True, is_phishing(self.brands, 'https://www.wella.co.il.photo.com/signin'))
        self.assertEqual(True, is_phishing(self.brands, 'https://www.netfix.com.photo.com/signin'))
        self.assertEqual(True, is_phishing(self.brands, 'https://www.amaazon.com.s.com/signin'))

    def test_unique(self):
        self.assertEqual(None, is_phishing(self.brands, 'https://www.nothing.co.il.photo.com/signin'))
        self.assertEqual(None, is_phishing(self.brands, 'https://www.cantbe.co.il.photo.com/signin'))
        self.assertEqual(None, is_phishing(self.brands, 'https://www.noidea.co.il'))
        self.assertEqual(None, is_phishing(self.brands, 'https://www.cantknow.co.il'))
        self.assertEqual(None, is_phishing(self.brands, 'https://www.cant.know.co.il'))


if __name__ == '__main__':
    unittest.main()