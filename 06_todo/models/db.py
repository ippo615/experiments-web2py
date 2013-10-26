db=DAL('sqlite://todo.db')
db.define_table('todo',
	Field('task',requires=IS_NOT_EMPTY())
)

