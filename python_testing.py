import json
from flask import Flask, make_response, request
from flask_wtf import CSRFProtect
from django.http import HttpResponseRedirect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

def update_and_show_counter(counter):
    counter =+ 8
    print(counter)

counter = 10
update_and_show_counter(counter)

def complicated_code(input):
    a=1
    b=2
    c=3
    d=4

    if a in (a,b,c,d):
        input += c
        if a < b:
            input += b
            if c < d:
                input += d
                if a < c:
                    input += a
                    if a < d:
                        input += d
                        if c < d:
                            input += d
                            if a < b:
                                input += a

    return input

@app.route('/xss2')
def index2():
    
    return make_response(complicated_code(request.args.get("input")))

@app.route("/")
def example():
    operation = request.args.get("operation")
    eval(f"product_{operation}()") # Noncompliant
    return "OK"