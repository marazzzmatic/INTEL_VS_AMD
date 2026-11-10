from flask import Flask

app = Flask(__name__)
db_session.global_init('db/arch_guide.db')


@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():
    return None # временно пока нет html


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
