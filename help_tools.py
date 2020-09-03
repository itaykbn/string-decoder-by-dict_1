import logging

logging.basicConfig(filename='logs.log', level=logging.DEBUG)


class HelpTools:
    @staticmethod
    def reverse(string):
        new_string = ""
        for i in string:
            new_string = i + new_string
        return new_string

    @staticmethod
    def represents_int(string):

        try:
            int(string)
            return True
        except ValueError:  # Errors should never pass silently. Unless explicitly silenced.
            logging.info('value not int')
            return False

    @staticmethod
    def clear_log(name):
        with open(name, 'w'):
            pass
