import os
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = os.environ["SMTP_USER"]      # your Gmail address
SMTP_PASS = os.environ["SMTP_PASS"]      # Gmail app password
NOTIFY_TO = os.environ.get("NOTIFY_TO", SMTP_USER)  # defaults to same address


def send_notification(name: str, email: str, message: str) -> None:
    msg = EmailMessage()
    msg["Subject"] = f"Portfolio contact from {name}"
    msg["From"]    = SMTP_USER
    msg["To"]      = NOTIFY_TO
    msg.set_content(
        f"Name:    {name}\n"
        f"Email:   {email}\n"
        f"\n"
        f"{message}\n"
    )
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USER, SMTP_PASS)
        smtp.send_message(msg)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/contact", methods=["POST"])
def contact():
    data    = request.get_json()
    name    = data.get("name", "").strip()
    email   = data.get("email", "").strip()
    message = data.get("message", "").strip()

    if not name or not email or not message:
        return jsonify({"success": False, "error": "All fields are required."}), 400

    try:
        send_notification(name, email, message)
    except Exception as e:
        print(f"Failed to send email: {e}")
        return jsonify({"success": False, "error": "Failed to send message. Please try again."}), 500

    return jsonify({"success": True, "message": f"Thanks, {name}! I'll be in touch soon."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
