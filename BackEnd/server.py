from flask import (
    Flask,
    request,
    abort
)

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello\n"

@app.route("/login", methods = ["POST"])
def login():
    username = request.json=["username"]
    user_taken = username in users
    if user_taken:
        abort(403)
    else:
        user.append(username)
        return 'Successfully logged in'    

    pass

if __name__ == '__main__':
    app.run(debug=True)
