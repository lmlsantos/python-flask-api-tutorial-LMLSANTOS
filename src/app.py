from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

# data to be stored (todo list)
todos = [
    {"label": "My first task", "done": False},
    {"label":"My second task", "done": False},
    {"label":"My third task", "done": False}
]

#creating the first endpoint"
@app.route('/todos', methods=['GET'])
def hello_world():
    #converting the variable todos into a json string, and return it to the frontend 
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
   request_body = request.data
   print("Incoming request with the following body", request_body)
   return 'Response for the POST todo'






# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)