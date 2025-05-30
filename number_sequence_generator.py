class NumberSequenceGenerator:
    """
    Number Sequence Generator Node: Generates a sequence of numbers with specified repetitions.
    
    This node generates a sequence of numbers within a specified range (start_number to end_number),
    repeating each number a specified number of times before moving to the next number.
    
    Each time the node is executed, it outputs the next number in the sequence. When the sequence
    is complete (after outputting the end_number the specified number of times), it starts over
    from the beginning.
    
    The node maintains its state between workflow runs, similar to the Random Seed behavior in ComfyUI.
    This allows for continuous sequences across multiple executions of the workflow.
    
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
                "reset": (["no", "yes"], {"default": "no"}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = "NUMBER"
    FUNCTION = "generate_number"
    CATEGORY = "Logic-Support"
    
    # ComfyUI의 상태 저장 메커니즘을 활용하기 위한 플래그
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        if kwargs.get("reset", "no") == "yes":
            return float("nan")  # 항상 변경된 것으로 간주
        return False  # 상태 유지
    
    # 각 인스턴스마다 고유한 상태를 유지하기 위한 클래스 변수
    state = {}
    
    def generate_number(self, start_number, end_number, repeat_count, reset):
        # 범위 검증 - 시작 숫자가 종료 숫자보다 크면 값을 교환
        if start_number > end_number:
            start_number, end_number = end_number, start_number
        
        # 상태 키 생성 (범위와 반복 횟수로 구성)
        state_key = f"{start_number}_{end_number}_{repeat_count}"
        
        # 리셋이 요청되었거나 상태가 없는 경우 초기화
        if reset == "yes" or state_key not in NumberSequenceGenerator.state:
            NumberSequenceGenerator.state[state_key] = {
                "current_number": start_number,
                "current_repeat": 1
            }
        
        # 현재 상태 가져오기
        current_state = NumberSequenceGenerator.state[state_key]
        
        # 현재 숫자 저장
        result = current_state["current_number"]
        
        # 반복 횟수 증가
        current_state["current_repeat"] += 1
        
        # 현재 숫자의 반복 횟수가 지정된 반복 횟수에 도달하면 다음 숫자로 이동
        if current_state["current_repeat"] > repeat_count:
            current_state["current_number"] += 1
            current_state["current_repeat"] = 1
            
            # 종료 숫자를 넘어가면 시작 숫자로 돌아감
            if current_state["current_number"] > end_number:
                current_state["current_number"] = start_number
        
        return (result,)

NODE_CLASS_MAPPINGS = {
    "NumberSequenceGenerator": NumberSequenceGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NumberSequenceGenerator": "Number Sequence Generator"
}
