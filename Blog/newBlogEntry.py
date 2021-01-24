# A script that I execute if I ever want to create a new blog entry.
# Steps:
#   1.) Asks me for the title of entry:
#       - creates new directory and directory.md file with template.
#   2.) Adds the html code for this new entry.

import os
import re
import json
import sys
from datetime import date

today = date.today()
blogEntryTitle = "temp"
blogEntryDescription = "temp description"
last_modified = str(today)
tags = ""
inputTitle = ""


def main():
    global blogEntryTitle, blogEntryDescription, last_modified, tags, inputTitle

    # If an argument was passed, we are updating, else we are creating
    if (len(sys.argv) > 1):
        inputTitle = str(sys.argv[1])
        updateEntry()
        sys.exit(0)
    else:

        blogEntryTitle = input("Enter new blog entry title: ")
        blogEntryDescription = input(
            "Enter a short description for {}: ".format(blogEntryTitle))
        os.mkdir(blogEntryTitle)
        os.mkdir(blogEntryTitle + "/cover_img")
        print("created directory called " + blogEntryTitle)
        f = open("{}/{}.md".format(blogEntryTitle, blogEntryTitle), "w+")

        addEntrytoHTML()

        with open('entries.json', 'r') as json_file:
            data = json_file.read()

        objs = json.loads(data)
        obj_keys = objs.keys()
        for key in objs:
            print("key: " + key + " " + str(objs[key]))


def updateEntry():
    global blogEntryTitle, blogEntryDescription, last_modified, tags

    htmlFile = open("../blog.html", "r").read()
    entries_raw = re.findall(
        '<!-- BLOG ENTRIES -->(.*?)<!-- BLOG ENTRIES END -->', htmlFile, re.DOTALL)
    lineiterator = iter(entries_raw[0].splitlines())
    entries = []
    cur_entry = ""
    found_entry = False
    modifying_date = False
    for l in lineiterator:
        if (found_entry):

            if (modifying_date):
                if (re.match('.*\d{4}-\d{2}-\d{2}.*', l)):
                    print("CHANGING ENTRY MODIFIED DATE")
                    today = date.today()
                    l = re.sub("\d{4}-\d{2}-\d{2}", str(today), l)

            if (re.match('\w*', l)):
                print("appending!")
                print(l)
                cur_entry += str(l)

            if (l == ""):
                print("ADDING TO LIST..")
                cur_entry += "\n"
                entries.append(cur_entry)
                cur_entry = ""
                found_entry = False
                modifying_date = False

        if (re.search('<!--', l)):
            print("LOOK AT ME: " + l)
            if (re.match('.*<!-- {} -->'.format(inputTitle), l)):
                modifying_date = True
            cur_entry += str(l)
            found_entry = True

    sep = '<!-- BLOG ENTRIES -->'
    stripped = htmlFile.split(sep, 1)[
        0] + sep + "<div class='uk-container uk-margin-remove uk-padding-remove'>"

    for entry in entries:
        print(entry)
        stripped += entry + "\n"

    stripped += "\n\n<!-- BLOG ENTRIES END -->"

    print(stripped)
    f = open("../blog.html", "w")
    f.write(stripped)
    f.close()

    # run prettier on file.
    os.system("npx prettier --write ../blog.html")


def addEntrytoHTML():
    global blogEntryTitle, blogEntryDescription, last_modified, tags

    htmlFile = open("../blog.html", "r").read()
    entries_raw = re.findall(
        '<!-- BLOG ENTRIES -->(.*?)<!-- BLOG ENTRIES END -->', htmlFile, re.DOTALL)
    lineiterator = iter(entries_raw[0].splitlines())
    entries = []
    cur_entry = ""
    found_entry = False
    for l in lineiterator:
        if (found_entry):
            # if (re.match('.*\d{4}-\d{2}-\d{2}.*', l)):
            #     print("CHANGING ENTRY MODIFIED DATE")
            #     today = date.today()
            #     l = re.sub("\d{4}-\d{2}-\d{2}", str(today), l)

            if (re.match('\w*', l)):
                print("appending!")
                print(l)
                cur_entry += str(l)

            if (l == ""):
                print("ADDING TO LIST..")
                cur_entry += "\n"
                entries.append(cur_entry)
                cur_entry = ""
                found_entry = False

        if (re.search('<!--', l)):
            print(l)
            cur_entry += str(l)
            found_entry = True

    template = "\n\n<!-- {} -->\n".format(blogEntryTitle)
    if (len(entries) % 2 == 0):
        template += "<a href='./Blog/{}/{}.html'>\n".format(
            blogEntryTitle, blogEntryTitle)
        template += "<div class='uk-card uk-card-default uk-grid-collapse uk-child-width-1-2@s uk-margin' uk-grid >"
        template += "<div class='uk-card-media-left uk-cover-container'>"
        template += "<img src='./Blog/Processing_P3D/resources/11_P3D.gif' alt='' uk-cover />"
        template += "<canvas width='600' height='400'></canvas>"
        template += "</div>"
        template += "<div> <div class='uk-card-body'> <h3 class='uk-card-title'> {} <span class='uk-text-warning'>(WIP)</span> </h3> <span>last modified: {} </span> <p> {} </p> </div> </div>".format(
            blogEntryTitle, last_modified, blogEntryDescription)
        template += "</div> </a>\n\n"
        template += "<!-- BLOG ENTRIES END -->"
        template += "</div></div></body></html>"

    else:
        template += "<a href='./Blog/{}/{}.html'>\n".format(
            blogEntryTitle, blogEntryTitle)
        template += "<div class='uk-card uk-card-default uk-grid-collapse uk-child-width-1-2@s uk-margin' uk-grid >"
        template += "<div> <div class='uk-card-body'> <h3 class='uk-card-title'> {} <span class='uk-text-warning'>(WIP)</span> </h3> <span>last modified: {} </span> <p> {} </p> </div> </div>".format(
            blogEntryTitle, last_modified, blogEntryDescription)
        template += "<div class='uk-card-media-left uk-cover-container'>"
        template += "<img src='./Blog/Processing_P3D/resources/11_P3D.gif' alt='' uk-cover />"
        template += "<canvas width='600' height='400'></canvas>"
        template += "</div>"
        template += "</div> </a>\n\n"
        template += "<!-- BLOG ENTRIES END -->"
        template += "</div></div></body></html>"

    entries.append(template)

    sep = '<!-- BLOG ENTRIES -->'
    stripped = htmlFile.split(sep, 1)[
        0] + sep + "<div class='uk-container uk-margin-remove uk-padding-remove'>"

    for entry in entries:
        print(entry)
        stripped += entry + "\n"

    print(stripped)
    f = open("../blog.html", "w")
    f.write(stripped)
    f.close()

    # run prettier on file.
    os.system("npx prettier --write ../blog.html")


main()
