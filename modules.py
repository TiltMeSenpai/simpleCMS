from tornado.web import UIModule
import re

snippet = re.compile(r"^(?:\<h[1-9]\>.*?\</h[1-9]\>)?((?:(?:.|\n)+?</p>){0,2})")

class Entry(UIModule):
    def render(self, path, **kwargs):
        return self.render_string(path, **kwargs)

class Snippet(UIModule):
    def render(self, path, **kwargs):
        return self.render_string(
                "snippet.html",
                title=path.split('/')[-1][:-5].replace('_', ' '),
                snippet=snippet.findall(Entry(self).render(path, **kwargs).decode())[:1][0],
                link='/'+path[6:]
                )
