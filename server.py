#!/usr/bin/env Python
# coding=utf-8

import os
import tornado.ioloop
import tornado.httpserver
import tornado.web

from application import application


def main():

    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    print("Development server is running at http://127.0.0.1:%s" % port)
    print("Quit the server with Control-C")

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()