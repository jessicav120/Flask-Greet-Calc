# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add_nums():
    '''Get sum of a & b query arguments'''

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(operations.add(a, b))

@app.route('/sub')
def subtract_nums():
    '''Get difference of a - b query arguments'''

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(operations.sub(a, b))

@app.route('/mult')
def mult_nums():
    '''Get product of a * b query arguments'''

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(operations.mult(a, b))

@app.route('/div')
def div_nums():
    '''get quotient of a/b query arguments'''

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(operations.div(a, b))

OPERATIONS = {
    'add': operations.add,
    'sub': operations.sub,
    'mult': operations.mult,
    'div': operations.div
}

@app.route('/math/<operation>')
def all_math(operation):
    '''
    Perform math operations on a & b query arguments according to the operation specified in the path.
    operations are defined in the OPERATIONS dictionary and are called through the url.
    '''
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    opp = OPERATIONS.get(operation) #is there a difference in performance between this syntax and OPERATIONS[operation](a,b)?

    return str(opp(a,b))
