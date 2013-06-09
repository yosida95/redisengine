# -*- coding: utf-8 -*-

import unittest

from redisengine.session import sessionmaker
from redisengine.connections import Connection


class SessionMakerTest(unittest.TestCase):

    def test_noargs(self):
        Session = sessionmaker()

        self.assertEqual(Session.__name__, u'Session')
        self.assertTrue(isinstance(Session, type))

    def test_with_connection(self):
        connection = Connection()
        Session = sessionmaker(connection=connection)

        self.assertIs(Session._connection, connection)


class SessionTest(unittest.TestCase):

    def test_bind(self):
        connection = Connection()
        session = sessionmaker()()
        session.bind(connection=connection)

        self.assertIs(session._connection, connection)
