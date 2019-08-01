from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/tweet", methods=["GET", "POST"])
def tweet():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        content = request.form["content"]
        return render_template("index.html", content=content)


if __name__ == "__main__":
    app.run(debug=True)
