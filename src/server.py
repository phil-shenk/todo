import philtasks as pt
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, world!'

@app.route('/list_tasks')
def get_tasks():
    result = pt.tasksToString('tasks')
    print(result)
    return result
app.run(host='150.212.200.217')

