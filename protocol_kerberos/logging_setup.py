import logging


class AppLogging:
    @staticmethod
    def setup_logs():
        logging.basicConfig(
                filename='logging.log',
                filemode='a',
                format='%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                level=logging.DEBUG
            )
