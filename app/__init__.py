from flask import Flask

from config import Config
from app.extensions import db


def create_app(config_class=None):
  
  if config_class is None:
    config_class = Config

  app = Flask(__name__)
  app.config.from_object(Config)

  # Initialize Flask extensions here
  db.init_app(app)


  @app.cli.command("migrate")
  def migrate():
    with app.app_context():
      db.drop_all()
      db.create_all()
      db.session.commit()

    print("[INFO] Database migration has been done.")


  @app.cli.command("scrap")
  def scrap():
    pass

  return app
