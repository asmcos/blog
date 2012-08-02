#coding=utf-8
from uliweb import expose
from models import blogs
from forms  import BlogsForm
from uliweb import function
require_login = function('require_login')
from uliweb.contrib.auth.views import login


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

@expose('/delete/<id>')
def delete(id):
	if require_login():
		return redirect(url_for(login))
	n = blogs.get(blogs.c.id == id)
	if n:
		n.delete()
	return redirect('/');

@expose('/edit/<id>')
def edit(id):
	if require_login():
		return redirect(url_for(login))
	if request.method == 'GET':
		p = blogs.get(blogs.c.id==id)
		form = BlogsForm(data={'title':p.title,'content':p.content})
		return {'form':form}
	elif request.method == 'POST':
		form = BlogsForm()
            	flag = form.validate(request.params)
		n = blogs.get(blogs.c.id == id)
		if n:
			n.username = request.user.username
			n.title    = form.data.title
			n.content  = form.data.content
			n.save()
		return redirect('/');
