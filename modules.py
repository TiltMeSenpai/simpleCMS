from tornado.web import UIModule
import re

snippet = re.compile(r"(^(?:(?:.|\n)+?</p>){2})")

class Entry(UIModule):
    def render(self, path, **kwargs):
        return self.render_string(path, **kwargs)

class Snippet(UIModule):
    def render(self, path, **kwargs):
        return self.render_string(
                "snippet.html",
                title=path.split('/')[-1][:-5].replace('_', ' '),
                snippet="".join(snippet.findall(str(Entry(self).render(path, **kwargs)))[:1]),
                link='/'+path
                )
