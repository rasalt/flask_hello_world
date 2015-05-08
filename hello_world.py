from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def say_hi():
  return "Hello World"
  
import functools
def twist(function):
  @functools.wraps(function)
  def wrapper(*args, **kwargs):
    print "This is crazy"
#    function()
  return wrapper  

def twister(twister):
  def decorator(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
      print twister
      function()
    return wrapper  
  return decorator 


@twister("She sells sea shells on the sea shore")
def yellow():
  print "This is yellow"

@app.route("/hello/<name>")
def hi_person(name):
#return "Hello {}!".format(name.title())
  html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
  return html.format(name.title())
#if __name__ == "__main__":
#  yellow()
@app.route("/jedi/<fname>/<lname>")
def hi_jedi_person(fname, lname):
#return "Hello {}!".format(name.title())
  jname = lname[0:3] + fname[0:2]
  html = """
        <h1>
            Hello {}!
        </h1>     
    """
  return html.format(jname.title())
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)