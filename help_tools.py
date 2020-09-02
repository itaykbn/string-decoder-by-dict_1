class HelpTools:
    @staticmethod
    def reverse(string):
        new_str = ""
        for i in string:
            new_str = i + new_str
        return new_str

    @staticmethod
    def represents_int(string):
        try:
            int(string)
            return True
        except ValueError:
            return False
