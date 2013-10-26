def index():
	form=crud.create(db.messages)
	#form = SQLFORM(db.person)
	rows=db().select(db.messages.ALL)
	return dict(form=form,rows=rows)
