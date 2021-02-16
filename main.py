from flask import Flask 
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
# initialize app as an API
api = Api(app)

names = {
  "karan": {
    "name": "karan kumar"
  }
}

name_post_args = reqparse.RequestParser()
# body validation
name_post_args.add_argument("age", type=int, help="Need to send age")

# create a resource 
class HelloWorld(Resource):
  def get(self, name):
    return { "details": names[name] }
  def post(self, name): 
    args = name_post_args.parse_args()
    return { "you sent": args.age }

# register it as a resource 
api.add_resource(HelloWorld, "/people/<string:name>")

if __name__ == "__main__":
  app.run(debug=True)


