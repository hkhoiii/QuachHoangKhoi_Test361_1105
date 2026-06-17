from flask import Flask, request, jsonify
from ecc import ECCCipher
app = Flask(__name__)
####### ECC #########

ecc_cipher = ECCCipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'ECC Keys generated successfully'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    keys = ecc_cipher.load_keys()
    private_key = keys["private_key"]
    signature = ecc_cipher.sign(message,private_key)
    signature_hex = signature.hex()

    return jsonify({'signature': signature_hex})


@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    keys = ecc_cipher.load_keys()
    public_key = keys["public_key"]
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message,signature,public_key)
    return jsonify({'is_verified': is_verified})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
