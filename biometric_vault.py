from flask import Flask, jsonify, render_template_string, request
import os
import base64

app = Flask(__name__)

# Minimal HTML page with WebAuthn JS
HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Biometric Vault</title>
</head>
<body>
<h1>🔒 Biometric Vault</h1>
<button id="login">Unlock with Fingerprint</button>
<p id="status"></p>

<script>
const status = document.getElementById("status");
document.getElementById("login").addEventListener("click", async () => {
    try {
        // Create a dummy challenge from server
        const challenge = new Uint8Array([1,2,3,4,5,6,7,8]);
        const credential = await navigator.credentials.create({
            publicKey: {
                challenge: challenge,
                rp: { name: "Biometric Vault" },
                user: { id: new Uint8Array([1,2,3,4]), name: "Kiki", displayName: "Kiki" },
                pubKeyCredParams: [{ type: "public-key", alg: -7 }],
                authenticatorSelection: { authenticatorAttachment: "platform", userVerification: "required" },
                timeout: 60000
            }
        });
        console.log("Credential:", credential);
        status.innerText = "✅ Fingerprint verified! Vault unlocked!";
    } catch (err) {
        console.error(err);
        status.innerText = "❌ Fingerprint failed!";
    }
});
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
