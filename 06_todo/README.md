To Do List
==========

This example shows how to make a simple "to do" list.

It includes several new concepts including: url redirection, 
database delete operations, and url arguments.

In the default controller we have 2 functions: `index` and `delete`.
`index` is the default function - it shows you the items on your todo
list and lets you submit the form.

`delete` handles the deletion of a record (a todo list item). To delete
the 5th item you need to send a request to `/06_todo/default/delete/5`.
Note the 5 at the end of the url that is considered an argument to the
function. It can be accessed in the controller via `request.args[0]`.
Check the `delete` function in the `default` controller to see how to 
get an element by id from the database, delete it, and redirect the 
user to the index page.

