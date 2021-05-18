#!/usr/bin/python3
from modules.person import * 

def get_buf():
    s=Student()
    s.id=2
    buf=s.encode()
    print(buf)

def get_data():
    s=Student()
    s.id=2
    buf=s.encode()
    s.decode(buf)
    print(s.id)
