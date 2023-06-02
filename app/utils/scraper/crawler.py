from scrapy import signals
from scrapy.signalmanager import dispatcher
from scrapy.crawler import CrawlerProcess

from app.extensions import db
from app.models import Flat

from . import FlatsSpider


def on_item_scraped(item):
  new_flat = Flat(item.get('title'), item.get('image_url'))
  db.session.add(new_flat)


def crawl_flats():
  dispatcher.connect(on_item_scraped, signal=signals.item_scraped)

  process = CrawlerProcess()
  process.crawl(FlatsSpider)
  process.start()

  db.session.commit()
