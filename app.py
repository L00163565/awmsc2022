from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'sql4.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql4480309'
app.config['MYSQL_PASSWORD'] = 'ywtgHyDEsc'
app.config['MYSQL_DB'] = 'sql4480309'
app.config['MYSQL_PORT'] = 3306

# route to home page when / is present in url
@app.route('/')
def index():
    return render_template('home.html')

# route to home page when url points to "/home"
@app.route('/home.html')
def load_home_page():
    return render_template('home.html')

# route to login_signup page when url points to "/home"
@app.route('/login_signup')
def load_login_page():
    return render_template('login_signup.html')

# route to check whether login or signup to render depending on method call
@app.route('/login_signup_check', methods = ['GET','POST'])
def login_signup():
    if request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')
        cursor = mysql.connection.cursor()
        print('email',email, 'password', password)
        cursor.execute('''select * from customer_details where email=%s and password=%s''',(email,password))
        result = cursor.fetchone()
        print('result',result)
        if None != result and email == result[1] and password == result[2]:
            mysql.connection.commit()
            cursor.close()
            return render_template('profile.html')
        else: 
            mysql.connection.commit()
            cursor.close()
            return '<h1>not matched</h1>'

    if request.method == 'POST':
        fullname = request.form.get('su-name')
        email = request.form.get('su-mail')
        password = request.form.get('su-pass')  
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO customer_details (fullname, email, password) VALUES (%s,%s,%s)''',(fullname, email, password))
        mysql.connection.commit()
        cursor.close()
        return render_template('login_signup.html', confirm_message='registration successful')   # pop up for registration

# route to bookings page 
@app.route('/bookings.html')
def load_bookings_page():
    return render_template('bookings.html')

# route to profile page
@app.route('/profile.html')
def load_profile_page():
    return render_template('profile.html')

# route to payment page
@app.route('/payment.html')
def load_payment_page():
    return render_template('payment.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
