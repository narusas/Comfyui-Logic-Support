class NumberConditionChecker:
    """
    숫자 범위 체크 노드: 입력된 숫자가 지정된 범위 안에 들어오면 true, 아니면 false를 출력합니다.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {                
                "lower_value": ("INT", {"default": 0}),
                "lower_op": (["NONE", "<", "<="], {"default": "<="}),
                "number": ("INT", {"default": 5}),
                "upper_op": (["NONE", "<", "<="], {"default": "<"}),
                "upper_value": ("INT", {"default": 10}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = "BOOLEAN"
    FUNCTION = "check_condition"
    CATEGORY = "Logic-Support"

    def check_condition(self, lower_value, lower_op, number, upper_op, upper_value):
        # 초기값을 True로 설정
        in_range = True
        
        # 하한 조건 확인 (NONE이 아닌 경우에만)
        if lower_op != "NONE":
            if lower_op == "<":
                if not (lower_value < number):
                    in_range = False
            elif lower_op == "<=":
                if not (lower_value <= number):
                    in_range = False
        
        # 상한 조건 확인 (NONE이 아닌 경우에만)
        if upper_op != "NONE":
            if upper_op == "<":
                if not (number < upper_value):
                    in_range = False
            elif upper_op == "<=":
                if not (number <= upper_value):
                    in_range = False
        
        return (in_range,)

NODE_CLASS_MAPPINGS = {
    "NumberConditionChecker": NumberConditionChecker
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NumberConditionChecker": "Number Condition Checker"
}
