from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/greet', methods=['POST'])
def greet():
    #write data to file or to DB
    inputName =""
    return render_template("home.html",myName=inputName)
@app.route('/')
def home():
    
    return render_template("home.html",myName="")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/Maverick/')
def Maverick():
    return render_template("Jones.html")


if __name__=="__main__":
    app.run(debug=True)
