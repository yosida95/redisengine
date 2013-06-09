# -*- coding: utf-8 -*-

from redis.client import StrictRedis


class Connection(object):

    def __init__(self, hostname=u'localhost', port=6379, db=0):
        self.hostname = hostname
        self.port = port
        self.db = db

        self._connection = None

    def connect(self):
        if self._connection is None:
            self._connection = StrictRedis(host=self.hostname,
                                           port=self.port,
                                           db=self.db)

        return self._connection

    @property
    def connection(self):
        return self.connect()
