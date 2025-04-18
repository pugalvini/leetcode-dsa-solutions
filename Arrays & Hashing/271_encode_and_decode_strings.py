# Problem Statement: https://leetcode.com/problems/encode-and-decode-strings
# The `Codec` class provides methods to encode a list of strings into a single string and decode it back into a list of strings.
# This is useful for scenarios where you need to serialize and deserialize a list of strings, such as storing or transmitting data.
# Input:
#   - `encode`: A list of strings to be encoded into a single string.
#   - `decode`: A single encoded string to be decoded back into a list of strings.
# Output:
#   - `encode`: A single string representing the encoded list of strings.
#   - `decode`: A list of strings obtained by decoding the encoded string.

# Time Complexity:
#   - `encode`: O(n), where n is the total number of characters in all strings. Each string is processed once.
#   - `decode`: O(n), where n is the length of the encoded string. Each character is processed once.
# Space Complexity:
#   - O(n), where n is the size of the encoded string or the list of decoded strings.

import ast
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encode = ""
        for s in strs:
            encode += str(len(s)) + "#" + s
        return encode
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decode, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1

            length = int(s[i:j])
            decode.append(s[j+1: j+1+length])
            i = j+1+length
        return decode

if __name__ == "__main__":
    codec = Codec()

    # Example 1: Normal case
    strs = ["hello", "world"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    print("Input:", strs)
    print("Encoded:", encoded)
    print("Decoded:", decoded)
    # Expected:
    # Input: ["hello", "world"]
    # Encoded: "5#hello5#world"
    # Decoded: ["hello", "world"]

    # Example 2: Empty strings
    strs = ["", "abc", ""]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    print("Input:", strs)
    print("Encoded:", encoded)
    print("Decoded:", decoded)
    # Expected:
    # Input: ["", "abc", ""]
    # Encoded: "0#3#abc0#"
    # Decoded: ["", "abc", ""]

    # Example 3: Single string
    strs = ["single"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    print("Input:", strs)
    print("Encoded:", encoded)
    print("Decoded:", decoded)
    # Expected:
    # Input: ["single"]
    # Encoded: "6#single"
    # Decoded: ["single"]

    # Example 4: Empty list
    strs = []
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    print("Input:", strs)
    print("Encoded:", encoded)
    print("Decoded:", decoded)
    # Expected:
    # Input: []
    # Encoded: ""
    # Decoded: []
