import logging

# logging code. This is used for us to debug in case of an error. You can see the logs through kubectl logs <pod_name>
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def log_message(message):
	logger.info(message)