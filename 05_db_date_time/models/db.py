db=DAL('sqlite://messages.db')
db.define_table('messages',
	Field('author',requires=IS_NOT_EMPTY()),
	Field('body','text',requires=IS_NOT_EMPTY()),
	# datetime will be filled on the server when the form is processed
	Field('datetime')
)

