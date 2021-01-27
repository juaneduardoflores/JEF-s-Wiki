## A Makefile to turn any markdown file into html with the blog template.

.PHONY: all clean output open

PANDOCFLAGSHTML =                                      \
  --table-of-contents                                  \
  --toc-depth=5                                        \
  --from=markdown+markdown_in_html_blocks              \
  --metadata-file=../pandoc/metadata.yaml              \
  --template=../pandoc/blog_template.html              \
  -V mainfont="DejaVu Serif"                           \
  -V monofont="DejaVu Sans Mono"
  # --highlight-style=../pandoc/pygments.theme           \

# a wildcard that searches recursively
rwildcard=$(wildcard $1$2) $(foreach d,$(wildcard $1*),$(call rwildcard,$d/,$2))

# find all markdown files
ALL_MARKDOWN := $(call rwildcard,./,*.md)
MARKDOWN := $(call rwildcard,./,*.md)
HTML=$(MARKDOWN:.md=.html)

DIRECTORY = $(sort $(dir $(wildcard ./*/)))

all: $(HTML) ../blog.html

# convert to html and update modified_time
# $(HTML): $(ALL_MARKDOWN)
# 	@echo $@
# 	pandoc $(@D)/$(@D).md -o $@ $(PANDOCFLAGSHTML)
# 	python newBlogEntry.py $(@D)

%.html: %.md
	@echo $@
	pandoc $< -o $@ $(PANDOCFLAGSHTML)
	python newBlogEntry.py $(@D)

../blog.html: tags.json
	@echo adding new tags to html..
	python newTags.py

clean:
	rm $(HTML)
