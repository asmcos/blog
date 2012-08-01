#coding=utf-8
from uliweb import expose
from models import blogs
from forms  import BlogsForm

@expose('/')
def index():
	blog = blogs.all();
	form = BlogsForm();
	if request.method == 'POST':
		flag = form.validate(request.params)
		if flag:
			n = blogs(**form.data);
			n.username = request.user.username
			n.save();
	return {'blog':blog,'form':form}
