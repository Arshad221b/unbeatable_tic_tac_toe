import  re
from    flask           import Flask, render_template, request, redirect
from    flask.helpers   import url_for
from numpy.core.numeric import outer


app = Flask(__name__, template_folder='templates')


@app.route('/')
def processed_data():
    return render_template('tic_tac_toe.html')


if __name__=='__main__':
    app.run(debug=True)