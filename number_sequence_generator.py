class NumberSequenceGenerator:
    """
    Number Sequence Generator Node: Generates a sequence of numbers with specified repetitions.
    
    This node generates a sequence of numbers within a specified range (start_number to end_number),
    repeating each number a specified number of times before moving to the next number.
    
    Each time the node is executed, it outputs the next number in the sequence. When the sequence
    is complete (after outputting the end_number the specified number of times), it starts over
    from the beginning.
    
    Usage examples:
    - With start_number=1, end_number=3, repeat_count=2:
      Outputs 1,1,2,2,3,3,1,1,2,2,3,3,... on successive executions
    - With start_number=5, end_number=7, repeat_count=1:
      Outputs 5,6,7,5,6,7,... on successive executions
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "start_number": ("INT", {"default": 1, "min": 1, "max": 1000, "step": 1}),
                "end_number": ("INT", {"default": 10, "min": 1, "max": 1000, "step": 1}),
                "repeat_count": ("INT", {"default": 1, "min": 1, "max": 100, "step": 1}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = "NUMBER"
    FUNCTION = "generate_number"
    CATEGORY = "Logic-Support"
    
    # 클래스 변수로 현재 상태 저장
    current_number = 1
    current_repeat = 1
    
    def generate_number(self, start_number, end_number, repeat_count):
        # 범위 검증 - 시작 숫자가 종료 숫자보다 크면 값을 교환
        if start_number > end_number:
            start_number, end_number = end_number, start_number
        
        # 클래스 변수가 현재 범위를 벗어나면 초기화
        if (NumberSequenceGenerator.current_number < start_number or 
            NumberSequenceGenerator.current_number > end_number):
            NumberSequenceGenerator.current_number = start_number
            NumberSequenceGenerator.current_repeat = 1
        
        # 현재 숫자 저장
        result = NumberSequenceGenerator.current_number
        
        # 반복 횟수 증가
        NumberSequenceGenerator.current_repeat += 1
        
        # 현재 숫자의 반복 횟수가 지정된 반복 횟수에 도달하면 다음 숫자로 이동
        if NumberSequenceGenerator.current_repeat > repeat_count:
            NumberSequenceGenerator.current_number += 1
            NumberSequenceGenerator.current_repeat = 1
            
            # 종료 숫자를 넘어가면 시작 숫자로 돌아감
            if NumberSequenceGenerator.current_number > end_number:
                NumberSequenceGenerator.current_number = start_number
        
        return (result,)

NODE_CLASS_MAPPINGS = {
    "NumberSequenceGenerator": NumberSequenceGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NumberSequenceGenerator": "Number Sequence Generator"
}
