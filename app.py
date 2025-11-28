from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    r.incr('visits')
    count = r.get('visits').decode('utf-8')
    return f"<h1>Welcome!</h1><p>You are visitor number: {count}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)