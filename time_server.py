from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_time():    
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time

if __name__ == '__main__':
    app.run(debug=True)
