from flask import Flask, request, render_template
import threading
from functions import motor_forward, motor_backward, motor_stop, set_angle
from gpio_config import get_components
from self_drive import auto_loop

app = Flask(__name__)
drive_mode = {'mode': 'manual', 'auto_thread': None, 'stop_flag': False}

def should_stop():
    return drive_mode['stop_flag']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cmd")
def cmd():
    if drive_mode['mode'] != 'manual':
        return "Manual control disabled"
    
    action = request.args.get("action")
    if action == "forward":
        motor_forward()
    elif action == "backward":
        motor_backward()
    elif action == "stop":
        motor_stop()
    elif action == "left":
        set_angle(10)
    elif action == "right":
        set_angle(60)
    elif action == "center":
        set_angle(30)
    return f"Command {action} executed."

@app.route("/mode")
def mode():
    new_mode = request.args.get("mode")
    if new_mode == "auto":
        drive_mode['mode'] = 'auto'
        drive_mode['stop_flag'] = False
        if drive_mode['auto_thread'] is None or not drive_mode['auto_thread'].is_alive():
            t = threading.Thread(target=auto_loop, args=(should_stop,))
            t.daemon = True
            drive_mode['auto_thread'] = t
            t.start()
        return "Switched to Auto Mode"
    else:
        drive_mode['mode'] = 'manual'
        drive_mode['stop_flag'] = True
        motor_stop()
        return "Switched to Manual Mode"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
