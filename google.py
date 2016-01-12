#!/home/adamryman/bin/venv3/bin/python3
"""Takes a phrase as input and Googles it.
If Google thinks the phrase should be different, print Google's phrase to standard out,
otherwise print the input phrase to standard out"""

import sys
import requests
from bs4 import BeautifulSoup

def main():
    """Main logic that prints to standard out"""
    search_request = parse_search_request()

    page = get_page(search_request)

    spell_tag = get_spell_tag(page)

    # If the spell tag does not exist or if the text is empty then the input is
    # spelled correctly as far as Google is concerned, output it
    # otherwise output the Google spelling
    if spell_tag is None or spell_tag.text == "":
        print(search_request)
    else:
        print(spell_tag.text)

def get_spell_tag(page):
    """Get out the tag that has the Google spelling or is empty"""
    soup = BeautifulSoup(page.text, 'html.parser')
    spell_tag = soup.find('a', {'class' : 'spell'})

    return spell_tag

def get_page(search):
    """Get Google html page that has Google spelling and/or same spelling"""
    headers = {
        "User-Agent" :
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0",
    }
    url = 'http://google.com/search?h1=en&q=' + search + "&meta=&gws_rd=ssl"
    page = requests.get(url, headers=headers)
    return page

def parse_search_request():
    """Parse arguments to get search request for Google spell checking"""
    return ' '.join(sys.argv[1:])

if __name__ == '__main__':
    main()
