import os
import sys
from flask import Flask
from flask_cors import CORS

# 🔧 Fix Python path so sibling folders are discoverable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routes.upload import upload_blueprint

app = Flask(__name__)
CORS(app)

# Register the route blueprint
app.register_blueprint(upload_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
