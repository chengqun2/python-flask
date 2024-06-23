from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash

# 定义app
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    password = 'admin'
    password_hash = generate_password_hash(password)
    return password_hash

if __name__ == '__main__':
    # 运行app
    app.run()