class NumberConditionChecker:
    """
    Number Condition Checker Node: Checks if a number is within specified bounds and returns a boolean result.
    
    This node evaluates whether an input number satisfies specified conditions using lower and upper bounds.
    The conditions can be configured using operators:
    - Lower bound: NONE, < (less than), <= (less than or equal to)
    - Upper bound: NONE, < (less than), <= (less than or equal to)
    
    When a bound is set to "NONE", that particular bound check is ignored.
    
    The node returns TRUE if the number satisfies all specified conditions, otherwise FALSE.
    
    Usage examples:
    - Check if a number is between 0 and 10: lower_value=0, lower_op="<=", number=5, upper_op="<", upper_value=10 → TRUE
    - Check if a number is positive: lower_value=0, lower_op="<", number=5, upper_op="NONE", upper_value=0 → TRUE
    - Check if a number is at most 100: lower_value=0, lower_op="NONE", number=75, upper_op="<=", upper_value=100 → TRUE
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
