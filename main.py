from flask import Flask, render_template
import requests
from post import Post

response = requests.get("https://api.npoint.io/4af156202f984d3464c3")
data = response.json()
print(data)
all_posts = [Post(data[i]["id"], data[i]["title"], data[i]["subtitle"], data[i]["body"]) for i in range(len(data))]

app = Flask(__name__)

@app.route('/')
@app.route('/blog')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:pid>')
def view_post(pid):
    return render_template("post.html", posts=all_posts, pid=pid)


if __name__ == "__main__":
    app.run(debug=True)
