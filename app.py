from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This change was pushed from VS Code!'
