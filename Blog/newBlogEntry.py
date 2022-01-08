#!/usr/bin/python
# -*- coding: utf-8 -*-

# A script that I execute if I ever want to create a new blog entry.
# Steps:
#   1.) Asks me for the title of entry:
#       - creates new directory and directory.md file with template.
#   2.) Adds the html code for this new entry.

import os
import re
import json
import sys
import random
from datetime import date
from pathlib import Path

today = date.today()
blogEntryTitle = "temp"
blogEntryDescription = "temp description"
blogEntryTags = ""
last_modified = str(today)
tags = []
inputTitle = ""
added_new_tag = False


def main():
    global blogEntryTitle, blogEntryDescription, blogEntryTags, last_modified, tags, inputTitle, added_new_tag

    # If an argument was passed, we are updating, else we are creating
    if (len(sys.argv) > 1):
        inputTitle = str(sys.argv[1])
        updateEntry()
        sys.exit(0)

    else:
        blogEntryTitle = input("Enter new blog entry title: ")
        blogEntryDescription = input(
            "Enter a short description for {}: ".format(blogEntryTitle))
        blogEntryTags = input("Enter any tags followed by comma: ")
        tags = blogEntryTags.split(",")
        os.mkdir(blogEntryTitle.replace(" ", "_"))
        os.mkdir(blogEntryTitle.replace(" ", "_") + "/cover")
        f = open("{}/{}.md".format(blogEntryTitle.replace(" ", "_"),
                                   blogEntryTitle.replace(" ", "_")), "w+")

        f.write(
            "---\ntitle: {}\ndate_created: {}\n---".format(blogEntryTitle, last_modified))

        addEntrytoHTML()

        if (added_new_tag):
            with open('tags.json', 'r') as tags_file:
                json_data = json.load(tags_file)

            tags_html = ""

            for tag in json_data:
                tagClassifier = tag.strip().replace(" ", "_")
                tagName = tag
                tagColor = str(json_data[tag])
                list_element = "<li uk-filter-control='.tag-{}'><a href='#'>\n<span class='uk-label' style='background-color: {}; color: white'>{}</span>\n</a>\n</li>\n".format(
                    tagClassifier, tagColor, tagName)
                tags_html += list_element + "\n"

            htmlFile = open("../blog.html", "r+")
            htmlFilestr = htmlFile.read()

            septop = '<!-- START TAGS -->'
            sepbottom = '<!-- END TAGS -->'
            top = htmlFilestr.split(septop, 1)[0]
            bottom = htmlFilestr.split(sepbottom, 1)[1]

            newhtml = top + septop + tags_html + sepbottom + bottom

            htmlFile.seek(0)
            htmlFile.write(newhtml)
            htmlFile.truncate()
            htmlFile.close()


def updateEntry():
    global blogEntryTitle, blogEntryDescription, blogEntryTags, last_modified, tags, today

    htmlFile = open("../blog.html", "r").read()
    entries_raw = re.findall(
        '<!-- BLOG ENTRIES -->(.*?)<!-- BLOG ENTRIES END -->', htmlFile, re.DOTALL)
    lineiterator = iter(entries_raw[0].splitlines())
    entries = []
    cur_entry = ""
    found_entry = False
    modifying_date = False
    index = 0
    target_index = 0
    for l in lineiterator:
        if (found_entry):

            if (modifying_date):
                if (re.match('.*\d{4}-\d{2}-\d{2}.*', l)):
                    print("CHANGING ENTRY MODIFIED DATE")
                    l = re.sub("\d{4}-\d{2}-\d{2}", str(today), l)

            if (re.match('\w*', l)):
                # print("appending!")
                # print(l)
                cur_entry += str(l)

            if (l == ""):
                # print("ADDING TO LIST..")
                index += 1
                cur_entry += "\n"
                entries.append(cur_entry)
                if (modifying_date):
                    target_index = index
                    print("target_index: " + str(target_index))
                cur_entry = ""
                found_entry = False
                modifying_date = False

        if (re.search('<!--', l)):
            print("LOOK AT ME: " + l)
            # take into account regex special characters
            inputTitlestr = inputTitle
            inputTitlestr = inputTitlestr.replace('+', '\+')
            print(inputTitlestr)
            if (re.match('.*<!-- {} -->'.format(inputTitlestr.replace('_', ' ')), l)):
                print("MODIFYING TIME...")
                modifying_date = True
            cur_entry += str(l)
            found_entry = True

    sep = '<!-- BLOG ENTRIES -->'
    header = htmlFile.split(sep, 1)[
        0] + sep + "<ul class='js-filter uk-list uk-width-2-3@s uk-align-center'>"

    stripped = ""
    updated_entry = ""
    entry_index = 0
    for entry in entries:
        entry_index += 1
        if (entry_index == target_index):
            updated_entry = entry + "\n"
            print("found entry...")
            continue
        stripped += entry + "\n"

    stripped += "\n\n<!-- BLOG ENTRIES END --></ul><script id='dsq-count-scr' src='//juanedflores-blog.disqus.com/count.js' async></script>"
    htmlcode = header + updated_entry + stripped

    f = open("../blog.html", "w")
    f.write(htmlcode)
    f.close()

    # run prettier on file.
    os.system("npx prettier --write ../blog.html")


