from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
# initialize app as an API
api = Api(app)

# create a resource 
class HelloWorld(Resource):
  def get(self, page):
    return { "PAGE": "PAGE IS " + str(page) }
  def post(self): 
    return { "method": "Hey there" }

# register it as a resource 
api.add_resource(HelloWorld, "/home/<int:page>")

if __name__ == "__main__":
  app.run(debug=True)


