from flask import Flask, jsonify, render_template
from subprocess import call
from flask_socketio import SocketIO, send, join_room
# from flask_socketio import join_room, leave_room

app = Flask(__name__)
app.secret_key = "mysecret"

socket_io = SocketIO(app)

clients = []

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
    room = message["name"]

    join_room(room);
    send(to_client, room=room)
    # send(to_client, room=message["name"])



if __name__ == '__main__':
    socket_io.run(app, debug=True, port=3000)
