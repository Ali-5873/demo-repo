from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Flask Redis GitOps API"
    })


@app.route("/health")
def health():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, socket_connect_timeout=2)
        r.ping()

        return jsonify({
            "status": "ok",
            "redis": "connected"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "redis": "disconnected",
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)