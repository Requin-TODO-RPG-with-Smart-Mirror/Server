import socketio

sio = socketio.Client()

@sio.on('get_todo')
def todo(data):
    print(data)

print('RUN!')
sio.connect('http://127.0.0.1:5556')
