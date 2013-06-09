# -*- coding: utf-8 -*-

import inspect

from .types import Type


class Table(object):

    def __init__(self, name, *columns):
        self.name = name
        self.columns = columns

    def __new__(cls, *args, **kwargs):
        self = super(Table, cls).__new__(cls)

        if len(args) < 2:
            for column in kwargs.get(u'columns', []):
                column.set_table(self)
        elif len(kwargs) is 0:
            for column in args[1:]:
                column.set_table(self)
        else:
            raise TypeError()

        return self


class Column(object):

    def __init__(self, *args, **kwargs):
        args = list(args)

        self.table = None
        try:
            if isinstance(args[0], basestring):
                self.name = args.pop(0)
            else:
                self.name = None

            if inspect.isclass(args[0]) and issubclass(args[0], Type)\
                    or inspect.isclass(type(args[0]))\
                    and issubclass(type(args[0]), Type):
                self.type_ = args.pop(0)
            else:
                self.type_ = None
        except IndexError:
            raise TypeError
        else:
            if len(args) > 0:
                raise TypeError()

        self.primary_key = kwargs.get(u'primary_key', False)
        self.nullable = kwargs.get(u'nullable', True)
        self.auto_increment = kwargs.get(u'auto_increment', False)

    def set_table(self, table):
        assert isinstance(table, Table)
        if self.table:
            raise TypeError(u'table has already set')

        self.table = table

    def set_name(self, name):
        assert isinstance(name, basestring)
        if self.name:
            raise TypeError(u'name has already set')

        self.name = name
