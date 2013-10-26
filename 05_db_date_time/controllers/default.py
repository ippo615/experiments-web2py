import time

def index():
	form = SQLFORM(db.messages)
	# I've only been able to insert the datetime AFTER
	# validating the form - If I insert the datetime then validate
	# then the datetime is removed
	if form.validate():
		# Add custom field values
		form.vars.datetime = time.asctime()
		# Inser the record manually
		form.vars.id = db.messages.insert(**dict(form.vars))
	rows=db().select(db.messages.ALL)
	return dict(form=form,rows=rows)
