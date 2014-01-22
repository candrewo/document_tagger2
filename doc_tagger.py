import sys
import re
import os

directory = sys.argv[1]
 
title_search = re.compile(r"""
  (title:\s*) # searches for "title"
  (?P<title>( # named group
    (\S*      # 0 or more non-white spaces
      (\ ?)   # escapes the space in the verbose regex (0 or 1)
      )+      # 1 or more of stated pattern
)
(\n+          # searches for new line (1 or more)
  (\ *))      # looks for 0 or more spaces from the new line
(\S*          # o or more non-white spaces
  (\ ?)       # escapes the space in the verbose regex (0 or 1)
  )+)""", re.IGNORECASE | re.VERBOSE) 

author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

keyword = {}
for kw in sys.argv[2:]:
  keyword[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)

for fl in (os.listdir(directory)):
  if fl.endswith('.txt'):       #if it's a text file
    fl_path = os.path.join(directory, fl) #the full path to the file is the directory plus
    with open(fl_path, 'r') as f:         #open the file as f
      doc = f.read()      #for each item that appears in the directory
  title = re.search(title_search, doc).group('title')
  author = re.search(author_search, doc)
  translator = re.search(translator_search, doc)
  illustrator = re.search(illustrator_search, doc)
  if author: 
    author = author.group('author')
  if translator:
    translator = translator.group('translator')
  if illustrator:
    illustrator = illustrator.group('illustrator')
  print "***" * 25
  print "Title:  {}".format(title)
  print "Author(s): {}".format(author)
  print "Translator(s): {}".format(translator)
  print "Illustrator(s): {}".format(illustrator)
  print "\n"
  print "Here are the counts for keywords entered:"
  for search in keyword:
    print "\"{0}\": {1}".format(search, len(re.findall(keyword[search], doc)))
  print "***" * 25