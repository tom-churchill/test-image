from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/')
def cpu_load():
    start_time = time.time()
    count = int(request.args.get('count', 10))
    for i in range(count):
        pass
    return f'3 {time.time() - start_time}\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
