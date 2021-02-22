from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/welcome/<name>')
def welcome(name):
    return 'Welcome %s!' % name


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('dashboard', name=name))
    else:
        name = request.args.get('name')
        return render_template('welcome.html')


if __name__ == '__main__':
    app.run(debug=True)
