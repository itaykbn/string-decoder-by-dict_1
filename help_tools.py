import logging

logging.basicConfig(filename='logs.log', level=logging.DEBUG)


class HelpTools:
    @staticmethod
    def clear_log(name):
        with open(name, 'w'):
            pass

    @staticmethod
    def add_to_log(alert_type, message):
        logging.log(alert_type, message)

    @staticmethod
    def delete_log_dialog():
        while True:
            delete_log = input("do you want to delete previous log? enter y/n")
            if delete_log == 'y':
                HelpTools.clear_log('logs.log')
                break
            elif delete_log == 'n':
                break
            else:
                print("invalid input")
