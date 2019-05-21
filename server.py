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
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('127.0.0.1', 8081))
    print('연결 확인 됐습니다.')
    clientSock.send(str(message["msg"]).encode('utf-8'))
    print('메시지를 전송했습니다.')
    data = clientSock.recv(1024)
    print('받은 데이터 : ', data.decode('utf-8'))
    to_client['message'] = data.decode('utf-8')
    to_client['fromUid'] = 'poki'
    room = message["name"]
    join_room(room);
    send(to_client, room=room)



if __name__ == '__main__':
    socket_io.run(app, host='0.0.0.0', debug=True, port=3000)
