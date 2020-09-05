from help_tools import HelpTools


class Decoder:
    def __init__(self, words_dict):
        self.words_dict = words_dict

    def decode(self, string):
        string += "0"
        final_string = ""
        word = ""
        for char in string:
            result = self.decode_char(char)
            if result is not None:
                if result != "flip":
                    word += result

                if result == "flip":
                    final_string += word[::-1] + " "
                    word = ""
            else:
                HelpTools.add_to_log(40, "value turned out to be None,from 'decode()'")
        return final_string.strip()

    def decode_char(self, search_value):
        for key, value in self.words_dict.items():
            if value == search_value:
                return key
        if search_value is not None:
            if search_value.isnumeric():
                return "flip"
            else:
                return search_value
        else:
            HelpTools.add_to_log(40, "value turned out to be None,from 'decode_char()'")
            return None
