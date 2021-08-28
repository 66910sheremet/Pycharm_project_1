from step_one import generator
import logging
logging.basicConfig(level = logging.INFO)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Диаметр горловины смесителя, %s см2', generator.dg_opt)