from flask import Flask, redirect, url_for, session, request # type: ignore
from google.auth.transport.requests import Request # type: ignore
from google_auth_oauthlib.flow import Flow # type: ignore
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

GOOGLE_CLIENT_SECRET_FILE = "modules/client_secret_1049775549569-o1c8j1rt8lr0ajacso7u49d6fa7eum3o.apps.googleusercontent.com.json"
SCOPES = ["https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile", "openid"]

flow = Flow.from_client_secrets_file(
    GOOGLE_CLIENT_SECRET_FILE,
    scopes=SCOPES,
    redirect_uri="http://localhost:5000/callback"
)

@app.route("/login")
def login():
    auth_url, _ = flow.authorization_url(prompt="consent")
    return redirect(auth_url)

@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials
    session["user"] = credentials.token
    return "Login exitoso con Google"

if __name__ == "__main__":
    app.run(debug=True)
