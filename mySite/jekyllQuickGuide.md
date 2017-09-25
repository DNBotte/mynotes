# The Fastest Way to Launch a Static Website on GitHub Pages Using Jekyll

### Prerequisites:

* Domain Registered
* GitHub Account

## I. Setting Up the Site's Repository

**1.** Create a New Repository named: "username.github.io"
**2.** Enter url on settings page
**3.** Create CNAME file (depends on hosting site's instructions)

## II. Add Jekyll Files

## III. Cutsomize

**1.** Rename index.html (this is just a template based on the default layout)  
**Note:** If homepage is unique/has no includes, upload as is.  
Same for other unique pages.  
**2.** Upload includes as .html into the _includes directory  
**3.** Upload layout and name it as layoutName.html into the layout directory  
### Example Layout:
```html
<!DOCTYPE html>
<html>

  {% include head.html %}
  
  <body>
  
    {% include nav.html %}
	
	{% include leftSideBar.html %}
	
	  {{ content }}
	  
	{% include rightSideBar.html %}
	
	{% include footer.html %}
	
  </body>
  
</html>
```

### Notice:

* All includes are between {% %} tags
* There is a space between include, its tag, and the name of the include
* There is also a space between the include itself and include and its tag
* Content = everything in the page itself

**4.** Create a page
```html
---
layout: layoutName
---
<p>Content Goes Here</p>
```
### Notice:

* The top of the page must have 3 dashes above and below the layout key
* There is a colon at the end of *layout*
* There is a space between *layout:* and the name of the layout
* The code above must be written on the first, second, and third line (respectively) in order to work
* Spacing and punctuation must be precise or it will not work