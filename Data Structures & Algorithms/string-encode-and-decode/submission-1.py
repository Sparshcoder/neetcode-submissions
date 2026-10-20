class Solution:

    def encode(self, strs: List[str]) -> str:
        joined_string = "".join([f"{len(x)}#{x}" for x in strs])
        return joined_string

    def decode(self, s: str) -> List[str]:
        operative_string = s
        final_string_list = []
        while len(operative_string)>0:
            character_length = operative_string.split("#")[0]
            length_of_chra = len(character_length)
            final_string_list.append( operative_string[length_of_chra+1:int(character_length)+1+length_of_chra])
            operative_string = operative_string[int(character_length)+1+length_of_chra:]
        return final_string_list
