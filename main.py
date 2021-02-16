from flask import Flask 
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
# initialize app as an API
api = Api(app)

names = {
  "karan": {
    "name": "karan kumar"
  }
}

ages = [ 25, 26]

# body validation
name_post_args = reqparse.RequestParser()
name_post_args.add_argument("age", type=int, help="Need to send age", required=True)


def abort_if_age_not_exist(age): 
  if age not in ages:
    abort(404, message="Age is not valid")


# create a resource 
class HelloWorld(Resource):
  def get(self, name):
    return { "details": names[name] }, 202
  def post(self, name): 
    args = name_post_args.parse_args()
    abort_if_age_not_exist(args.age)
    return { "User Age": "VALID" }

# register it as a resource 
api.add_resource(HelloWorld, "/people/<string:name>")

if __name__ == "__main__":
  app.run(debug=True)
