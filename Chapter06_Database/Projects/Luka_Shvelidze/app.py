from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/order')
def info():
    message = "Order N1"
    return render_template('order.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
