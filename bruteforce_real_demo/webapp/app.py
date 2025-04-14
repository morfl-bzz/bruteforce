from flask import Flask, render_template, request, jsonify, redirect, url_for
import time

app = Flask(__name__)

USERNAME = "user123"
PASSWORD = "pass123"

attempts = {}  # IP-based attempt tracking
logs = []  # Store logs for real-time feedback

@app.route("/unsafe", methods=["GET", "POST"])
def unsafe():
    global logs
    ip = request.remote_addr
    now = time.time()
    message = ""

    if ip not in attempts:
        attempts[ip] = {"count": 0, "last": 0}

    # Redirect to blocked page after 5 failed attempts
    if attempts[ip]["count"] >= 5:
        return redirect(url_for("blocked"))

    if request.method == "POST":
        user = request.form.get("username")
        pwd = request.form.get("password")

        if user == USERNAME and pwd == PASSWORD:
            attempts[ip] = {"count": 0, "last": 0}  # Reset attempts
            message = "Login erfolgreich!"
            logs.append(f"SUCCESS: {user} logged in with password '{pwd}'")
            return redirect(url_for("bank"))
        else:
            attempts[ip]["count"] += 1
            attempts[ip]["last"] = now
            message = "Login fehlgeschlagen"
            logs.append(f"FAILED: Attempt with password '{pwd}'")

    return render_template("unsafe.html", message=message, logs=logs)


@app.route("/blocked", methods=["GET"])
def blocked():
    ip = request.remote_addr
    if ip in attempts:
        attempts[ip]["count"] = 0
    return render_template("blocked.html")


@app.route("/bank", methods=["GET"])
def bank():
    return render_template("bank.html")


@app.route("/secure", methods=["GET", "POST"])
def secure():
    global logs
    ip = request.remote_addr
    now = time.time()
    message = ""

    if ip not in attempts:
        attempts[ip] = {"count": 0, "last": 0}

    # Block IP for 60 seconds after 5 failed attempts
    if attempts[ip]["count"] >= 5 and now - attempts[ip]["last"] < 60:
        return redirect(url_for("blocked"))  # Redirect to the blocked page  # Redirect to the blocked page

    if request.method == "POST":
        user = request.form.get("username")
        pwd = request.form.get("password")

        if user == USERNAME and pwd == PASSWORD:
            attempts[ip] = {"count": 0, "last": 0}  # Reset attempts
            message = "Login erfolgreich!"
            logs.append(f"SUCCESS: {user} logged in with password '{pwd}'")
        else:
            attempts[ip]["count"] += 1
            attempts[ip]["last"] = now
            message = "Login fehlgeschlagen"
            logs.append(f"FAILED: Attempt with password '{pwd}'")

    return render_template("secure.html", message=message, logs=logs)


@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(logs)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)