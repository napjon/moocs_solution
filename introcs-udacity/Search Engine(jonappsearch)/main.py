#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
form = """

<html>
  <head>
    <title>Search Engine</title>
  </head>

  <body>
    <h2>Search Engine</h2>
    <form method="post">
      <textarea name="text">%(text)s</textarea>
      <br>
      <input type="submit">
      <br>
      <br>
      <br>
      %(links)s
    </form>
  </body>

</html>
"""

import webapp2

import cgi

from search import lucky_search
from crawler import crawl_web, compute_ranks

class MainHandler(webapp2.RequestHandler):
    def render(self, text = "", links = ""):
        return self.response.write(form%{'text' :self.escape_html(text),
                                  'links':self.escape_html(links)})
    def get(self):
        self.render()


    def escape_html(self,s):

        return cgi.escape(s, quote = True)

    def post(self):

        corpus, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
        ranks = compute_ranks(graph)
        query = self.request.get('text')
        result = lucky_search(corpus, ranks, query)
        if not result:
            self.render(text = "", links = "try www.google.com")
        else:
            self.render(text = query, links = result)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

