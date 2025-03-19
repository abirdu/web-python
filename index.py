from flask import Flask, render_template, request

from datetime import datetime

app = Flask(__name__)
   

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register' , methods = ['GET','POST'])
def register():
    print(request)
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password'] 
        return f"Nombre de usuario: {username}, contraseñe {password}"       


    return render_template('register.html')
    

if __name__ == '__main__':
    app.run(debug=True)