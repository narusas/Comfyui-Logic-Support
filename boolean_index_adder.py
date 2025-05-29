class BooleanIndexAdder:
    """
    Boolean 인덱스 더하기 노드: 10개의 boolean 값 중 true인 첫 번째 값의 인덱스를 입력 숫자에 더합니다.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_number": ("INT", {"default": 0}),
                "bool1": ("BOOLEAN", {"default": False}),
                "bool2": ("BOOLEAN", {"default": False}),
                "bool3": ("BOOLEAN", {"default": False}),
                "bool4": ("BOOLEAN", {"default": False}),
                "bool5": ("BOOLEAN", {"default": False}),
                "bool6": ("BOOLEAN", {"default": False}),
                "bool7": ("BOOLEAN", {"default": False}),
                "bool8": ("BOOLEAN", {"default": False}),
                "bool9": ("BOOLEAN", {"default": False}),
                "bool10": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = "INT"
    FUNCTION = "add_index"
    CATEGORY = "Logic-Support"

    def add_index(self, base_number, bool1, bool2, bool3, bool4, bool5, 
                 bool6, bool7, bool8, bool9, bool10):
        # 모든 boolean 값을 리스트로 모음
        bools = [bool1, bool2, bool3, bool4, bool5, 
                bool6, bool7, bool8, bool9, bool10]
        
        # true인 첫 번째 값의 인덱스 찾기 (1부터 시작)
        index_to_add = 0
        for i, b in enumerate(bools):
            if b:
                index_to_add = i + 1  # 인덱스는 1부터 시작하도록 +1
                break
        
        # 인덱스를 base_number에 더하기
        result = base_number + index_to_add
        
        return (result,)

NODE_CLASS_MAPPINGS = {
    "BooleanIndexAdder": BooleanIndexAdder
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BooleanIndexAdder": "Boolean Index Adder"
}
