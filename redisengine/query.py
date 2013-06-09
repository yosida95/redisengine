# -*- coding: utf-8 -*-

from .schema import Column


class Expression(object):
    eq = 0  # equal
    ne = 1  # not equal
    lt = 2  # less than
    gt = 3  # greater than

    operators = (eq, ne, lt, gt)

    def __init__(self, target, value, operator):
        assert isinstance(target, Column)
        assert operator in self.operators

        self._target = target
        self._value = value
        self._operator = operator

    def __eq__(self, other):
        ret = isinstance(other, self.__class__)
        ret &= self._target == other._target
        ret &= self._value == other._value
        ret &= self._operator == other._operator

        return ret

    def __ne__(self, other):
        ret = not isinstance(other, self.__class__)
        ret |= self._target == other._target
        ret |= self._value == other._value
        ret |= self._operator == other._operator

        return ret


class Query(object):

    def __init__(self, session, target):
        assert isinstance(target, type)
        assert hasattr(target, u'__metadata__')

        self._session = session
        self._target = target
        self._expressions = []

    def __call__(self, *expressions):
        for expression in expressions:
            if expression in self._expressions:
                continue

            if isinstance(expression, Expression) is False:
                raise ValueError(u'Argument must be instance'
                                 + u' of redisengine.query.Expression')

            if expression._target.table is self._target:
                raise ValueError(u'Argument must be specified'
                                 + u' as expression of target of query')

            self._expressions.append(expression)

        return self
