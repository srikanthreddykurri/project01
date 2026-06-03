from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Hello Srikanth!</h1>
    <h2>let us deploy this app in the kubernetes</h2>
    <p>Pod Hostname: {socket.gethostname()}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
