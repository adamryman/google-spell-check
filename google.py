#!/home/adamryman/bin/venv3/bin/python3

import argparse
import sys
import requests
from bs4 import BeautifulSoup

def main():
    search_request = parse_search_request()

    page = get_page(search_request)

    spell_tag = get_spell_tag(page)

    if spell_tag == None or spell_tag.text == "":
        print(search_request)
    else:
        print(spell_tag.text)

def get_spell_tag(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    spell_tag = soup.find('a', {'class' : 'spell'})

    return spell_tag

# Get google html page that has correct spelling
def get_page(search):
    headers = {
        "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0",
    }
    url = 'http://google.com/search?h1=en&q=' + search + "&meta=&gws_rd=ssl"
    r = requests.get(url, headers=headers)
    return r

# Parse arguments to get search request
def parse_search_request():
    return ' '.join(sys.argv[1:])

if __name__ == '__main__':
    main()
