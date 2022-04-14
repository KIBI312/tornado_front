import tornado.ioloop
import tornado.web
import logging
import shlex
import subprocess
import tornado
import yaml

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        app_id=3
		with open("both.yaml", mode='r') as f:
			content = f.read()
		with open(('config-%s.yaml' % app_id), 'x') as f:
			f.write(content.replace('{{ id }}', ('%s' % app_id)))
        spawn_portal = subprocess.run(['kubectl', 'apply', '-f', ('%s' % app_id)], capture_output=True)
		app_id+=1

def make_app():
    return tornado.web.Application([
        (r"/create_portal", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
