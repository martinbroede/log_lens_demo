from logging.handlers import TimedRotatingFileHandler


class DummyFileHandler(TimedRotatingFileHandler):
    """
    Handler to test if custom handlers are working
    """
