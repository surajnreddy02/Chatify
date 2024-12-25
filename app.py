import eventlet
eventlet.monkey_patch()

from flask import Flask, request, render_template, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, send

from utils import generate_room_code

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SDKFJSDFOWEIOF'
socketio = SocketIO(app)

rooms = {}


@app.route('/', methods=["GET", "POST"])
def home():
    session.clear()

    if request.method == "POST":
        name = request.form.get('name')
        action = request.form.get('action')
        code = request.form.get('code')

        if not name:
            return render_template('home.html', error="Name is required", code=code)

        if action == "create":
            room_code = generate_room_code(6, list(rooms.keys()))
            rooms[room_code] = {'members': 0, 'messages': [], 'users': []}
        elif action == "join":
            if not code:
                return render_template('home.html', error="Please enter a room code to join", name=name)
            if code not in rooms:
                return render_template('home.html', error="Room code is invalid", name=name)
            if name in rooms[code]['users']:
                return render_template('home.html', error="Name already taken in this room", name=name, code=code)

            room_code = code
        else:
            return render_template('home.html', error="Please select an action (Create or Join)", name=name)

        session['room'] = room_code
        session['name'] = name
        return redirect(url_for('room'))

    return render_template('home.html')


@app.route('/room')
def room():
    room_code = session.get('room')
    name = session.get('name')

    if name is None or room_code is None or room_code not in rooms:
        return redirect(url_for('home'))

    messages = rooms[room_code]['messages']
    users = rooms[room_code].get('users', [])
    return render_template('room.html', room=room_code, user=name, messages=messages, users=users)


@socketio.on('connect')
def handle_connect():
    name = session.get('name')
    room = session.get('room')

    if name is None or room is None:
        return

    if room not in rooms:
        rooms[room] = {'members': 0, 'messages': [], 'users': []}

    join_room(room)
    rooms[room]['members'] += 1
    rooms[room]['users'].append(name)

    send({
        "sender": "",
        "message": f"{name} has entered the chat"
    }, to=room)

    send({
        "sender": "",
        "message": f"Users in the room: {', '.join(rooms[room]['users'])}"
    }, to=room)


@socketio.on('message')
def handle_message(payload):
    room = session.get('room')
    name = session.get('name')

    if room not in rooms:
        return

    message = {
        "sender": name,
        "message": payload["message"]
    }
    send(message, to=room)
    rooms[room]["messages"].append(message)


@socketio.on('disconnect')
def handle_disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        rooms[room]['users'].remove(name)
        if rooms[room]["members"] <= 0:
            del rooms[room]

    send({
        "message": f"{name} has left the chat",
        "sender": ""
    }, to=room)


if __name__ == '__main__':
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)
