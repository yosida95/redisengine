# -*- coding: utf-8 -*-


class Type(object):

    @property
    def python_type(self):
        raise NotImplementedError


class Integer(Type):

    @property
    def python_type(self):
        return int


class String(Type):

    @property
    def python_type(self):
        return str


class Unicode(Type):

    @property
    def python_type(self):
        return unicode


class List(Type):

    @property
    def python_type(self):
        return list
