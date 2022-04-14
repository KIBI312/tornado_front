import tornado.ioloop
import tornado.web
import logging
import shlex
import subprocess
import tornado
import yaml

app_id = 3

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global app_id
        app_id += 1
        new_id = app_id
        with open("both.yaml", mode='r') as f:
            content = f.read()
        with open(('config-%s.yaml' % new_id), 'x') as f:
            f.write(content.replace('{{ id }}', ('%s' % new_id)))
        spawn_portal = subprocess.run(['kubectl', 'apply', '-f', ('config-%s.yaml' % new_id)])


def make_app():
    return tornado.web.Application([
        (r"/create_portal", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
