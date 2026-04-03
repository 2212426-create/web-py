from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/music"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# đảm bảo folder tồn tại
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_songs():
    files = os.listdir(UPLOAD_FOLDER)
    return files

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
        return redirect(url_for("index"))

    songs = get_songs()
    return render_template("index.html", songs=songs)

if __name__ == "__main__":
    app.run(debug=True)