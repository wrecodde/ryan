# api server for ryan app

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import define
define("port", default=7927, type=int)

class BaseHandler(tornado.web.RequestHandler):
	pass

class APIHandler(BaseHandler):
	def get(self):
		self.write("Its Ryan here.")
	
	def post(self):
		pass

handlers = [
	(r"/api", APIHandler),
]

settings = dict(
	debug = True,
)

api = tornado.web.Application(
	handlers,
	**settings,
)

def start():
	tornado.options.parse_command_line()
	server = tornado.httpserver.HTTPServer(api)
	server.listen(tornado.options.options.port)
	
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	start()