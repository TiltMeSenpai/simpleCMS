import re
import os
import tornado
import inspect
import modules
from tornado.web import HTTPError
from tornado.template import *
import argparse
from markdown2 import markdown

class Config():
    port = 80
    title = "Yet Another CMS"
    debug = True
    def __init__(self, **kwargs):
        p = argparse.ArgumentParser()
        p.add_argument('-p', type=int, default=8080, dest='port')
        p.add_argument('-d', default=False, dest='debug', action='store_true')
        args = p.parse_args()
        for arg in args.__dict__:
            setattr(self, arg, args.__dict__[arg])
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

cwd=os.getcwd()
pages = {}
for i in next(os.walk('templates/posts'))[1]:
    pages.update({i:{}})
    for j in next(os.walk(os.path.join('templates/posts', i)))[1]:
        pages[i].update({j:[i for i in next(os.walk(os.path.join('templates/posts',i ,j)))[2] if i[0] != '.']})
print(pages)

class BaseHandler(tornado.web.RequestHandler):
    pass

class HomeHandler(BaseHandler):
    def get(self):
        send = self.render('home.html', no_comments=True, pages=pages)

class ArchiveHandler(BaseHandler):
    def get(self, *time):
        pagelist = []
        if not time:
            for year in sorted([int(i) for i in pages])[::-1]:
                for month in sorted([int(i) for i in pages[str(year)]])[::-1]:
                    for page in pages[str(year)][str(month)][::-1]:
                        pagelist.append(os.path.join('posts', str(year), str(month), str(page)))
        else:
            if not time[0] in pages or not time[1] in pages[time[0]]:
                raise HTTPError(404)
            for page in pages[time[0]][time[1]]:
                pagelist.append(os.path.join('posts', time[0], time[1], page))
        print(pagelist)
        self.render('archive.html', pagelist=pagelist, pages=pages, time=time)

class EntryHandler(BaseHandler):
    def get(self, *post):
        print(post)
        self.render('post.html', path=os.path.join('posts', *[i for i in post])+".md", pages=pages)

class ISTA301Handler(BaseHandler):
    def get(self):
        self.render('ista301posts.html', pages=pages)

def start(config = Config()):
    server = tornado.web.Application(
        [
            (r"/?", HomeHandler),
            (r"/archive/?", ArchiveHandler),
            (r"/([0-9]{4})/([0-9]{1,2})/?", ArchiveHandler),
            (r"/([0-9]{4})/([0-9]{1,2})/([^/]*?)(?:.html?)?", EntryHandler),
            (r"/ista301/?", ISTA301Handler)
        ],
        title= config.title,
        template_path= os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=config.debug,
        ui_modules=modules,
        compress_whitespace=False
        )
    server.listen(config.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    start()
