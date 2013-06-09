# -*- coding: utf-8 -*-

import unittest

from redisengine.schema import (
    Column,
    Table
)
from redisengine.types import Integer


class TableTest(unittest.TestCase):

    def test_constructor(self):
        table = Table(u'name', Column(u'column', Integer))

        self.assertEqual(table.name, u'name')
        self.assertTrue(all(map(lambda column: isinstance(column, Column),
                                table.columns)))
        self.assertTrue(all(map(lambda column: column.table is table,
                                table.columns)))


class ColumnTest(unittest.TestCase):

    def test_constructor(self):
        column = Column(Integer, auto_increment=True)
        self.assertIs(column.table, None)
        self.assertIs(column.name, None)
        self.assertFalse(column.primary_key)
        self.assertTrue(column.nullable)
        self.assertTrue(column.auto_increment)

        column = Column(u'column', Integer(), auto_increment=True)
        self.assertIs(column.table, None)
        self.assertIs(column.name, u'column')
        self.assertFalse(column.primary_key)
        self.assertTrue(column.nullable)
        self.assertTrue(column.auto_increment)

    def test_set_table(self):
        table = Table(u'table', Column(u'column', Integer()))
        column = Column(u'column', Integer(), auto_increment=True)
        column.set_table(table)
        self.assertIs(column.table, table)

        with self.assertRaises(TypeError):
            column.set_table(table)

    def test_set_name(self):
        column = Column(Integer(), auto_increment=True)
        column.set_name(u'column')
        self.assertIs(column.name, u'column')

        with self.assertRaises(TypeError):
            column.set_name(u'column')
