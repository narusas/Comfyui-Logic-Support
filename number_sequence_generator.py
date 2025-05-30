import os
import json
import time

# 로그 파일 경로 설정
LOG_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(LOG_DIR, "sequence_generator_log.txt")

def log_debug(message):
    """디버그 메시지를 로그 파일에 기록"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

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
        reset = kwargs.get("reset", "no")
        log_debug(f"IS_CHANGED 호출됨: reset={reset}, kwargs={kwargs}")
        if reset == "yes":
            log_debug("IS_CHANGED: 리셋 요청으로 float('nan') 반환")
            return float("nan")  # 항상 변경된 것으로 간주
        log_debug("IS_CHANGED: 상태 유지를 위해 False 반환")
        return False  # 상태 유지
    
    # 각 인스턴스마다 고유한 상태를 유지하기 위한 클래스 변수
    state = {}
    
    def generate_number(self, start_number, end_number, repeat_count, reset):
        log_debug(f"generate_number 호출: start={start_number}, end={end_number}, repeat={repeat_count}, reset={reset}")
        log_debug(f"현재 상태 딕셔너리: {json.dumps(NumberSequenceGenerator.state, indent=2)}")
        
        # 범위 검증 - 시작 숫자가 종료 숫자보다 크면 값을 교환
        if start_number > end_number:
            log_debug(f"범위 교환: {start_number} > {end_number}, 교환 후: {end_number}, {start_number}")
            start_number, end_number = end_number, start_number
        
        # 상태 키 생성 (범위와 반복 횟수로 구성)
        state_key = f"{start_number}_{end_number}_{repeat_count}"
        log_debug(f"상태 키: {state_key}")
        
        # 리셋이 요청되었거나 상태가 없는 경우 초기화
        if reset == "yes" or state_key not in NumberSequenceGenerator.state:
            if reset == "yes":
                log_debug(f"리셋 요청으로 상태 초기화")
            elif state_key not in NumberSequenceGenerator.state:
                log_debug(f"상태 키가 없어 상태 초기화: {state_key}")
            
            NumberSequenceGenerator.state[state_key] = {
                "current_number": start_number,
                "current_repeat": 1
            }
            log_debug(f"초기화된 상태: {NumberSequenceGenerator.state[state_key]}")
        
        # 현재 상태 가져오기
        current_state = NumberSequenceGenerator.state[state_key]
        log_debug(f"현재 상태: {current_state}")
        
        # 현재 숫자 저장
        result = current_state["current_number"]
        log_debug(f"결과 값: {result}")
        
        # 반복 횟수 증가
        current_state["current_repeat"] += 1
        log_debug(f"반복 횟수 증가: {current_state['current_repeat']}")
        
        # 현재 숫자의 반복 횟수가 지정된 반복 횟수에 도달하면 다음 숫자로 이동
        if current_state["current_repeat"] > repeat_count:
            current_state["current_number"] += 1
            current_state["current_repeat"] = 1
            log_debug(f"다음 숫자로 이동: {current_state['current_number']}")
            
            # 종료 숫자를 넘어가면 시작 숫자로 돌아감
            if current_state["current_number"] > end_number:
                current_state["current_number"] = start_number
                log_debug(f"범위 끝에 도달하여 처음으로 돌아감: {start_number}")
        
        log_debug(f"업데이트된 상태: {NumberSequenceGenerator.state}")
        log_debug(f"반환 값: {result}\n{'-'*50}")
        
        return (result,)

# 로그 파일 초기화 (모듈 로드 시 한 번만 실행)
if os.path.exists(LOG_FILE):
    # 로그 파일이 너무 크면 초기화
    if os.path.getsize(LOG_FILE) > 1024 * 1024:  # 1MB 이상이면 초기화
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 로그 파일 초기화\n")

log_debug("\n" + "="*50)
log_debug(f"NumberSequenceGenerator 모듈 로드됨: {time.strftime('%Y-%m-%d %H:%M:%S')}")
log_debug(f"로그 파일 경로: {LOG_FILE}")

NODE_CLASS_MAPPINGS = {
    "NumberSequenceGenerator": NumberSequenceGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NumberSequenceGenerator": "Number Sequence Generator"
}
