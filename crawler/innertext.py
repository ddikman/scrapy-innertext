def innertext(elements, delimiter=""):
    return list(delimiter.join(element.css('*::text').getall()) for element in elements)