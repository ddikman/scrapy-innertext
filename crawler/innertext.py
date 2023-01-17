from bs4 import BeautifulSoup

def innertext_quick(elements, delimiter=""):
    return list(delimiter.join(element.css('*::text').getall()) for element in elements)

def innertext(selector):
    html = selector.get()
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text().strip()