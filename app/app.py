from flask import Flask, jsonify, request

app = Flask(__name__)

payments = [
    {
        "id": 1,
        "customer": "Samuel",
        "amount": 500
    }
]

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/payments")
def get_payments():
    return jsonify(payments)

@app.route("/payments", methods=["POST"])
def create_payment():
    payment = request.json
    payments.append(payment)

    return jsonify({
        "message": "payment created",
        "payment": payment
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)