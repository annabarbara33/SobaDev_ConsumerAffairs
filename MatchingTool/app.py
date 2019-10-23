from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Q1')
def get_Q1():
    return render_template('Q1.html', )
@app.route('/Q2')
def get_Q2():
    return render_template('Q2.html', )

@app.route('/result')
def get_result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
