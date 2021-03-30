from flask import Flask, render_template, request, session, redirect, url_for, g, flash
import model

app = Flask(__name__)
app.secret_key = 'Aloha'


username = ''
user = model.check_users()

# home functions: homepage, login, signup, logout

@app.route('/', methods = ['GET','POST'])
def home():
    if 'username' in session:
        g.user = session ['username']
        all_task = model.get_all()
        return render_template('dashboard.html', tasks = all_task)
    return render_template('homepage.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('username', None)
        are_u_user = request.form['username']
        pwd = model.check_pw(are_u_user)
        if request.form['password'] == pwd:
            session['username'] = request.form['username']
            return redirect(url_for('home'))        
    return render_template('login.html')


@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        message = 'Please sign up'
        return render_template('signup.html')
    else:
        username = request.form['username']
        password = request.form['password']
        token_word = request.form['token_word']
        model.signup(username, password, token_word)
        return redirect(url_for('login'))  


@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home')) 


    # Functions for data base CRUD

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        task = request.form['task']
        day = request.form['day']

        model.add_task(name,task,day)

        flash("The task was added to the list.")

        return redirect(url_for('home'))


@app.route('/update', methods = ['GET','POST'])
def update():
    if request.method == 'POST':
        id_of_task = request.form.get('id')
        person = request.form['name']
        task = request.form['task']
        day = request.form['day']

        model.update_task(id_of_task,person,task,day)
        
        flash("Your Task is updated :)")

        return redirect(url_for('home'))

@app.route('/delete/<id>', methods = ['GET','POST'])
def delete(id):
    model.delete_task(id)
    flash("The task was deleted.")
    return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(port= 7000, debug= True)





