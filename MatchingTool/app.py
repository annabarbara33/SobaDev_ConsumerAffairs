from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def __repr__(self):
        return '<Task %r>' % self.id


mylist = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Q1')
def get_Q1():
    return render_template('Q1.html', )


@app.route('/Q2')
def get_Q2():
    return render_template('Q2.html', )


@app.route('/Q3')
def get_Q3():
    return render_template('Q3.html', )


@app.route('/Q4')
def get_Q4():
    return render_template('Q4.html', )


@app.route('/R1')
def get_Qr():
    return render_template('R1.html', )


if __name__ == "__main__":
    app.run(debug=True)
