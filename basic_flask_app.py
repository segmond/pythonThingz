from flask import Flask

# http://blog.miguelgrinberg.com/post/restful-authentication-with-flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

if __name__ == '__main__':
    app.run(debug=True)
