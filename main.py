from flask import make_response, request, redirect, render_template

from app import create_app

app = create_app()


@app.route('/')
def index():
    response = make_response(redirect('/colibri'))

    return response


@app.route('/colibri', methods=['GET', 'POST'])
def colibri():
    frstmsj = 'Alma de Colibri'
    username = 'andrés'
    products = ['Manies', 'Nuez', 'Mix Semillas', 'Pimentón', 'Sal del Himalaya', 'Coco Rallado']
    context = {
        'frstmsj': frstmsj,
        'username': username,
        'products': products
    }

    return render_template('colibri.html', **context)
