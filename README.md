# pelican-tufte

A Pelican theme using Tufte CSS. Build with academics in mind.

## Demo 

You can see a live demo [here](https://janiceto.github.io/pelican-tufte/).

![Demo](screenshot.png)


## Usage

This theme supposes that every article has a category and only those with category `Blog` are considered blog posts. 

Articles with other categories are considered items and are listed in that category page.


### Settings

Pelican settings supported by this theme:

- `SITESUBTITLE`
- `MENUITEMS`
- `DISPLAY_PAGES_ON_MENU`
- `DISPLAY_CATEGORIES_ON_MENU`
- `INDEX_SAVE_AS`

Additionaly supported settings variables:

- `PROFILE_IMAGE_URL` - image to display in the `index.html` page


### Use a static page as home page

Use the save_as variable in the page you wish to use as home page. For instance, in the `content/pages/home.md`:

```
Title: Welcome to My Site
URL:
save_as: index.html

Thank you for visiting. Welcome!
```

If the original blog index is still wanted, it can then be saved in a different location by setting `INDEX_SAVE_AS = 'blog.html'`.


### Reorder the menu items

In the settings file make `DISPLAY_PAGES_ON_MENU` and `DISPLAY_CATEGORIES_ON_MENU` `False` and create the `MENUITEMS` variable as follows:

```python
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
    ('Bio', '/'),
    ('Publications', '/category/publications.html'),
    ('Teaching', '/category/teaching.html'),
    ('Talks', '/category/talks.html'),
    ('Projects', '/category/projects.html'),
    ('Blog', '/blog.html'),
    ('Contact', '/pages/contact.html'),
)
```

### Using margin notes in articles

You can create margin notes in the style of [Tufte CSS](https://edwardtufte.github.io/tufte-css/) by adding the following HTML in the contents of any article.

```html
<span class="marginnote">
    Margin note  text here.
</span>
```

## Contributing

Contributions are welcome.


## Acknowledgements

This theme is based on the [Tufte CSS](https://edwardtufte.github.io/tufte-css/) created by Dave Liepmann.


## License

Released under the [MIT license](LICENSE)
