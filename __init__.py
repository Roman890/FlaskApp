from flask import Flask,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, asc
import datetime
import helpers
from stoptests import deleteCron, createCron
from multiprocessing import Process
import time

app = Flask(__name__)
#app.secret_key = "Secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/testbots'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Bots(db.Model):
    __tablename__ = 'bots'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(200))
    tests = db.relationship('Tests', backref='bots')

    def __init__(self, name, image):
        self.name = name
        self.image = image

class Tests(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    bot_id = db.Column(db.Integer(), db.ForeignKey('bots.id'))
    logs = db.relationship('Logs', backref='tests')

    def __init__(self, id, name, bot_id):
        self.id = id
        self.name = name
        self.bot_id = bot_id
        
class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(100))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    test_id = db.Column(db.Integer(), db.ForeignKey('tests.id'))

    def __init__(self, text, test_id):
        self.text = text
        self.test_id = test_id


@app.route('/', methods=['GET'])
def main():
    bots = Bots.query.all()
    data = helpers.find_logs_from_bots() 
    return render_template("index.html", bots=bots, data=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        image = request.form['image']
        my_data = Bots(name, image)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('main'))


@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Bots.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        db.session.commit()
        return redirect(url_for('main'))


@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Bots.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    return redirect(url_for('main'))


@app.route('/insertTest', methods = ['POST'])
def insert_test():
    if request.method == 'POST':
        name = request.form['name']
        id = int(request.form['value1'])
        bot_id = request.form['id']
        my_data = Tests(id, name, bot_id)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('tests', id=bot_id))


@app.route('/tests/<id>', methods = ['GET'])
def tests(id):
    all_tests = Tests.query.filter(Tests.bot_id == id)
    my_data = Bots.query.get(id)
    return render_template("tests.html", tests=all_tests, bot=my_data)


@app.route('/back', methods = ['GET'])
def back():
    return redirect(url_for('main'))


@app.route('/logs/<id>', methods = ['GET'])
def logs(id):
    all_logs = Logs.query.filter(Logs.test_id == int(id))
    return render_template('logs.html', logs=all_logs)


@app.route('/logs_for_index/<id>', methods = ['GET'])
def logs_for_index(id):
    all_logs = Logs.query.filter(Logs.test_id == int(id)).order_by(desc(Logs.id)).limit(3).all()[::-1]
    return render_template('logs.html', logs=all_logs)


# stop and run tests
@app.route('/starttests/<id>', methods = ['GET'])
def starttests(id):
    all_tests = Tests.query.filter(Tests.bot_id == id)
    my_data = Bots.query.get(id)
    #createCron()
    return render_template("tests.html", tests=all_tests, bot=my_data)

@app.route('/stoptests/<id>', methods = ['GET'])
def stoptests(id):
    all_tests = Tests.query.filter(Tests.bot_id == id)
    my_data = Bots.query.get(id)
    #deleteCron()
    return render_template("tests.html", tests=all_tests, bot=my_data)


if __name__ == "__main__":
    db.create_all()
    app.run(threaded=True)