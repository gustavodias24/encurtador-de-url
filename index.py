from flask import Flask
from api.blueprints.CRUD import crud_bp
from api.blueprints.RedLinks import redlinks_bp

app = Flask(__name__)
app.register_blueprint(crud_bp)
app.register_blueprint(redlinks_bp)

if __name__ == "__main__":
    app.run(debug=True)
