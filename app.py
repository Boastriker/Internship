from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def repr(self):
        return '<Login %r>' % self.id


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/indexNoButton.html')
def home2():
    return render_template('indexNoButton.html')


@app.route('/register.html', methods=['POST', 'GET'])
def register():
    if(request.method =='POST'):
        user_username = request.form['Username']
        print(user_username)
        user_password = request.form['password']
        print(user_password)
        new_login = Login(username = user_username, password = user_password)
        try:
            db.session.add(new_login)
            db.session.commit()
            return redirect('/indexNoButton.html')
        except:
            return 'There was an error'
    else:
        return render_template('register.html') 


@app.route('/login.html', methods=['GET'])
def login():
    if('username' in request.args):
        user_username = request.args.get('username')
        user_password = request.args.get('pass')
        print(user_username)
        try:
            x = Login.query.filter_by(username=user_username).all()
            print(x)
            return redirect('/indexNoButton.html')
        except:
            return 'There was an error'
    else:
        return render_template('login.html')
@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == "__main__":
    app.run(debug=True)