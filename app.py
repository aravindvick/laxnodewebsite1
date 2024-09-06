from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
