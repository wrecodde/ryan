# test app server for ryan

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

import os

from tornado.options import define
define("port", default=7926, type=int)

class BaseHandler(tornado.web.RequestHandler):
	pass

class IndexHandler(BaseHandler):
	def get(self):
		self.render("index.html")
	
	def post(self):
		pass

class AppHandler(BaseHandler):
	def get(self):
		pass
	
	def post(self):
		pass

handlers = [
	(r"/", IndexHandler),
	(r"/app", AppHandler),
]

settings = dict(
	debug = True,
	static_path = os.path.join(os.getcwd(), "assets"),
	template_path = os.path.join(os.getcwd(), "pages"),
)

app = tornado.web.Application(
	handlers,
	**settings,
)

def start():
	tornado.options.parse_command_line()
	server = tornado.httpserver.HTTPServer(app)
	server.listen(tornado.options.options.port)
	
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	start()