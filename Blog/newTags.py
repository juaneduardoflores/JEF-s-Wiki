import os
import json
import re


def main():

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


main()
