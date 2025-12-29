from flask import Flask, render_template #importing Flask class and render function

app = Flask(__name__) #creating object of Flask class

@app.route('/') #creating route for home page
def home():
    return render_template('home.html') #returning html to render on home page 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) #starting the server in debug mode