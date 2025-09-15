class TDDExample():
    def __init__(self):
        pass
 
    def reverse_string(self, input_str: str) -> str:
        """Reverses order of characters in string input_str."""
        return input_str[::-1] if input_str is not None else input_str
 
    def find_longest_word(self, sentence: str) -> str:
        """Returns the longest word in string sentence. If ties, return the first."""
        import re
        words = re.findall(r"\w+", sentence)  # splits on non-word chars, removes punctuation/newlines
        if not words:
            return ""
        return max(words, key=len)
 
    def reverse_list(self, input_list: list) -> list:
        """Reverses order of elements in list input_list."""
        return list(reversed(input_list))
 
    def count_digits(self, input_list: list, number_to_be_counted: int) -> int:
        """Return count of occurrences of number_to_be_counted in input_list."""
        return input_list.count(number_to_be_counted)