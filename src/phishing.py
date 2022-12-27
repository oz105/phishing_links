import re
import difflib
import tldextract



""" returns dictionary contains domain, subdomain, suffix of the url """

def get_metadata_from_url(url):
    url_data = tldextract.extract(url)
    metadata = {'domain': url_data.domain, 'subdomain': url_data.subdomain, 'suffix': url_data.suffix}

    return metadata


""" This function goes through the brands dictionary we received,
adds relevant information to each brand according to its url
domain, subdomain, suffix  """

def get_metadata(brands):

    brands_metadata = {}
    for name, url in brands.items():
        url_data = get_metadata_from_url(url)
        metadata = {'url': url}
        metadata.update(url_data)
        brands_metadata[name] = metadata

    return brands_metadata


""" Check if the domain of the url is in list 
  if it is we will return False because if we found the domain
  in the list its means this is not phishing
  """

def verify_domain(brands_metadata, url):
    url_data = get_metadata_from_url(url)
    target_domain = url_data['domain']
    target_suffix = url_data['suffix']

    for name, metadata in brands_metadata.items():
        if metadata['domain'] == target_domain and metadata['suffix'] == target_suffix:
            return target_domain

    return False


""" Check if there is typosquatting and to what domain it pretend to be """

def verify_typosquatting(brands_metadata, url):
    url_data = get_metadata_from_url(url)
    target_domain = url_data['domain']
    domains_list = []
    for metadata in brands_metadata.values():
        temp_domain = metadata['domain']
        domains_list.append(temp_domain)

    # If we want to be more precise, we can increase the "cutoff" variable,
    # but that way there is a chance that we will miss an impersonation of a certain domain.

    possible_to_pretend = difflib.get_close_matches(target_domain, domains_list, n=1, cutoff=0.7)

    if len(possible_to_pretend) > 0:
        return possible_to_pretend

    # this for url that have subdomain with typosquatting like 'https://www.wella.co.il.photo.com/signin'

    elif url_data['subdomain'] != 'www' and url_data['subdomain'] != '':
        possible_option = verify_typosquatting(brands_metadata, url_data['subdomain'])
        if possible_option:
            return possible_option

    else:
        return False

""" Check if the subdomain appears in the list and determine what domain it pretend to be"""

def verify_subdomain(brands_metadata, url):
    url_data = get_metadata_from_url(url)
    target_subdomain = url_data['subdomain']

    for name, metadata in brands_metadata.items():
        temp_domain = metadata['domain']
        if temp_domain in target_subdomain:
            return temp_domain

    return False


""" This function get dictionary of brands and url and will return 
    True - if its phishing
    False - if its not
    None - if cant tell 
    based on the dictionary of brands
    """
def is_phishing(brands, url):
    brands_metadata = get_metadata(brands)

    domain_check = verify_domain(brands_metadata, url)
    if domain_check:
        print("Its OK. The domain is on the list")
        print("The domain is " + str(domain_check))
        return False

    typosquatting_check = verify_typosquatting(brands_metadata, url)
    if typosquatting_check:
        print("CAREFUL! The Url: " + str(url) + " is Phishing!")
        for possible in typosquatting_check:
            print("Try to pretend to be " + str(possible) + " domain")
        return True

    subdomain_check = verify_subdomain(brands_metadata, url)
    if subdomain_check:
        print("CAREFUL! The Url: " + str(url) + " is Phishing!")
        print("Try to pretend to be " + str(subdomain_check) + " domain")
        return True

    print("Cannot determine about this url: " + str(url))


if __name__ == '__main__':
    # for example
    brands = {"Google": "www.google.com",
              "Netflix": "www.netflix.com",
              "Paypal": "www.paypal.com",
              "Walla": "www.walla.co.il",
              "Amazon": "www.amazon.com",
              "Yahoo": "www.yahoo.com",
              "Microsoft": "www.microsoft.com",
              "Ebay": "www.ebay.com",
              "Wikipedia": "www.wikipedia.org"
              }
    url = "www.netflx.com"
    print(is_phishing(brands,url))


