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
HTML=$(ALL_MARKDOWN:.md=.html)

DIRECTORY = $(sort $(dir $(wildcard ./*/)))

	# @echo converting $(@D)/$(@F)
	# for f in $(ALL_MARKDOWN); do pandoc $$f -o $@ $(PANDOCFLAGSHTML); done

all: $(HTML) 

$(HTML): $(ALL_MARKDOWN)
	pandoc $(@D)/$(@D).md -o $@ $(PANDOCFLAGSHTML)

clean:
	rm $(HTML)
