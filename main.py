import re
import os
import tornado
import inspect
import modules
from tornado.web import HTTPError
from tornado.template import *
import argparse

class Config():
    port = 80
    title = "Yet Another CMS"
    debug = True
    def __init__(self, **kwargs):
        p = argparse.ArgumentParser()
        p.add_argument('-p', type=int, default=80, dest='port')
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
        pages[i].update({j:[i for i in next(os.walk(os.path.join('templates/posts',i ,j)))[2]]})
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
        self.render('archive.html', pagelist=pagelist, pages=pages)

class EntryHandler(BaseHandler):
    def get(self, *post):
        print(post)
        self.render('post.html', path=os.path.join('posts',*[i for i in post])+".html", pages=pages)

def start(config = Config()):
    server = tornado.web.Application(
        [
            (r"/?", HomeHandler),
            (r"/archive/?", ArchiveHandler),
            (r"/([0-9]{4})/([0-9]{1,2})/?", ArchiveHandler),
            (r"/posts/([0-9]{4})/([0-9]{1,2})/([^/]*?)(?:.html?)?", EntryHandler)
        ],
        title= config.title,
        template_path= os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=config.debug,
        ui_modules=modules
        )
    server.listen(config.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    start()
