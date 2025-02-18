from flask import Flask
import subprocess
import os
import datetime

app = Flask(__name__)

@app.route('/htop')
def htop_output():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME")

    # Get system time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    ist_time_str = ist_time.strftime('%Y-%m-%d %H:%M:%S.%f')

    # Run the `top` command and capture its output
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, universal_newlines=True)
    except subprocess.CalledProcessError:
        top_output = "Error: Unable to fetch top output"

    # HTML output format
    response_html = f"""
    <html>
    <head><title>HTOP Output</title></head>
    <body>
        <h1>Name: Your Full Name</h1>
        <h2>Username: {username}</h2>
        <h3>Server Time (IST): {ist_time_str}</h3>
        <h4>TOP output:</h4>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
