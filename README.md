# scrapy-innertext

Repository to show how to get the innertext of elements.

The code for getting the innertext is in [crawler/innertext.py](./crawler/innertext.py)

## Usage

### The simple *innertext_quick*

The `innertext_quick` method is used by passing a selector to it:

```python
innertext_quick(response.css('#my-element'))
```

It will take any elements inside this element and join their texts. Examples:

```html
<div id="my-element">the <span>jabberwocky</span> is not <b>hungry</b></div>
```

Would generate `the jabberwocky is not hungry`

```html
<table id="my-element">
    <tr>
        <th>Col A</th>
        <th>Col B</th>
    </tr>
    <tr>
        <td>Val A</td>
        <td>Val B</td>
    </tr>
</table>
```

Would generate `Col ACol BVal AVal B`. To add spacing, you can set the delimiter `innertext_quick(response.css('#my-element'), " ")` which would give `Col A Col B Val A Val B`.

Since a selector is returned, you can also pull ot the value of all elements. For example:

```python
innertext_quick(response.css('#my-element td, #my-element th'))
```

Would with the table above generate a list `["Col A", "Col B", "Val A", "Val B"]`. This works even if the the `td` and `th` contains other elements such as span tags.


### Real rendering with *innertext*

The simple innertext method will only select all the elements and join their respective inner text. This creates problems where a structure may have linebreaks or other special structures and tags.

Instead, we can use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to get the html of the element and parse the text. This gives a more realistic rendering of the text and we can control what elements to ignore if we want, for example, to avoid outputting table values.

See the [innertext](./crawler/innertext.py) method.

For example:

```html
<div id="complex-text">
    <p>This div contains <i>complex</i> text</p>
    <ul>
        <li>List item 1</li>
        <li>List item 2</li>
    </ul>
    <blockquote>Including quotes</blockquote>
</div>
```

Will be rendered as `This div contains complex text\n\nList item 1\nList item 2\n\nIncluding quotes` correctly ignoring elements for styling (`<i>`, `<b>`, `<span>`) and creating line breaks between structural elements (`<blockquite>`, `li`).

## Testing

Run `pipenv run python test.py` which will create a tiny server hosting the `test.html` and then call `scrapy crawl test` to run the crawler on this file.

It will also finish by outputting the example texts parsed.