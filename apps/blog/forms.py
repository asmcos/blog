#coding=utf-8
from uliweb.form import *

class BlogsForm(Form):
#    username = StringField(label="用户名", required=True);
    title    = StringField(label="标题", required=True);
    content  = TextField(label="内容", required=True,rows=10,cols=60);
