class StringSwitchByNumber:
    """
    문자열 스위치 노드: 숫자 입력에 따라 해당 인덱스의 문자열을 출력합니다.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "number": ("INT", {"default": 1, "min": 1, "max": 10, "step": 1}),
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
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = "STRING"
    FUNCTION = "switch"
    CATEGORY = "Logic-Support"

    def switch(self, number, string1, string2, string3, string4, string5, 
               string6, string7, string8, string9, string10):
        # 숫자 값이 범위를 벗어나면 기본값으로 1 사용
        if number < 1 or number > 10:
            number = 1
        
        # 숫자에 따라 해당 문자열 반환
        strings = [string1, string2, string3, string4, string5, 
                  string6, string7, string8, string9, string10]
        
        selected_string = strings[number - 1]  # 인덱스는 0부터 시작하므로 -1 처리
        
        return (selected_string,)

NODE_CLASS_MAPPINGS = {
    "StringSwitchByNumber": StringSwitchByNumber
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringSwitchByNumber": "String Switch By Number"
}
