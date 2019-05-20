# -*- coding:UTF-8 -*-
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path
from url import url
from config import config
from tornado.options import define, options
import time
import os
import sys

define('port', default=config.DEFAULT_PORT, help='run with this port', type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = url
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            xsrf_cookies=False,
            cookie_secret=config.SECRET,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    try:
        sys.path.append(os.getcwd())
        tornado.options.parse_command_line()
        http_server = tornado.httpserver.HTTPServer(Application())
        http_server.listen(options.port)
        print('this server is run with port[{}]'.format(options.port))
        tornado.ioloop.IOLoop.current().start()
    except Exception as e:
        logging.error(e)
        raise Exception('服务存在错误，已停止')
