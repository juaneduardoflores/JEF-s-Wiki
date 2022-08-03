---
title: Workflow for This Blog 
date_created: January 30th, 2021 
---

This entry is to document my effort in trying to create a blog without any popular content management systems (CMS) like Wordpress to have maximum flexibility in the design and layout of my website. My goal was to edit plain text files on my local computer and from the comfort of my own text editing tools. I will go over the workflow that I have developed to make writing blog entries as smooth and easy as possible, from <a target="_blank" href="https://www.markdownguide.org/">Markdown</a> to HTML to a published website.

## Pandoc
I used <a target="_blank" href="https://pandoc.org/">Pandoc</a> to compile Markdown files to HTML using one shell command. A simple command to do this conversion would be:  
```shell
$ pandoc -f markdown -t html markdownfile.md
```

`-f/--from` is a <span style="font-weight:bold; cursor: pointer;" uk-tooltip="title: A command-line <strong>flag</strong> is a common way to specify options for command-line programs.">flag</span> that specifies what file type we are starting from, and `-t/--to` is the file type we are converting to. `markdownfile.md` is the file we want to convert. This will not overwrite the file, rather it will simply create a new file in the same directory called `markdownfile.html`.

A shorter way of doing the same thing is with the `-o` flag:  
```shell
$ pandoc inputfile.md -o outputfile.html
```

`-o/--output` specifies the output file. In this example, we are specifying that we want to output to a file called `outputfile.html` using `inputfile.md` as the input. Pandoc is smart enough to look at the extensions of the input and output files to know what the `--from` and `--to` flags would be without manually entering them.

There are more flags and options, but I will only go over a few more in the following section. Visit the <a target="_blank" href="https://pandoc.org/MANUAL.html">Pandoc User Manual</a> for more information.

## Makefile
Writing a Makefile is very handy to apply the `pandoc` command to every Markdown file in a directory instead of doing it one at a time. A Makefile contains shell commands that can be executed upon running the Unix utility <a target="_blank" href="https://edoras.sdsu.edu/doc/make.html">make</a>. An advantage of using a Makefile is that it keeps track of changes so that it only applies the commands to the files we need.

Here is the file that I am currently using for this Blog site:

<ul uk-accordion>
<li class=" uk-open">
<a id="code-file" class="uk-accordion-title" href="#">Makefile</a>
<div class="uk-accordion-content">
```make
PANDOCFLAGSHTML =                                           \
  --table-of-contents                                       \
  --toc-depth=4                                             \
  --from=markdown+markdown_in_html_blocks+bracketed_spans   \
  --template=blog_template.html

# a wildcard that searches recursively
rwildcard = $(wildcard $1$2) $(foreach d,$(wildcard $1*),$(call rwildcard,$d/,$2))

# find all markdown files
MARKDOWN := $(call rwildcard,./,*.md)
HTML = $(MARKDOWN:.md=.html)

all: $(HTML)

%.html: %.md
	@echo $@
	pandoc $< -o $@ $(PANDOCFLAGSHTML)
	python newBlogEntry.py $(@D)

clean:
	rm $(HTML)
```
</div>
</li>
</ul>

Now that we understand what Pandoc does, I can say that `PANDOCFLAGSHTML` is a variable containing all the flags that I am using with the `pandoc` command.

The complete command that I am using looks something like this:
```shell
$ pandoc markdownFile/markdownFile.md -o markdownFile/markdownFile.html --table-of-contents --toc-depth=4 --from=markdown+markdown_in_html_blocks+bracketed_spans --metadata-file=../pandoc/metadata.yaml --template=../pandoc/blog_template.html
```

- `--table-of-contents`: Outputs the html file with a table of contents. You can see what it made on this blog entry by clicking on the menu icon (<span uk-icon="menu"></span>) on the upper left side.

- `--toc-depth=4`: This will make headings in the table of contents have a maximum depth of 4, meaning that it will only include headings 1 through 4.

- `--from=markdown+markdown_in_html_blocks+bracketed_spans`: We are defining the filetype of the input file, but also extending the syntax to also include `markdown_in_html_blocks` and `bracketed_spans`. Read more about this <a target="_blank" href="https://boisgera.github.io/pandoc/markdown/">here</a>.

- `--template=../pandoc/blog_template.html`: Finally we specify the template file. This is crucial to have a consistent Blog layout. 

Below is a simple html template. The `$body$` variable will be replaced by the converted markdown content.

<ul uk-accordion>
<li class=" uk-open">
<a class="uk-accordion-title" href="#">blog_template.html</a>
<div class="uk-accordion-content">
```HTML
<!DOCTYPE html>
<html>
  <head>
    <title>$title$</title>
  </head>

  <body>
  $body$
  </body>
</html>
```
</div>
</li>
</ul>

Here is a directory structure example:
```bash
.
├── index.html
├── Blog/
│   ├─── Makefile
│   ├─── blog_template.html
│   ├─── Example_topic/
│   │       Example_topic.md
│   #       Example_topic.html (generated after running make)
```

The rest would be to design the website style. I use <a target="_blank" href="https://getuikit.com/">UIkit</a> as a front-end framework, <a target="_blank" href="https://highlightjs.org/">highlight.js</a> for code syntax highlighting, and <a target="_blank" href="https://disqus.com/">Disqus</a> for adding user comments. The site is hosted on <a target="_blank" href="https://pages.github.com/">Github Pages</a>.

---

## Inspiration
Here is a list of blogs that I have looked at and have been inspired by:

  - [https://timrodenbroeker.de/category/all/](https://timrodenbroeker.de/category/all/)
