from flask import Flask, request 
from flask_restful import Api, Resource

app = Flask(__name__)
# initialize app as an API
api = Api(app)

names = {
  "karan": {
    "name": "karan kumar"
  }
}

# create a resource 
class HelloWorld(Resource):
  def get(self, name):
    return { "details": names[name] }
  def post(self, name): 
    # the body comes in as a form 
    print(request.form)
    return { "method": "Hey there" }

# register it as a resource 
api.add_resource(HelloWorld, "/people/<string:name>")

if __name__ == "__main__":
  app.run(debug=True)


