import requests

# API Base URL (Change this to the real URL if not using the mock API)
BASE_URL = "http://127.0.0.1:5000"

def get_encrypted_data():
    # Call the `/encrypt` API endpoint
    response = requests.get(f"{BASE_URL}/encrypt")
    if response.status_code == 200:
        return response.json()
    raise Exception("Failed to fetch encrypted data")

def verify_decrypted_message(decrypted_text):
    # Prepare the payload for the `/verify` endpoint
    verify_payload = {
        "decrypted_text": decrypted_text,
        "email": "user@example.com",
        "phone_number": "1234567890",
        "name": "User Name",
        "user_submitted_code": "Example code used for decryption"
    }
    # Call the `/verify` API endpoint
    response = requests.post(f"{BASE_URL}/verify", json=verify_payload)
    return response.text

def decrypt_message(encrypted_text, key):
    # Replace this with actual decryption logic
    if encrypted_text == "mock_encrypted_text" and key == "mock_key":
        return "mock_decrypted_message"
    return "failed_to_decrypt"

def main():
    # Step 1: Get Encrypted Data
    data = get_encrypted_data()
    key = data["key"]
    encrypted_text = data["encrypted_text"]

    # Step 2: Decrypt the Message
    decrypted_text = decrypt_message(encrypted_text, key)
    print(f"Decrypted Message: {decrypted_text}")

    # Step 3: Verify Decrypted Message
    result = verify_decrypted_message(decrypted_text)
    print(f"Verification Result: {result}")

if __name__ == "__main__":
    main()
