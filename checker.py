from flask import Flask, render_remplate

app = Flask(__name__)

@app.rout('/')
def index():
    return render_remplate("index.html")


if __name__ == "__main__":
    app.run(debug=True)