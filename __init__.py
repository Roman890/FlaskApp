from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import time
import datetime
from multiprocessing import Process
from stoptests import deleteCron, createCron, pr


app = Flask(__name__)
app.secret_key = "Secret"


#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tbywqmjtrdcmxi:4d564fdf4081fd021f942e17ac54984385b68f01158271702daa0e562c3a7afd@ec2-3-216-129-140.compute-1.amazonaws.com:5432/db6qdt0bf8oa0r'
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
    value1 = db.Column(db.String(50))
    bot_id = db.Column(db.Integer(), db.ForeignKey('bots.id'))
    logs = db.relationship('Logs', backref='tests')

    def __init__(self, name, value1, bot_id):
        self.name = name
        self.value1 = value1
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
    all_bots = Bots.query.all()
    all_tests = Tests.query.all()
    return render_template("index.html", bots=all_bots, tests=all_tests)


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
        value1 = request.form['value1']
        bot_id = request.form['id']
        my_data = Tests(name, value1, bot_id)
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
    #p1 = Process(target=runTestApp)
    #p1.start()
    #p2 = Process(target=runFlaskApp)
    #p2.start()


