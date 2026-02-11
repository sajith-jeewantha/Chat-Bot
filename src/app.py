import os
from flask import Flask, render_template, url_for, request, redirect, session
from flask_session import Session
from src.bot import chat

app = Flask(__name__)
app.app_context()
app.secret_key = "fef745ab4ea539b541eb68697f3cf7a85cbdc1dcf59a02446c51cb6f3c8a1ac1"

# store sessions server-side (filesystem is simplest)
app.config["SESSION_TYPE"] = "filesystem"
# app.config["SESSION_FILE_DIR"] = "./.flask_session"
app.config["SESSION_FILE_DIR"] = os.path.join(app.root_path, ".flask_session")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_FILE_THRESHOLD"] = 1
Session(app)

@app.route('/clear', methods=['POST'])
def clear():
    session.pop('chats', None)
    return redirect(url_for('index'))


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'chats' not in session:
        session['chats'] = []

    if request.method == 'POST':
        message = request.form['message']
        responses = chat(message)

        chats = session['chats']  # get current list
        chats.append({"bot": False, "message": message})
        chats.append({"bot": True, "message": responses})
        session['chats'] = chats  # save back
        session.modified = True

        return redirect(url_for('index'))

    return render_template('index.html', chats=session['chats'])


if __name__ == '__main__':
    app.run(debug=True)
