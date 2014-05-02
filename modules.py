from tornado.web import UIModule
import re

snippet = re.compile(r"(^(?:(?:.|\n)+?<br/>){2})")

class Entry(UIModule):
    def render(self, path, **kwargs):
        return self.render_string(path, **kwargs)

class Snippet(UIModule):
    def render(self, path, **kwargs):
        return self.render_string(
                "snippet.html",
                title=path.split('/')[-1][:-5],
                snippet="".join(snippet.findall(Entry(self).render(path, **kwargs))[:1]),
                link='/'+path
                )
