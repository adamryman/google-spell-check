#!/home/adamryman/bin/venv3/bin/python3

import argparse
import sys
import requests
from bs4 import BeautifulSoup

def get_spell_tag(page):
    return

def get_page(search):

    # Gather contents of the page
    url = 'http://google.com/search?q=' + search
    print(url)
    r = requests.get(url)
    return r

def parse_search_request():
    return ' '.join(sys.argv[1:])

if __name__ == '__main__':
    search_request = parse_search_request()
    print(search_request)

    r = get_page(search_request)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.find_all('a', {'class' : 'spell'}))


