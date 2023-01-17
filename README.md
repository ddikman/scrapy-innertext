# scrapy-innertext

Repository to show how to get the innertext of elements.

The code for getting the innertext is in [crawler/innertext.py](./crawler/innertext.py)

## Testing

Run `pipenv run python test.py` which will create a tiny server hosting the `test.html` and then call `scrapy crawl test` to run the crawler on this file.
