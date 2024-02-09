from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')
@app.route('/register',methods=['POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        password=request.form['password']
        email=request.form['email']
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    

