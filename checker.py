from flask import Flask, render_template

app = Flask(__name__)

# Render an 8x8 balck and red checkboard
@app.route('/')
def index():
    return render_template("8x8.html")

# Render an 8x4 black and red checkboard
@app.route('/4')
def by_four_board():
    return render_template("8x4.html")

@app.route('/<int:x>/<int:y>')
def x_by_y_board(x, y):
    return render_template("xbyY.html", x=x, y=y)

if __name__ == "__main__":
    app.run(debug=True)