from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/sale')
def sale():
    return render_template('sale.html')

@app.route('/support')
def support():
    return render_template('support.html')

if __name__ == '__main__':
    # Listen on all network interfaces and on port 80
    app.run(host='0.0.0.0', port=80)
