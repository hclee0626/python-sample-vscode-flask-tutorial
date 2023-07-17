"""
from https://code.visualstudio.com/docs/python/tutorial-flask 
make sure you are running this in your virtual environment 
do (from Command Pallete): Terminal: Create New Terminal -> activates virtual environment
can also run from terminal: source .venv/bin/activate
"""

"""
In app.py, add code to import Flask and create an instance of the Flask object. 
If you type the code below (instead of using copy-paste), 
you can observe VS Code's IntelliSense and auto-completions:
"""

from flask import Flask
app = Flask(__name__)

# add a function that returns content 
# use Flask's app.route decorator to create a route for the function
@app.route("/")
def home():
    return "Hello, Flask!"

# run the app by entering "python -m flask run" in the terminal
# however actually just enter: "flask run"

# to open the default browser to the rendered page, Command+click the URL in the terminal
# when you visit a URL like /, message appears in the terminal showing the HTTP request 
# "127.0.0.1 - - [17/Jul/2023 13:41:03] "GET / HTTP/1.1" 200 -"

"""
Tip: When using a different filename than app.py, such as webapp.py, 
you will need to DEFINE an environment variable named FLASK_APP and 
set its value to your chosen file. Flask's development server then uses 
the value of FLASK_APP instead of the default file app.py. 
For more information, see Flask command line interface.
"""

