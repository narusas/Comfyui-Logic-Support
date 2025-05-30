class StringSwitchByNumber:
    """
    String Switch By Number Node: Outputs a string based on a numeric index input, supporting up to 15 strings.
    
    This node selects and outputs one of the input strings based on the provided numeric index.
    The index is 1-based, meaning index 1 selects string1, index 2 selects string2, and so on.
    
    If the provided index is out of range (less than 1 or greater than 15), the node defaults to returning string1.
    
    The node is useful for creating dynamic content selection, implementing conditional text outputs,
    or building decision-based workflows where different text options need to be selected.
    
    Usage examples:
    - With number=2 and string1="Option A", string2="Option B", string3="Option C": returns "Option B"
    - With number=5 and five different strings configured: returns the fifth string
    - With number=0 (out of range): returns string1 as the default
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "number": ("INT", {"default": 1, "min": 1, "max": 15, "step": 1}),
                "string1": ("STRING", {"default": "문자열1"}),
                "string2": ("STRING", {"default": "문자열2"}),
                "string3": ("STRING", {"default": "문자열3"}),
                "string4": ("STRING", {"default": "문자열4"}),
                "string5": ("STRING", {"default": "문자열5"}),
                "string6": ("STRING", {"default": "문자열6"}),
                "string7": ("STRING", {"default": "문자열7"}),
                "string8": ("STRING", {"default": "문자열8"}),
                "string9": ("STRING", {"default": "문자열9"}),
                "string10": ("STRING", {"default": "문자열10"}),
                "string11": ("STRING", {"default": "문자열11"}),
                "string12": ("STRING", {"default": "문자열12"}),
                "string13": ("STRING", {"default": "문자열13"}),
                "string14": ("STRING", {"default": "문자열14"}),
                "string15": ("STRING", {"default": "문자열15"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = "STRING"
    FUNCTION = "switch"
    CATEGORY = "Logic-Support"

    def switch(self, number, string1, string2, string3, string4, string5, 
               string6, string7, string8, string9, string10,
               string11, string12, string13, string14, string15):
        # 숫자 값이 범위를 벗어나면 기본값으로 1 사용
        if number < 1 or number > 15:
            number = 1
        
        # 숫자에 따라 해당 문자열 반환
        strings = [string1, string2, string3, string4, string5, 
                  string6, string7, string8, string9, string10,
                  string11, string12, string13, string14, string15]
        
        selected_string = strings[number - 1]  # 인덱스는 0부터 시작하므로 -1 처리
        
        return (selected_string,)

NODE_CLASS_MAPPINGS = {
    "StringSwitchByNumber": StringSwitchByNumber
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringSwitchByNumber": "String Switch By Number"
}
