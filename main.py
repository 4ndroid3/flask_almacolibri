from flask import Flask, make_response, request, redirect, render_template

from app import create_app

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response(redirect('/colibri'))

    return response


@app.route('/colibri', methods=['GET', 'POST'])
def colibri():
    frstmsj = 'tangalanga'
    context = {
        'frstmsj': frstmsj
    }

    return render_template('colibri.html', **context)
