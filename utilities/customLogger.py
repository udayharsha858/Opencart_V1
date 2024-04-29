import logging


class LogGenerator:

    @staticmethod
    def log_generator():
        logging.basicConfig(filename="/Volumes/Work/QA_Python Project/Opencart_V1/logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s:', datefmt='%m/%d/%Y %I:%M:%S %p')
        logg = logging.getLogger()
        logg.setLevel(logging.DEBUG)
        return logg
