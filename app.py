from flask import Flask, render_template_string, request

app = Flask(__name__)
PIN = "1234"
notes = []
unlocked = False

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Secret Vault</title>
<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #1e1e2f, #2b5876);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(15px);
    padding: 30px;
    border-radius: 20px;
    width: 90%;
    max-width: 400px;
    color: white;
    text-align: center;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

input {
    width: 100%;
    padding: 12px;
    margin: 10px 0;
    border-radius: 10px;
    border: none;
    outline: none;
}

button {
    width: 100%;
    padding: 12px;
    border-radius: 10px;
    border: none;
    background: #00c6ff;
    color: white;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

button:hover {
    background: #0072ff;
}

.note {
    background: rgba(255,255,255,0.1);
    padding: 8px;
    border-radius: 8px;
    margin-top: 5px;
}
</style>
</head>
<body>

<div class="card">
<h2>🔐 Secret Vault</h2>

{% if not unlocked %}
<form method="POST">
<input type="password" name="pin" placeholder="Enter PIN">
<button type="submit">Unlock</button>
</form>
{% else %}
<form method="POST">
<input type="text" name="note" placeholder="Write your secret...">
<button type="submit">Save</button>
</form>

<h3>Your Notes</h3>
{% for n in notes %}
<div class="note">{{n}}</div>
{% endfor %}
{% endif %}

</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    global unlocked
    if request.method == "POST":
        if not unlocked:
            if request.form["pin"] == PIN:
                unlocked = True
        else:
            notes.append(request.form["note"])
    return render_template_string(HTML, unlocked=unlocked, notes=notes)

app.run(host="0.0.0.0", port=5000)
