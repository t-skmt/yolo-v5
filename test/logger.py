from logging import basicConfig, getLogger, DEBUG

basicConfig(level=DEBUG)  # メインのファイルにのみ書く

logger = getLogger(__name__)

logger.debug('hello')
logger.info("Info")
logger.warning("WARNING!")
