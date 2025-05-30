class StringConcatenator:
    """
    String Concatenator Node: Concatenates up to 15 input strings into a single output string with a specified separator.
    
    This node takes up to 15 string inputs and joins them together using a specified separator.
    Empty strings are automatically filtered out before concatenation.
    
    Available separator types:
    - EMPTY: No separator (direct concatenation)
    - COMMA: Comma separator ", "
    - SPACE: Space separator " "
    - PIPE: Pipe separator " | "
    
    The node is useful for creating dynamic text combinations, building prompts, or generating formatted output strings.
    
    Usage examples:
    - With separator_type="COMMA" and string1="Hello", string2="World": returns "Hello, World"
    - With separator_type="SPACE" and string1="ComfyUI", string2="Logic", string3="Support": returns "ComfyUI Logic Support"
    - With separator_type="EMPTY" and string1="prefix_", string2="suffix": returns "prefix_suffix"
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "separator_type": (["EMPTY", "COMMA", "SPACE", "PIPE"], {"default": "EMPTY"}),
                "string1": ("STRING", {"default": ""}),
                "string2": ("STRING", {"default": ""}),
                "string3": ("STRING", {"default": ""}),
                "string4": ("STRING", {"default": ""}),
                "string5": ("STRING", {"default": ""}),
            },
            "optional": {
                "string6": ("STRING", {"default": ""}),
                "string7": ("STRING", {"default": ""}),
                "string8": ("STRING", {"default": ""}),
                "string9": ("STRING", {"default": ""}),
                "string10": ("STRING", {"default": ""}),
                "string11": ("STRING", {"default": ""}),
                "string12": ("STRING", {"default": ""}),
                "string13": ("STRING", {"default": ""}),
                "string14": ("STRING", {"default": ""}),
                "string15": ("STRING", {"default": ""}),                
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = "CONCATENATED_STRING"
    FUNCTION = "concatenate"
    CATEGORY = "Logic-Support"

    def concatenate(self, string1, string2, string3, string4, string5, 
                   string6="", string7="", string8="", string9="", string10="",
                   string11="", string12="", string13="", string14="", string15="",
                   separator_type="EMPTY"):
        # 모든 문자열을 리스트로 모음
        strings = [string1, string2, string3, string4, string5, 
                  string6, string7, string8, string9, string10,
                  string11, string12, string13, string14, string15]
        
        # 빈 문자열이 아닌 것만 필터링
        filtered_strings = [s for s in strings if s]
        
        # 구분자 타입에 따라 적절한 구분자 선택
        separator = ""
        if separator_type == "COMMA":
            separator = ","
        elif separator_type == "SPACE":
            separator = " "
        elif separator_type == "PIPE":
            separator = "|"
        # EMPTY는 기본값인 공백 문자열 사용
            
        # 구분자를 사용하여 문자열 연결
        result = separator.join(filtered_strings)
        
        return (result,)

NODE_CLASS_MAPPINGS = {
    "StringConcatenator": StringConcatenator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringConcatenator": "String Concatenator"
}
