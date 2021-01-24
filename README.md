# Blog
One of my goals is to make it fast and easy to manage my blog without having to create new html files each time. I tried to simplify the process by implementing a python script and a Makefile.

## The python script: **newBlogEntry.py**
By running the script, the user is prompted to provide a title for a blog entry along with a description. It will create the directory and files necessary, except for the cover image which can be provided later. The script will also add the html code necessary in `blog.html`. 

If an argument is provided that matches a title of a post, it will update the modified_time value to the current date.

## The Makefile
By running `make` inside the Blog directory, it will look for any markdown files in the subdirectories that have changes and will convert them to html using the blog template.
