<<<<<<< HEAD

from flask import Flask, render_template
=======
from flask import Flask, render_template, jsonify
>>>>>>> 6942e60e347183e871c9ba60d03dd780e1f6bc54

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
if __name__ == '__main__':
    app.run(debug=True)
=======
@app.route('/software-solutions')
def software_solutions():
    return render_template('software_solutions.html')

@app.route('/mechanical-engineering')
def mechanical_engineering():
    return render_template('mechanical_engineering.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5004)
>>>>>>> 6942e60e347183e871c9ba60d03dd780e1f6bc54
