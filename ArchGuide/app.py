from flask import Flask, render_template
from data import db_session

app = Flask(__name__)
db_session.global_init('database/arch_guide.db')


@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
