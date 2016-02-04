from flask import Flask
from flask import render_template

app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<name>")
def hello_someone(name):
	return render_template("hello.html", name=name.title())

@app.route("/bye/<heather>")
def bye_someone(heather):
	return render_template("goodbye.html", heather=heather.title())

first_integer = 5
second_integer = 6

first_integer_string = str(first_integer)
second_integer_string = str(second_integer)

@app.route('/<first_integer_string>/minus/<second_integer_string>')
def show_maths():
	return "%d - %d" % (first_integer, second_integer)

app.run()