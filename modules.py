from tornado.web import UIModule
import re
import os
from CommonMark import HTMLRenderer, DocParser

snippet = re.compile(r"((?:(?:.|\n)+?(?:</p>|</div>)){0,2})")
stripHeaders = re.compile(r"(<h[1-9]>(?:.|\n)*?</h[1-9]>)")

class Entry(UIModule):
    parser = DocParser()
    renderer = HTMLRenderer()
    def render(self, path, **kwargs):
        return self.renderer.render(self.parser.parse(self.render_string(path, **kwargs).decode()))


class Snippet(UIModule):
    def render(self, path, **kwargs):
        return self.render_string(
            "snippet.html",
            title=os.path.splitext(path.split('/')[-1])[0].replace('_', ' '),
            snippet=stripHeaders.sub("", snippet.match(Entry(self).render(path, **kwargs)).group(1)),
            link=os.path.splitext(path)[0][5:]
        )
