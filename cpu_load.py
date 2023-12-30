from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def cpu_load():
    start_time = time.time()
    while time.time() - start_time < 1:
        pass
    return f'2 {start_time}\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
