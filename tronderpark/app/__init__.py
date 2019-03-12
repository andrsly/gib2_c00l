from flask import Flask

app = Flask(__name__)

from app import routes

if __name__ == "__main__":
   app.run(port=80,debug=True)
   #app.set( 'port', ( process.env.PORT=5000 ))
   #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)