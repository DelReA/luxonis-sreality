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
    pass

  @app.cli.command("scrap")
  def scrap():
    pass

  return app
