from flask import Flask, render_template, request

from datetime import datetime
import psycopg2

host = "dpg-cvi0asqn91rc73ajiomg-a.oregon-postgres.render.com"
database = "citasdb_r0ar"
user = "citasusr"
password = "UFLSv6ccCeYHJMMIXjPljHnvKKxKr4XR"
port = 5432

cur = None

try:
    conn = psycopg2.connect(
    host = host,
    database = database,
    user = user,
    password = password,
    port  = port
    )
    print("conexion correcta")
    cur = conn.cursor()
    cur.execute("SELECT 3*8")
    result = cur.fetchone()
    print(result)
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY,
                name VARCHAR(355)  NOT NULL,
                email VARCHAR(355)  NOT NULL,
                password VARCHAR(355)  NOT NULL ) """)
    conn.commit()
    

    cur.execute("INSERT INTO users ( name,email,password) VALUES (%s,%s,%s)",
                 ("mikel1","sasha@gmail.com","1234") )
    cur.execute("INSERT INTO users ( name,email,password) VALUES (%s,%s,%s)",
                 ("roma1","andrei@gmail.com","1234") )

    conn.commit()    

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    print("imprimimos tabla")
    for row in users:
        print(row)

    cur.close()
    conn.close()

except Exception as error:
    print(error)    
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()



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
        return f"Nombre de usuario: {username}, contraseña {password}"       


    return render_template('register.html')
    

if __name__ == '__main__':
    app.run(debug=True)