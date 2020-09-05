from help_tools import HelpTools


class Decoder:
    def __init__(self, words_dict):
        self.words_dict = words_dict

    def decode(self, string):
        final_string = ""
        word = ""
        char_counter = 0
        for char in string:
            result = self.decode_char(char)
            if result is not None:
                is_last = char_counter == len(string) - 1
                if result != "flip":
                    word += result
                    if is_last:
                        result = "flip"

                if result == "flip":
                    final_string += word[::-1] + " "
                    word = ""
            else:
                HelpTools.add_to_log(40, "value turned out to be None,from 'decode()'")
            char_counter += 1
        return final_string

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
