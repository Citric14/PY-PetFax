from flask import Flask

def create_app():
    app = Flask(__name__)

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

    return app