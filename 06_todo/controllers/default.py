
def delete():
	db(db.todo.id==request.args[0]).delete()
	redirect(URL('index'))

def index():
	form = SQLFORM(db.todo)
	if form.validate():
		form.vars.id = db.todo.insert(**dict(form.vars))
	rows=db().select(db.todo.ALL)
	return dict(form=form,rows=rows)

