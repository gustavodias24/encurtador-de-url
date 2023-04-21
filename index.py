from flask import Flask
from api.blueprints.WriteLinks import write_bp
from api.blueprints.ReadLinks import readLinks_bp

app = Flask(__name__)
app.register_blueprint(write_bp)
app.register_blueprint(readLinks_bp)

if __name__ == "__main__":
    app.run(debug=True)
