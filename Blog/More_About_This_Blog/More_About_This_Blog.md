---
title: More About This Blog 
date_created: January 30th, 2021 
---


### Workflow
The goal was to be able to easily create and modify blog entries without worrying about writing any HTML code. I have created a workflow that allows me to just write in the markdown format. I achieved this by using a Makefile and a python script.

#### The Makefile
```make

PANDOCFLAGSHTML =                                           \
  --table-of-contents                                       \
  --toc-depth=4                                             \
  --from=makrdown+markdown_in_html_blocks+bracketed_spans   \
  --template=../pandoc/blog_template.html

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

#### Explanation  
I am using [pandoc](https://pandoc.org/){target="&#95;blank"} to convert markdown to html.  

A simple command to do this conversion would be:  
```shell
$ pandoc -f markdown -t html markdownfile.md
```

`-f/--from` is a <span style="font-weight:bold; cursor: pointer;" uk-tooltip="title: A Command-line flag is a common way to specify options for command-line programs.">flag</span> that specifies what file type we are starting from, and `-t/--to` is the file type we are converting to. 

Another way to do it is with the `-o` flag:  
```shell
$ pandoc inputfile.md -o outputfile.html
```

`-o/--output` specifies the output file. In this example, we are specifying that we want to output to a file called `outputfile.html`. Pandoc is smart enough to look at the extensions of the input and output files to know what we are converting from and to.

---

Now that we understand what pandoc does, I can explain that all this Makefile does is look for every markdown file in the subdirectories and turns them into html. The `PANDOCFLAGSHTML` variable contains all the flags I am using with the pandoc command.

So in the end it is running something like this:
```shell
$ pandoc markdownFile/markdownFile.md -o markdownFile/markdownFile.html --table-of-contents --toc-depth=4 --from=markdown+markdown_in_html_blocks+bracketed_spans --metadata-file=../pandoc/metadata.yaml --template=../pandoc/blog_template.html -V mainfont="DejaVu Serif" -V monofont="DejaVu Sans Mono"
```

`--table-of-contents`: Outputs the html file with a table of contents. 


### Inspiration
Here are a list of blogs that I took inspiration from.  
  - [https://timrodenbroeker.de/category/all/](https://timrodenbroeker.de/category/all/)