def addEntrytoHTML():
    global blogEntryTitle, blogEntryDescription, blogEntryTags, last_modified, tags

    htmlFile = open("../blog.html", "r").read()
    entries_raw = re.findall(
        '<!-- BLOG ENTRIES -->(.*?)<!-- BLOG ENTRIES END -->', htmlFile, re.DOTALL)
    lineiterator = iter(entries_raw[0].splitlines())
    entries = []

    template = "\n\n<!-- {} -->\n".format(blogEntryTitle)
    tagfilter = ""
    for tag in tags:
        tag = tag.strip()
        tag = tag.replace(" ", "_")
        tagfilter += "tag-" + tag + " "

    print("adding tags: " + tagfilter)
    template += "<li class='{}'>".format(tagfilter)
    template += "<a href='https://juanedflores.com/Blog/{}/{}.html#disqus_thread'>Link</a>".format(
        blogEntryTitle.replace(" ", "_"), blogEntryTitle.replace(" ", "_"))
    template += "<a href='./Blog/{}/{}.html'>\n".format(
        blogEntryTitle.replace(" ", "_"), blogEntryTitle.replace(" ", "_"))
    template += "<div class='uk-card uk-card-default uk-grid-collapse uk-child-width-1-2@s uk-margin' uk-grid>"
    template += "<div class='uk-background-cover' uk-img> <div class='uk-card-body'> <h3 class='uk-card-title'> {} <span class='uk-text-warning'>(WIP)</span> </h3> <span>last modified: {} </span> <p> {} </p>".format(
        blogEntryTitle, last_modified, blogEntryDescription)

    #  add tags
    template = addTags(template)

    template += "</div></div>"
    template += "<div class='uk-card-media-left uk-cover-container'>"
    template += "<img src='./Blog/{}/cover/cover.png' alt='' uk-cover />".format(
        blogEntryTitle.replace(" ", "_"))
    template += "<canvas width='600' height='400'></canvas>"
    template += "</div>"
    template += "</div> </a></li>\n\n"

    entries.append(template)

    cur_entry = ""
    found_entry = False
    for l in lineiterator:
        if (found_entry):
            if (re.match('\w*', l)):
                cur_entry += str(l)

            if (l == ""):
                cur_entry += "\n"
                entries.append(cur_entry)
                cur_entry = ""
                found_entry = False

        if (re.search('<!--', l)):
            cur_entry += str(l)
            found_entry = True

    sep = '<!-- BLOG ENTRIES -->'
    stripped = htmlFile.split(sep, 1)[
        0] + sep + "<ul class='js-filter uk-list uk-width-2-3@s uk-align-center'>"

    for entry in entries:
        stripped += entry + "\n"

    stripped += "<!-- BLOG ENTRIES END -->"
    stripped += "</ul></div></div><script id='dsq-count-scr' src='//juanedflores-blog.disqus.com/count.js' async></script></body></html>"

    # print(stripped)
    f = open("../blog.html", "w")
    f.write(stripped)
    f.close()

    # run prettier on file.
    os.system("npx prettier --write ../blog.html")
    os.system("npx prettier --write ./tags.json")


def addTags(template):
    global added_new_tag

    if (len(tags) > 0):
        json_file = open("tags.json", "r")
        data = json_file.read()
        objs = json.loads(data)
        json_file.close()

        for tag in tags:
            tag = tag.strip()

            tag_color = "#FFFFFF"

            keyfound = False
            for key in objs:
                if (key.upper() == tag.upper()):
                    keyfound = True
                    tag_color = objs[key]
                    newtag = "<span class='uk-label' style='background-color: {}'>{}</span>\n".format(
                        tag_color, tag)

            if (not keyfound):
                # random hex color
                random_number = random.randint(0, 16777215)
                hex_number = format(random_number, 'x')
                hex_number = '#'+hex_number

                objs[tag] = hex_number
                tag_color = objs[tag]
                print(objs)
                json_file = open("tags.json", "w+")
                json_obj = json.dumps(objs, indent=2)
                json_file.write(str(json_obj))
                newtag = "<span class='uk-label' style='background-color: {}'>{}</span>\n".format(
                    tag_color, tag)

            template += newtag
            json_file.close()
            added_new_tag = True

    return template


main()
