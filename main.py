from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
# initialize app as an API
api = Api(app)

# create a resource 
class HelloWorld(Resource):
  def get(self):
    return { "data": "Hello World" }

# register it as a resource 
api.add_resource(HelloWorld, "/home")

if __name__ == "__main__":
  app.run(debug=True)


