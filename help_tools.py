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
        except ValueError:
            return False
