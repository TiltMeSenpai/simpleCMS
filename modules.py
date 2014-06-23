from tornado.web import UIModule
import re

snippet = re.compile(r"((?:(?:.|\n)+?(?:</p>|</div>)){0,2})")
stripHeaders = re.compile(r"(\<h[1-9]\>.*?\</h[1-9]\>)")
class Entry(UIModule):
    def render(self, path, **kwargs):
        return self.render_string(path, **kwargs)

class Snippet(UIModule):
    def render(self, path, **kwargs):
        return self.render_string(
                "snippet.html",
                title=path.split('/')[-1][:-5].replace('_', ' '),
                snippet=stripHeaders.sub("",snippet.match(Entry(self).render(path, **kwargs).decode()).group(1)),
                link='/'+path[6:]
                )
