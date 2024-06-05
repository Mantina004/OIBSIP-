from flask import Flask, flash, render_template, request, session, redirect, url_for
import managedb


app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/home')
def home():
    return render_template('home.html', username = session['username'])

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/NewUser')
def addNewUser():
    return render_template("registration.html")

@app.route('/')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''    
    if request.method == 'POST':
        user=request.form['username']
        pwd=request.form['password']
        result = managedb.dbSelect('*', 'users', f"username = '{user}' AND password = '{pwd}'")
        print(result)        
        if result:
            session['loggedin'] = True
            session['username'] = result[0][1]
            return redirect(url_for('home'))
        else:
            print('no record found')
            msg = 'Incorrect username or password. Try again!'
            flash(msg)
    return render_template('index.html')



@app.route('/registration', methods=['GET', 'POST'])
def registration():
    msg = ''    
    if request.method == 'POST':
        user=request.form['username']
        pwd=request.form['password']
        email= request.form['email']
        if user_Exists(user):
            msg = "Username already exists. Try Again!"
            flash(msg)
            return render_template('registration.html')
        else:
            if managedb.dbAdd('users', 'username, password, email', '%s, %s, %s', (user,pwd,email)):                
                msg = "Registration Successful. Log In"
                flash(msg)
                return redirect(url_for('index'))
        

def user_Exists(username):  
    results = managedb.dbSelect('*', 'users', f"username = '{username}'")
    if len(results) ==0:
        return False  
    else:
        return True


if __name__ == "__main__":
    app.run()
