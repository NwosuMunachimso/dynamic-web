from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
 return "This is my home attached to root URL"

@app.route("/hello")
def hello():
 return "Hello world from python flask web framework"

@app.route("/hello/<string:name>/")
def hello_with_person_name(name):
# The two lines below will work. But the second is more convenient as it
# implicitly identifies whether the variable is a string or number, etc
# return "Hello %s, greetings from Flask Framework!" % name
    return "Hello {}, greetings from Flask Framework!".format(name)


# In the function below, the name passed will be used inside
# a template file called hello.html. We shall see what
# template engine options exist. For now we'll use Jinja2.
# The template file should be inside a folder called
# templates. Notice the call to the function render_template which we have imported.

@app.route("/hello2/<string:name>/")
def hello_with_template(name):
    return render_template('hello.html', person_name=name)

# Let's use a more complex template with inheritance.
# Two templates are involved here - hello-with-layout.html and
# layout.html. hello-with-layout.html inherits layout.html.
# We'll therefore only refer to the former in this python
# function.
@app.route("/hello3/<string:name>/")
def hello_with_layout(name):
    return render_template('hello-extend-layout.html', person_name=name)

if __name__ == "__main__":
    app.run()
