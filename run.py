from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'dfdfdf'


@app.route('/')
def index():
    if 'color' in session:
        color = session['color']
    else:
        color = "#FFF"

    if 'text_color' in session:
        text_color = session['text_color']
    else:
        text_color = "#000"

    return render_template('index.html', color=color, text_color=text_color)


@app.route('/red')
def red():
    session['color'] = '#F00'
    return redirect('/')


@app.route('/redtext')
def redtext():
    session['text_color'] = '#F00'
    return redirect('/')

@app.route('/bluetext')
def bluetext():
    session['text_color'] = '#00F'
    return redirect('/')

@app.route('/greentext')
def greentext():
    session['text_color'] = '#0F0'
    return redirect('/')

@app.route('/blacktext')
def blacktext():
    session['text_color'] = '#000'
    return redirect('/')

@app.route('/blue')
def blue():
    session['color'] = '#00F'
    return redirect('/')


@app.route('/green')
def green():
    session['color'] = '#0F0'
    return redirect('/')


@app.route('/default')
def default():
    del session['color']
    return redirect('/')


app.run(debug=True)
