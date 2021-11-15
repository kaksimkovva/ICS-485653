import collections


class String:

    def repeat_a_sequence_of_characters(self, string_value):
        dictionary = {}
        results = collections.Counter(string_value)
        for key, value in results.items():
            dictionary[key] = value
            if value >= 3:
                print("True")
                return True
            else:
                print("False")
                return False

    def palindrome(self, string_value):
        reverse_string = string_value[::-1]
        if string_value == reverse_string:
            print("True")
            return True
        else:
            print("False")
            return False


string_class = String()
string_class.repeat_a_sequence_of_characters("sssaaaaa")
string_class.palindrome("шабаш")