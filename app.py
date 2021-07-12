from flask import Flask
application = Flask(__name__)

@application.route("/")
def main():
	return "Hello!"

if __name__ == "__main__":
	application.run(host="0.0.0.0", port=8080)
