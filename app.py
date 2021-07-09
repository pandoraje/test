from flask import Flask
application = Flask(__name__)

@application.route("/")
def main():
	return "Hello!"

@application.route('/how are you')
def hello():
	return 'I am good, how about you?'

if __name__ == "__main__":
	application.run()
