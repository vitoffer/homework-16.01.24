from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '92347_а114!'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    session['fio'] = request.form['fio']
    session['klass'] = request.form.get('klass')
    return redirect('/test')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/answer', methods=['POST'])
def answer():
    num1 = request.form['num1']
    num2 = request.form['num2']
    num3 = request.form['num3']
    if num1 == '16' and num2 == '1' and num3 == '200':
        return redirect('/success')
    else:
        return redirect('/fail')


@app.route('/success')
def success():
    return render_template('success.html', fio=session['fio'], klass=session['klass'])


@app.route('/fail')
def fail():
    return render_template('fail.html', fio=session['fio'], klass=session['klass'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
