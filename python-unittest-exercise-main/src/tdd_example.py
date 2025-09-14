class TDDExample():
    def __init__(self):
        pass

    def reverse_string(self, input_str: str) -> str:
        """
        Reverses order of characters in string input_str.
        """
        s1=input_str[::-1]
        return s1

    def find_longest_word(self, sentence: str) -> str:
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        sentence=sentence.strip()
        l1=sentence.split(" ")
        max=""
        for i in l1:
            if len(max)<len(i):
                max=i

        return max

    def reverse_list(self, input_list: list) -> list:
        """
        Reverses order of elements in list input_list.
        """
        
        n=len(input_list)
        n2=n//2
        for i in range(0,n2):
            input_list[i],input_list[n-i-1]=input_list[n-1-i],input_list[i]

        return input_list

    def count_digits(self, input_list: list, number_to_be_counted: int) -> int:
        """
        Return count of digits
        """
        
        s=set()
        for i in input_list:
            s.add(i)

        l2=list(s)
        return len(l2)