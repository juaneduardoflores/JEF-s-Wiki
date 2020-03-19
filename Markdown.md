_italic_ : underscore to make text italic
*bold* : two asterisks to make text bold
*_bold&italic_* : you can make text bold _and_ italic

Note: 
  * Making text bold or italic is often referred to as adding _emphasis_

##### Headers
To make a header in Markdown, you preface the text with a number sign ¨#¨.
Add number signs to determine header level.
# Header one
## Header two
### Header three
#### Header four
##### Header five
###### Header six

Note: 
  * Headers one and six should be used sparingly.
  * You can't make a header bold, but you can italicize certain words.
  * You can also use an alternate syntax with equal signs below header or hyphens.

##### Links
Inline link - wrap the link text in brackets "[ ]", and the link address in parenthesis "( )". 
[Visit GitHub!](www.github.com)

Note: 
  * You can add emphasis to link texts.
  * You can make links within headings too.

Reference link - a link to another place in the document. Use "[ ]" for text and another "[ ]" with text of another tag name wrapped in brackets. The referenced tag that is wrapped in brackets is also followed by a colon and a link.
Here's [a link to something else][another place].

[another place]: www.github.com

##### Images
Like links, but images are prefaced with an exclamation point "!".

Inline image link
![Benjamin Bannekat](https://octodex.github.com/images/bannekat.png)

Note:
  * You don't have to add alt text, but it will make it more accessible to people who are visually impaired and use screen readers.

Reference image link
![The founding father][Father]
[Father]: http://octodex.github.com/images/founding-father.jpg

##### Block quotes
A block quote is a sentence or paragraph that's been specially formatted to draw attention to the reader.

Preface a link with the "greater than" caret ">".

> "Block quote"

You can also place a caret character on each line of the quote. This is useful if your quote spans multiple paragraphs.

> Paragraph one
> 
> Paragraph two
>
> Paragraph three

Note: 
  * Notice that empty lines must also have the caret character.
  * Block quotes can contain other Markdown elements, such as italics, images, or links.
  * You can nest block quotes within each other.

##### Lists
  * asterisks
  * asterisks

  1. numbered
  2. numbered

Note: 
  * You can add italics, bold, or links.
  * You can nest one list within another. Just remember to indent each asterisk one space or more than the preceding item.
  * You can also use minus(-) or plus(+)
  * You can add more context to a list. For ex:
    
     This is additional context.
     > and using the caret character.
    
##### Paragraphs
soft break - add two space after each line. Also called a line break.
hard break - separate paragraph with a line.

##### Code Blocks
Normally indented four spaces or one tab. 

    <html>
      <head>
        <title>Test</title>
      </head>
      
Note: 
  * You can also use fenced code blocks. This is recommended because they're easier and support syntax highlighting.

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
      
To denote a word or phrase as code, enclose it in grave accents(`).

`This is code`

Note: 
  * If the word or phrase you want to denote as code includes one or more back ticks, you can escape it by enclosing the word or phrase in double back ticks('').

``This is code with `embedded` back ticks``

##### Horizontal Rules
To create a horizontal rule, use three or more asterisks (***), dashes (---), or underscores (___) on a line by themselves.

***

---

__________

##### URL and Email Addresses
To quickly turn a URL or email address into a link, enclose it in angle brackets.

<fake@example.com>

##### Escaping Characters
To display a literal character that would otherwise be used to format text in a Markdown document, add a backslash(\) in front of the character.

\* Without the backslash, this would be a bullet list.

##### Tables
Tables aren't part of the core Markdown spec, but they are part of GFM (GitHub Flavored Markdown).

Colons can be used to align columns.

| Example 1     | Example 2       | Example 3 |
| ------------- | :-------------: | -----:    |
| 0             | 12              | $1        |
| 1             | 0.0001          | $2        |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use Inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

##### Youtube Videos
<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
