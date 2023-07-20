from flask import Flask
app = Flask(__name__)
  
# @app.route('/green')
# def hello():
#   return "welcome to the green deployment"

@app.route('/blue')
def my_blue():
   return "welcome to the blue deployment"
  
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)
