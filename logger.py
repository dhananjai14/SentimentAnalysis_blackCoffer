import logging


class logs:

    def __int__(self):
        pass

    def write_log(self, process_name, log_msg, log_level='info'):
        """
        Write log to the logger file
        :param  process_name: Current process name
        :param log_msg: What need to be logged
        :param log_level: default "INFO". Options available: 'info , 'warning', 'error', 'critical', 'exception'
        :return: None
        """
        p_name = process_name
        filename = r'C:\Users\preet\Desktop\DS\Project\Blackcoffer\code_logs\{}.txt'.format(p_name)
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(name)s %(message)s')
        if log_level == 'info':
            logging.info('\t\t' + log_msg)
        if log_level == 'warning':
            logging.warning('\t\t' + log_msg)
        if log_level == 'error':
            logging.error('\t\t' + log_msg)
        if log_level == 'critical':
            logging.critical('\t\t' + log_msg)
        if log_level == 'exception':
            logging.exception('\t\t' + log_msg)
