
# Phishing_Links

##

![alt text](https://github.com/oz105/phishing_links/blob/main/img/img.png)

## src

In this folder there is the file Phishing.py which contains the code 
that performs the tests according to the list of brands we received.

Returns True - if the url is indeed Phishing.

Returns False - if the url is not Phishing and its domain is in the list of brands.

Returns None - if we can't tell.

## test

### test_url_ok
      
      In this test case we check URLs that should not be phishing because they are listed.

### test_typo

      In this test case we check URLs that are supposed to be phishing due to a typo

### test_subdomain
      
      In this test case, we check URLs that are supposed to be phishing due to domain impersonation using the subdomain.

### test_mixed
      
      In this test case, we check URLs that are supposed to be phishing with a combination of typo and posing domain using the subdomain.
      
### test_unique

      In this test case, we test URLs that we can't tell if they are phishing or not - should return None.
      
