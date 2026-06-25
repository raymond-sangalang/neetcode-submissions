class Solution:
    
    OFFSET = 3

    def encode(self, strs: List[str]) -> str:
        str_to_encoded = ""

        for word in strs:
            word_sz = len(word)
            new_encoded = f"{word_sz}#"
            for i in range(word_sz):
                # Add to the ASCII value and wrap around with modulo
                rotated_ascii = (ord(word[i]) + self.OFFSET) % 128
                rotated_char = chr(rotated_ascii)
                
                # Append character to substring
                new_encoded += rotated_char
           
            # Append to returned encoded string
            str_to_encoded += new_encoded
        print(str_to_encoded)
        return str_to_encoded
            
        

    def decode(self, s: str) -> List[str]:
        result_list = []
        index = 0

        # Iterate through each character of the string
        while index < len(s):
            
            j = index
            # Locate the 'hashtag' delimiter at the end of a word
            while s[j] != "#":
                j += 1

            len_word = int(s[index:j])
            index = j + 1

            end = index + len_word
            word_to_add = ""

            while index < end:
                rotated_ascii = (ord(s[index]) - self.OFFSET) % 128
                word_to_add += chr(rotated_ascii)
                index += 1

            result_list.append(word_to_add)

        return result_list




