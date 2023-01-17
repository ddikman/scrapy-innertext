# scrapy-innertext

Repository to show how to get the innertext of elements.

The code for getting the innertext is in [crawler/innertext.py](./crawler/innertext.py)

## Usage

The `innertext` method is used by passing a selector to it:

```python
innertext(response.css('#my-element'))
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

Would generate `Col ACol BVal AVal B`. To add spacing, you can set the delimiter `innertext(response.css('#my-element'), " ")` which would give `Col A Col B Val A Val B`.

Since a selector is returned, you can also pull ot the value of all elements. For example:

```python
innertext(response.css('#my-element td, #my-element th'))
```

Would with the table above generate a list `["Col A", "Col B", "Val A", "Val B"]`. This works even if the the `td` and `th` contains other elements such as span tags.



## Testing

Run `pipenv run python test.py` which will create a tiny server hosting the `test.html` and then call `scrapy crawl test` to run the crawler on this file.
