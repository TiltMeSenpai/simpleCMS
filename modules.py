from tornado.web import UIModule
import re

snippet = re.compile(r"\s?(?:\<h[1-9]\>.*?\</h[1-9]\>)?((?:(?:.|\n)+?</p>){0,2})")

class Entry(UIModule):
    def render(self, path, **kwargs):
        return self.render_string(path, **kwargs)

class Snippet(UIModule):
    def render(self, path, **kwargs):
        return self.render_string(
                "snippet.html",
                title=path.split('/')[-1][:-5].replace('_', ' '),
                snippet=snippet.match(Entry(self).render(path, **kwargs).decode()).group(1),
                link='/'+path[6:]
                )
