"""
Renders the static index.html for GitHub Pages (no contact form).
Run this before committing/pushing to generate the static site file.

    python build.py
"""

from app import app

with app.app_context():
    with app.test_request_context():
        from flask import render_template
        html = render_template("index.html")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Built index.html for GitHub Pages (contact form excluded).")
