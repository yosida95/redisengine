# -*- coding: utf-8 -*-

from .connection import Connection


class SessionBase(object):
    _connection = None

    def bind(self, connection):
        assert isinstance(connection, Connection)

        self._connection = connection


def sessionmaker(connection=None):
    def constructor(self, connection=None):
        self.connection = connection

    _dict = {
        u'_connection': connection
    }
    return type('Session', (SessionBase, ), _dict)
