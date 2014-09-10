from bs4 import BeautifulSoup
import bleach
import re
import os, os.path
folder = "www.vnjpclub.com/trung-cap/soumatome-n2/han-tu/"
# folder = "temp/"
out_folder = "temp2/"
tag_black_list = ['style', 'xml', 'script']
tag_white_list = ["p"]
attr_white_list = {'*': ['title']}

# postlist = os.listdir(folder)

# for post in postlist:
#     # HERE: you need to specify the directory again, the value of "post" is just the filename:
#     text = BeautifulSoup(open(folder + post))
#     text.encode("utf-8")

#     # Step one, with BeautifulSoup: Remove tags in tag_black_list, destroy contents.
#     [s.decompose() for s in text(tag_black_list)]
#     pretty = (text.prettify())


#     # Step two, with Bleach: Remove tags and attributes not in whitelists, leave tag contents.
#     cleaned = bleach.clean(pretty, strip="TRUE", attributes=attr_white_list, tags=tag_white_list)

#     fout = open(out_folder + post, "wr+")
#     fout.write(cleaned.encode("utf-8"))
#     fout.close()
#
# file_tmp = os.listdir(out_folder)
# import codecs
# output = codecs.open("text.csv", "wr+", "utf-8")
# for file in file_tmp:
#     chapter = file[12:15]
#     text = BeautifulSoup(open(out_folder + file), from_encoding="utf-8")
#     table = text.find("table")
#     rows = table.find_all("tr")
#     for r in rows:
#         col = r.find_all("td")
#         output.write(u"\n")
#         line = chapter + ":"
#         for c in col:
#             line += c.string.strip() + ":"
#         output.write(unicode(line))
# output.close()

# get mondai.txt
# file_tmp = os.listdir(out_folder)
# import codecs
# output = codecs.open("mondai.txt", "wr+", "utf-8")
# for file in file_tmp:
#     chapter = file[9:12]
#     output.write(unicode(chapter))
#     text = BeautifulSoup(open(out_folder + file), from_encoding="utf-8")
#     pra = text.find_all("p")
#     for p in pra:
#         if p != "":
#             output.write(u"\n")
#             line = p.string.strip()
#             output.write(unicode(line))
# output.close()

#get anwser.txt
file_tmp = os.listdir(folder)
import codecs
output = codecs.open("anwser.txt", "wr+", "utf-8")
for file in file_tmp:
    chapter = file[9:12]
    output.write(unicode(chapter + "\n"))
    text = BeautifulSoup(open(folder + file), from_encoding="utf-8")
    pra = text.find_all("div", class_="candich")
    for p in pra:
        if p.string:
            line = p.string.strip()
            output.write(unicode(line + "\n"))
output.close()


#remove something and output to tmp




