from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)


users = [               #list with dictionary embedded
    {
    'username':'driesvw@email.com',
    'password': '123'
    },
    {
    'username':'annelies@email.com',
    'password': '123'
    }
    ]

@app.route('/')
def start():
    return "Waiting for login request"

@app.route('/login', methods=['POST','GET'])
def login():

    if request.method == 'POST':
        uservar = request.form['username']
        passwordvar = request.form['password']

        logattempt = [{'password':passwordvar, 'username':uservar}]

        if list(filter(lambda user: user['username'] == uservar, users)) == logattempt:          #(authentication)
            return redirect('http://127.0.0.1:5000/'+ uservar)
                                                                                              
        else:
            return render_template('wrongcred.html')

    else:
        return render_template('index.html')




@app.route('/register')           #not finished yet
def register():

    if request.method == 'POST':
        uservar = request.form['username']
        passwordvar = request.form['password']

        return render_template('index.html', uservar=uservar, passwordvar=passwordvar)


    else:
        return render_template('register.html')




if __name__ == '__main__':
    app.run(debug=True, port=5003)