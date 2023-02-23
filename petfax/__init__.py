from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)


    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  



    @app.route('/')
    def index():
        return "hello from pet fax"



    # @app.route('/pets')
    # def pets():
    #     return "its pets"


    from . import pet
    app.register_blueprint(pet.bp)



    from . import fact
    app.register_blueprint(fact.bp)

    from . import models 
    models.db.init_app(app)
    migrate = Migrate(app, models.db)


    return app