from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock `/encrypt` endpoint
@app.route('/encrypt', methods=['GET'])
def encrypt():
    return jsonify({
        "key": "mock_key",
        "encrypted_text": "mock_encrypted_text"
    })

# Mock `/verify` endpoint
@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    if data["decrypted_text"] == "mock_decrypted_message":
        return "Success: Decrypted message is correct!"
    return "Error: Incorrect decrypted message.", 400

if __name__ == "__main__":
    app.run(port=5000)
