from . import user



def init_app(app):
    app.register_blueprint(user.BP, url_prefix='/')

