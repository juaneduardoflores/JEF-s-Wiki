## A Makefile to turn any markdown file into html with the blog template.

.PHONY: all clean output open

PANDOCFLAGSHTML =                                      \
  --table-of-contents                                  \
  --from=markdown+markdown_in_html_blocks              \
  --metadata-file=../pandoc/metadata.yaml           \
  --template=../pandoc/blog_template.html           \
  --highlight-style=../pandoc/pygments.theme        \
  -V mainfont="DejaVu Serif"                           \
  -V monofont="DejaVu Sans Mono"

# a wildcard that searches recursively
rwildcard=$(wildcard $1$2) $(foreach d,$(wildcard $1*),$(call rwildcard,$d/,$2))

# find all markdown files
ALL_MARKDOWN := $(call rwildcard,./,*.md)
MARKDOWN := $(call rwildcard,./,*.md)
HTML=$(MARKDOWN:.md=.html)

DIRECTORY = $(sort $(dir $(wildcard ./*/)))

all: $(HTML) 

# convert to html and update modified_time
# $(HTML): $(ALL_MARKDOWN)
# 	@echo $@
# 	pandoc $(@D)/$(@D).md -o $@ $(PANDOCFLAGSHTML)
# 	python newBlogEntry.py $(@D)

%.html: %.md 
	@echo $@
	pandoc $< -o $@ $(PANDOCFLAGSHTML)
	python newBlogEntry.py $(@D)

clean:
	rm $(HTML)
