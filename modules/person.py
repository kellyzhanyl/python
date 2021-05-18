#!/usr/bin/python3
from ctypes import *

class Student(Structure):
    _pack_ = 1
    _fields_ = [
        #(字段名, c类型 )
        ('id', c_uint32),
        ('name', c_int32),
        ('age', c_uint8),
        ('address', c_char),
    ]
    
    def encode(self):
        return string_at(addressof(self), sizeof(self))

    def decode(self, data):
        memmove(addressof(self), data, sizeof(self))
        return len(data)
