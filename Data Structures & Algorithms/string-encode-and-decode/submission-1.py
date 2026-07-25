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


#First for the given strings encode it, by adding all the inidividual strings into 
#one string, but to remember each inidividual string place a "#" and number before
#the "#" to count the number of characters in the string.
#Next in decoding first start a while loop for length of s, then another while loop
#to keep iterating until a "#" is found, then end it there convert the length to a
#integer and use slicing method to cut the string and append it to the decoded answer.


