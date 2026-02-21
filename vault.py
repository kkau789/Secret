# vault.py
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Read environment variables from Render
PIN = os.environ.get("PIN")
FILE = os.environ.get("FILE")
port = int(os.environ.get("PORT", 5000))

# Simple HTML template for web menu
HTML_TEMPLATE = """
<!doctype html>
<title>Secret Vault</title>
<h1>Secret Vault 🔐</h1>

{% if not authenticated %}
<form method="post">
  Enter PIN: <input type="password" name="pin">
  <input type="submit" value="Login">
</form>
{% else %}
<form method="post">
  <textarea name="note" placeholder="Write your secret note"></textarea><br>
  <input type="submit" value="Add Note">
</form>
<h2>Your Secrets:</h2>
<pre>{{ secrets }}</pre>
{% endif %}
"""

def read_secrets():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return f.read()
    return ""

def add_secret(note):
    with open(FILE, "a") as f:
        f.write(note + "\n")

@app.route("/", methods=["GET", "POST"])
def home():
    authenticated = False
    secrets = ""
    
    if "authenticated" in request.cookies and request.cookies.get("authenticated") == "yes":
        authenticated = True

    if request.method == "POST":
        if not authenticated:
            pin_input = request.form.get("pin", "")
            if pin_input == PIN:
                authenticated = True
            else:
                return render_template_string(HTML_TEMPLATE, authenticated=False, secrets="")
        else:
            note = request.form.get("note", "")
            if note.strip():
                add_secret(note)
    
    if authenticated:
        secrets = read_secrets()

    response = render_template_string(HTML_TEMPLATE, authenticated=authenticated, secrets=secrets)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
