class BooleanIndexAdder:
    """
    Boolean Index Adder Node: Adds the index of the first true value among 15 boolean inputs to a base number.
    
    This node takes up to 15 boolean inputs and a base number. It finds the first boolean input that is true 
    and adds its index (1-based) to the base number. If no boolean input is true, it returns the base number unchanged.
    
    The node is useful for creating conditional logic flows where different paths need to be selected based on 
    boolean conditions, and the result needs to be used as an index or identifier.
    
    Usage examples:
    - With base_number=10 and bool1=False, bool2=True, bool3=False: returns 10+2=12
    - With base_number=5 and all boolean inputs False: returns 5
    - With base_number=0 and bool4=True: returns 0+4=4
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
                "bool11": ("BOOLEAN", {"default": False}),
                "bool12": ("BOOLEAN", {"default": False}),
                "bool13": ("BOOLEAN", {"default": False}),
                "bool14": ("BOOLEAN", {"default": False}),
                "bool15": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = "INT"
    FUNCTION = "add_index"
    CATEGORY = "Logic-Support"

    def add_index(self, base_number, bool1, bool2, bool3, bool4, bool5, 
                 bool6, bool7, bool8, bool9, bool10, bool11, bool12, bool13, bool14, bool15):
        # 모든 boolean 값을 리스트로 모음
        bools = [bool1, bool2, bool3, bool4, bool5, 
                bool6, bool7, bool8, bool9, bool10,
                bool11, bool12, bool13, bool14, bool15]
        
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
