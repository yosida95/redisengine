# -*- coding: utf-8 -*-

import unittest

from mock import patch

from redisengine.connection import Connection


class ConnectionTest(unittest.TestCase):

    def test_constructor(self):
        inst = Connection()
        self.assertEqual(inst.hostname, u'localhost')
        self.assertEqual(inst.port, 6379)
        self.assertEqual(inst.db, 0)

        inst = Connection(hostname=u'example.com', port=6378, db=1)
        self.assertEqual(inst.hostname, u'example.com')
        self.assertEqual(inst.port, 6378)
        self.assertEqual(inst.db, 1)

    def test_connect(self):
        with patch(u'redisengine.connection.StrictRedis') as mock:
            mock.return_value = True

            inst = Connection()
            self.assertIs(inst.connect(), True)
            self.assertIs(inst.connection, True)

            kwargs = mock.call_args[1]
            self.assertEqual(kwargs[u'host'], u'localhost')
            self.assertEqual(kwargs[u'port'], 6379)
            self.assertEqual(kwargs[u'db'], 0)

    def test_connection(self):
        with patch(u'redisengine.connection.StrictRedis') as mock:
            value = mock.return_value

            inst = Connection()
            self.assertEqual(inst.connection, value)
