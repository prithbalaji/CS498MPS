from flask import Flask
import socket
import subprocess
#flask
app = Flask(__name__)
#get,post
@app.route("/", methods=["GET"])
def get_seed():
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)

    return f"{private_ip}", 200

@app.route("/", methods=["POST"])
def post_seed():
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
