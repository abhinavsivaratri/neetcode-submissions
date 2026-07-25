class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0


        while i < len(s):
            length = ""
            
            while s[i] != "#":
                length += s[i]
                i += 1
            
            length = int(length)
            i += 1

            string = s[i:i+length]
            decoded_string.append(string)
            
            i += length  
        return decoded_string      


