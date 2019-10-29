import flask
import os


app = flask.Flask(__name__)


@app.route("/sensor")
def sensor():
    return flask.render_template("sensor.html")

@app.route("/rover")
def rover():
    return flask.render_template("rover.html")

@app.route("/video")
def video():
    return flask.render_template("video.html")

@app.route("/science")
def science():
    return flask.render_template("science.html")

@app.route("/")
def main_page():
	return flask.render_template("main_page.html")

if __name__ == "__main__":
    app.run(host = 'localhost')
    app.run()
