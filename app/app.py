from flask import Flask, Response
from flask import render_template, make_response


app = Flask(__name__)


@app.route('/<text>')
def page(text):
    # display simple text to browser.
    return make_response(render_template('index.html', text = text), 200, {'Content-Type': 'text/html'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



