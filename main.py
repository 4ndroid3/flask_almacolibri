from flask import make_response, request, redirect, render_template
from app import create_app

app = create_app()


@app.route('/')
def index():
    response = make_response(redirect('/colibri'))

    return response

@app.route('/colibri', methods=['GET', 'POST'])
def colibri():
    username = 'andrés'
    context = {
        'username': username
    }

    return render_template('colibri.html', **context)
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/products', methods=['GET', 'POST'])
def products():
    products = ['Manies', 'Nuez', 'Mix Semillas', 'Pimentón', 'Sal del Himalaya', 'Coco Rallado']
    context = {
        'products': products
    }

    return render_template('products.html', **context)
