from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

color_size = {'r': 255, 'g': 255, 'b': 255, 'area': 10}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control')
def control():
    return render_template('control.html')

@app.route('/pattern')
def pattern():
    return render_template('pattern.html', color_size=color_size)

@socketio.on('update_color_size')
def handle_update_color_size(data):
    global color_size
    color_size = data
    emit('color_size_updated', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
