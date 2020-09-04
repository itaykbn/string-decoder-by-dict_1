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
                if char_counter == len(string) - 1:
                    word += result
                    result = "flip"

                if result != "flip":
                    word += result
                else:
                    final_string += HelpTools.reverse(word) + " "
                    word = ""
            char_counter += 1
        return final_string

    def decode_char(self, search_value):
        for key, value in self.words_dict.items():
            if value == search_value:
                result = key
                return result
        if search_value is not None:
            if HelpTools.represents_int(search_value):
                return "flip"
            else:
                return search_value

        return None
