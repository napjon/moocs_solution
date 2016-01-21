# Use the BeautifulSoup module to define a bold_links(page) procedure
# that takes as input a string representing the contents of a web page,
# and returns a set containing all the important links on that page.
# An important link is a link that is inside a bold (<b>...</b>) element
# or that contains a bold element inside the link text.
# For example, the string in the following page variable contains 2 bold links:
# 'http://www.cs.virginia.edu/evans/' and 'http://davedavefind.appspot.com/'.
page = """
        <a href="http://duckduckgo.com">DuckDuckGo</a> is pretty good, but it isn't
<b><a href="http://www.cs.virginia.edu/evans/">Dave</a></b>'s
<a href="http://davedavefind.appspot.com/"><b>favorite</b> search engine</a> or
<a href="http://www.cs.cmu.edu/~rgs/alice-X.html"><em>soup</em></a>!
"""


html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
important = set(['http://www.cs.virginia.edu/evans/', 'http://davedavefind.appspot.com/'])

from bs4 import BeautifulSoup

# This is an example of how to work with Beautiful Soup
# For more information see the documentation at
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree
def get_all_links(page):
    soup = BeautifulSoup(page)
    links = []
    for link in soup.body.b:#soup.find_all('a'):
        links.append(link.get('href'))
    return links

def bold_links(string):
    #links = get_all_links(page)
   soup = BeautifulSoup(string)
   return set(link.get('href') for link in soup.find_all('a') \
               if (link.parent and (link.parent.name == u'b')) or link.b)
   #print links
   # return links
#soup.body.b
#string = " <b>The Dormouse's story</b>"
print bold_links(page)
# test
print bold_links(page) == important
