from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

# Data to be JSON serialize
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# The main page
@app.route('/')
def type():
    return 'Type in /todos to get transfered to the url'


#  The first endpoint GET
@app.route('/todos', methods=['GET'])
def set_todos():
    # Converting the above variable into a json string
    json_text = jsonify(todos)
    return json_text


# The second endpoint POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 200
  
   
# The third endpoint DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    
    del todos[position]
    return jsonify(todos), 200



# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)