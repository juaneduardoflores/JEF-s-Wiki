PANDOCFLAGSHTML =                                           \
  --table-of-contents                                       \
  --toc-depth=4                                             \
  --from=markdown+markdown_in_html_blocks+bracketed_spans   \
  --metadata-file=/Users/juaneduardoflores/Documents/Websites/ArtistWebsite/pandoc/metadata.yaml                   \
  --template=/Users/juaneduardoflores/Documents/Websites/ArtistWebsite/pandoc/blog_template.html                   \
  -V mainfont="DejaVu Serif"                                \
  -V monofont="DejaVu Sans Mono"

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
