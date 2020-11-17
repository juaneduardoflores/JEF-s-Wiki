.PHONY: all clean output open

PANDOCFLAGSPDF =                                       \
  --table-of-contents                                  \
  --include-in-header ./pandoc/latex/chapter_break.tex \
  --include-in-header ./pandoc/latex/inline_code.tex   \
  --pdf-engine=xelatex                                 \
  --from=markdown                                      \
  --highlight-style=./pandoc/pygments.theme            \
  -V mainfont="DejaVu Serif"                           \
  -V monofont="DejaVu Sans Mono"                       \
  -V linkcolor:blue                                    \
  -V geometry:a4paper                                  \
  -V geometry:margin=2cm

PANDOCFLAGSHTML =                                      \
  --table-of-contents                                  \
  -V toc-title="Work"                                  \
  --from=markdown+markdown_in_html_blocks                          \
  --metadata-file=./pandoc/metadata.yaml               \
  --template=./pandoc/template.html                    \
  --highlight-style=./pandoc/pygments.theme            \
  --shift-heading-level-by=1                           \
  -V mainfont="DejaVu Serif"                           \
  -V monofont="DejaVu Sans Mono"

SRC = Work.md

## Using Substitution reference to define the target pdf file
PDF=$(SRC:.md=.pdf)
HTML=$(SRC:.md=.html)
EPUB=$(SRC:.md=.epub)

all: $(HTML)

%.html: %.md
	pandoc $< -o index.html $(PANDOCFLAGSHTML)
	yarn prettier --write index.html
	
output:
	mkdir ./$(OUTPUTFLDR)

clean:
	rm -rf ./output

open: $(OUTPUTFLDR)/$(PDF)
	open output/Algos4ArtistsBook.pdf
