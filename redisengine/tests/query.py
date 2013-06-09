# -*- coding: utf-8 -*-

import unittest

from redisengine.schema import Column
from redisengine.session import sessionmaker
from redisengine.types import Integer
from redisengine.query import (
    Expression,
    Query
)

Session = sessionmaker()


class TestModel(object):
    __metadata__ = None

    column = Column(Integer)


class QueryTest(unittest.TestCase):

    def test_constructor(self):
        session = Session()
        query = Query(session, TestModel)

        self.assertEqual(query._session, session)
        self.assertIs(query._target, TestModel)

    def test_call(self):
        query = Query(Session(), TestModel)
        exp1 = Expression(TestModel.column, 10, Expression.eq)
        exp2 = Expression(TestModel.column, 20, Expression.ne)

        # method chain
        self.assertEqual(query(exp1, exp2), query)

        self.assertIs(len(query._expressions), 2)
        self.assertIn(exp1, query._expressions)
        self.assertIn(exp2, query._expressions)


class ExpressionTest(unittest.TestCase):

    def test_compare(self):
        exp1 = Expression(TestModel.column, 10, Expression.eq)
        exp2 = Expression(TestModel.column, 20, Expression.ne)
        exp3 = Expression(TestModel.column, 20, Expression.ne)

        self.assertNotEqual(exp1, exp2)
        self.assertEqual(exp2, exp3)
