from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
import requests
from flask_wtf import CSRFProtect
from flask_csp.csp import csp_header
import logging

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = b"uyZJieNY0lywRNdG"

@app.route("/index.html", methods= ["GET"])
def root():
    return redirect("/", 302)

@app.route("/", methods = ["GET"])
@csp_header(
    {
        "default-src": "'self'",
        "script-src": "'self'",
        "img-src": "http: https: data:",
        "object-src": "'self'",
        "style-src": "'self'",
        "media-src": "'self'",
        "child-src": "'self'",
        "connect-src": "'self'",
        "base-uri": "",
        "report-uri": "/csp_report",
        "frame-ancestors": "none",
    }
)

def index():
    return render_template("/index.html")

@app.route("/csp_report", methods= ["POST"])
@csrf.exempt
def csp_report():
    app.logger.critical(request.data.decode())
    return "done"