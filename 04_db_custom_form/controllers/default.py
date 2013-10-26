def index():
	form = SQLFORM(db.messages)
	if form.process().accepted:
		# The form was accepted/process successfully
		pass
	elif form.errors:
		# The form does not pass validation
		pass
	else:
		# The form has not be filled in
		pass
	rows=db().select(db.messages.ALL)
	return dict(form=form,rows=rows)
