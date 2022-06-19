import os
import secrets
from flask import render_template, url_for, flash, redirect, request, abort
from RLV import app, db, bcrypt

@app.route("/")
def home():
    return render_template('intro.html')