#coding=utf-8
from uliweb.orm import *

class blogs (Model):
    username = Field(CHAR);
    title    = Field(TEXT);
    content  = Field(TEXT);
    datetime = Field(datetime.datetime, auto_now_add=True);

