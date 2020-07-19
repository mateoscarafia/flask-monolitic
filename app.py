from products import products
from flask import Flask, jsonify, request, render_template, redirect

app = Flask(__name__)


# Template Route----------------------------------
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        req = request.form
        print(req)
        return redirect(request.url)
    return render_template('header.html')


@app.route('/sendme', methods=['POST'])
def sendme():
    req = request.get_json()
    print(req)
    return 'YESSSS'
# -------------------------------------------------


# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
