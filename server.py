from flask import Flask, jsonify, render_template
from subprocess import call
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = "mysecret"

socket_io = SocketIO(app)

@app.route('/')
def hello_world():
    return "Hello Gaemigo Project Home Page!!"

# @app.route('/chat')
# def chatting():
#     return render_template('chat.html')


@socket_io.on("message")
def request(message):
    print("message : "+ str(message))
    to_client = dict()
    to_client['message'] = message["msg"]
    to_client['fromUid'] = message["name"]
    send(to_client, broadcast=True)



if __name__ == '__main__':
    socket_io.run(app, debug=True, port=3000)
