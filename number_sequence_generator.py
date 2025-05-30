import os
import json
import time
import sys

# 로그 파일 경로 설정 - 절대 경로 사용
LOG_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(LOG_DIR, "sequence_generator_log.txt")

# 디버그 모드 설정 (필요할 때만 True로 변경)
DEBUG_MODE = False

def log_debug(message):
    """디버그 메시지를 로그 파일과 콘솔에 기록"""
    if not DEBUG_MODE:
        return
        
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"
    
    # 콘솔에 출력
    print(f"[NumberSequenceGenerator] {log_message}")
    sys.stdout.flush()  # 출력 버퍼 강제 플러시
    
    # 파일에 기록
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{log_message}\n")
    except Exception as e:
        print(f"[NumberSequenceGenerator] 로그 파일 쓰기 오류: {e}")

# ComfyUI의 상태 관리 메커니즘을 활용하기 위한 클래스
class SequenceState:
    def __init__(self, start_number, end_number, repeat_count):
        self.start_number = start_number
        self.end_number = end_number
        self.repeat_count = repeat_count
        self.current_number = start_number
        self.current_repeat = 1
        
    def get_next(self):
        result = self.current_number
        
        # 반복 횟수 증가
        self.current_repeat += 1
        
        # 현재 숫자의 반복 횟수가 지정된 반복 횟수에 도달하면 다음 숫자로 이동
        if self.current_repeat > self.repeat_count:
            self.current_number += 1
            self.current_repeat = 1
            
            # 종료 숫자를 넘어가면 시작 숫자로 돌아감
            if self.current_number > self.end_number:
                self.current_number = self.start_number
        
        return result
    
    def to_dict(self):
        return {
            "start_number": self.start_number,
            "end_number": self.end_number,
            "repeat_count": self.repeat_count,
            "current_number": self.current_number,
            "current_repeat": self.current_repeat
        }
    
    @classmethod
    def from_dict(cls, data):
        state = cls(
            data["start_number"],
            data["end_number"],
            data["repeat_count"]
        )
        state.current_number = data["current_number"]
        state.current_repeat = data["current_repeat"]
        return state

class NumberSequenceGenerator:
    """
    Number Sequence Generator Node: Generates a sequence of numbers with specified repetitions.
    
    이 노드는 지정된 범위(start_number부터 end_number까지)의 숫자를 순차적으로 반환합니다.
    각 숫자는 repeat_count번 반복되며, 범위의 끝에 도달하면 다시 처음부터 시작합니다.
    이 노드는 ComfyUI의 상태 저장 메커니즘을 활용하여 실행 간에 상태를 유지합니다.
    
    Usage examples:
    - With start_number=1, end_number=3, repeat_count=2:
      Outputs 1,1,2,2,3,3,1,1,2,2,3,3,... on successive executions
    - With start_number=5, end_number=7, repeat_count=1:
      Outputs 5,6,7,5,6,7,... on successive executions
    """
    
    # 워크플로우 단위로 상태를 관리하기 위한 디셔너리
    states = {}
    # 마지막 출력 값 저장을 위한 디셔너리
    last_outputs = {}
    # 현재 워크플로우 ID
    current_workflow_id = "default"
    # 상태 파일 경로
    STATE_FILE = os.path.join(LOG_DIR, "sequence_generator_state.json")
    
    @classmethod
    def load_state_from_file(cls):
        """파일에서 상태 로드"""
        try:
            if os.path.exists(cls.STATE_FILE):
                with open(cls.STATE_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # 상태 디셔너리 복원
                    workflow_states = data.get("states", {})
                    for workflow_id, state_data in workflow_states.items():
                        cls.states[workflow_id] = {}
                        for state_key, state_dict in state_data.items():
                            cls.states[workflow_id][state_key] = SequenceState.from_dict(state_dict)
                    
                    # 마지막 출력 값 복원
                    cls.last_outputs = data.get("last_outputs", {})
                    log_debug(f"파일에서 상태 로드 성공: {len(cls.states)} 워크플로우")
        except Exception as e:
            log_debug(f"파일에서 상태 로드 실패: {e}")
    
    @classmethod
    def save_state_to_file(cls):
        """파일에 상태 저장"""
        try:
            # 상태 디셔너리를 저장 가능한 형태로 변환
            workflow_states = {}
            for workflow_id, state_data in cls.states.items():
                workflow_states[workflow_id] = {}
                for state_key, state_obj in state_data.items():
                    workflow_states[workflow_id][state_key] = state_obj.to_dict()
            
            data = {
                "states": workflow_states,
                "last_outputs": cls.last_outputs
            }
            
            with open(cls.STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                
            log_debug(f"파일에 상태 저장 성공: {len(cls.states)} 워크플로우")
        except Exception as e:
            log_debug(f"파일에 상태 저장 실패: {e}")
    
    @classmethod
    def INPUT_TYPES(cls):
        # 현재 워크플로우 ID 가져오기
        workflow_id = getattr(cls, "current_workflow_id", "default")
        
        # 마지막 출력 값 표시를 위한 문자열 생성
        current_value = "N/A"
        if workflow_id in cls.last_outputs and cls.last_outputs[workflow_id]:
            # 가장 최근 값 가져오기
            current_value = list(cls.last_outputs[workflow_id].values())[-1]
        
        return {
            "required": {
                "start_number": ("INT", {"default": 1, "min": 1, "max": 1000, "step": 1}),
                "end_number": ("INT", {"default": 10, "min": 1, "max": 1000, "step": 1}),
                "repeat_count": ("INT", {"default": 1, "min": 1, "max": 100, "step": 1}),
                "reset": (["no", "yes"], {"default": "no"}),
            },
            "hidden": {
                "unique_id": ("STRING", {"default": "none"}),  # ComfyUI가 자동으로 설정하는 노드 고유 ID
                "current_value": ("STRING", {"default": f"현재 값: {current_value}"}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = "NUMBER"
    FUNCTION = "generate_number"
    CATEGORY = "Logic-Support"
    
    # ComfyUI의 상태 저장 메커니즘을 활용하기 위한 플래그
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        reset = kwargs.get("reset", "no")
        unique_id = kwargs.get("unique_id", "none")
        prompt = kwargs.get("prompt", None)
        extra_pnginfo = kwargs.get("extra_pnginfo", None)
        
        log_debug(f"IS_CHANGED 호출됨: reset={reset}, unique_id={unique_id}")
        
        # 워크플로우 정보 가져오기 시도
        workflow_id = "default"
        try:
            if extra_pnginfo is not None and "workflow" in extra_pnginfo:
                workflow = extra_pnginfo["workflow"]
                workflow_id = str(workflow.get("id", "default"))
                log_debug(f"IS_CHANGED: 워크플로우 ID 가져오기 성공: {workflow_id}")
        except Exception as e:
            log_debug(f"IS_CHANGED: 워크플로우 정보 가져오기 실패: {e}")
        
        # 워크플로우 ID 저장
        cls.current_workflow_id = workflow_id
        
        if reset == "yes":
            log_debug("IS_CHANGED: 리셋 요청으로 float('nan') 반환")
            return float("nan")  # 항상 변경된 것으로 간주
        
        # 항상 노드가 실행되도록 float('nan') 반환
        # ComfyUI에서 IS_CHANGED가 False를 반환하면 노드가 실행되지 않고 이전 결과를 재사용함
        log_debug("IS_CHANGED: 항상 노드가 실행되도록 float('nan') 반환")
        return float("nan")
        
    @classmethod
    def VALIDATE_INPUTS(cls, **kwargs):
        log_debug(f"VALIDATE_INPUTS 호출됨: kwargs={kwargs}")
        return True
    
    # 워크플로우별 상태 관리를 위한 메서드
    @classmethod
    def get_state_for_workflow(cls, workflow_id, start_number, end_number, repeat_count, reset="no"):
        """특정 워크플로우에 대한 상태 가져오기"""
        log_debug(f"워크플로우 {workflow_id}의 상태 가져오기")
        
        # 파일에서 상태 로드 (상태가 비어있는 경우에만)
        if not cls.states:
            cls.load_state_from_file()
            log_debug(f"파일에서 상태 로드 완료: {list(cls.states.keys())}")
        
        # 워크플로우 ID가 없으면 새로운 임시 ID 생성
        if workflow_id == "none":
            workflow_id = f"temp_{time.time()}"
            log_debug(f"임시 워크플로우 ID 생성: {workflow_id}")
        
        # 워크플로우가 상태 디셔너리에 없으면 초기화
        if workflow_id not in cls.states:
            cls.states[workflow_id] = {}
            log_debug(f"새 워크플로우 {workflow_id} 상태 초기화")
        
        # 파라미터 조합에 대한 키 생성
        state_key = f"{start_number}_{end_number}_{repeat_count}"
        
        # 리셋이 요청되었거나 해당 파라미터 조합에 대한 상태가 없는 경우
        if reset == "yes" or state_key not in cls.states[workflow_id]:
            if reset == "yes":
                log_debug(f"리셋 요청으로 상태 초기화: {state_key}")
            else:
                log_debug(f"상태 키가 없어 상태 초기화: {state_key}")
                
            # 새로운 상태 생성
            cls.states[workflow_id][state_key] = SequenceState(start_number, end_number, repeat_count)
        
        return cls.states[workflow_id][state_key]
    
    @classmethod
    def save_last_output(cls, workflow_id, state_key, value):
        """마지막 출력 값 저장"""
        if workflow_id == "none":
            return
            
        if workflow_id not in cls.last_outputs:
            cls.last_outputs[workflow_id] = {}
            
        cls.last_outputs[workflow_id][state_key] = value
        log_debug(f"워크플로우 {workflow_id}의 마지막 출력 값 저장: {state_key} = {value}")
    
    def generate_number(self, start_number, end_number, repeat_count, reset, unique_id="none", current_value=None):
        # 현재 워크플로우 ID 사용 (만약 IS_CHANGED에서 설정되었다면)
        workflow_id = getattr(NumberSequenceGenerator, "current_workflow_id", "default")
        log_debug(f"generate_number 호출: start={start_number}, end={end_number}, repeat={repeat_count}, reset={reset}, workflow_id={workflow_id}")
        
        # 범위 검증 - 시작 숫자가 종료 숫자보다 크면 값을 교환
        if start_number > end_number:
            log_debug(f"범위 교환: {start_number} > {end_number}, 교환 후: {end_number}, {start_number}")
            start_number, end_number = end_number, start_number
        
        # 워크플로우에 대한 상태 가져오기 (워크플로우 ID 사용)
        state = NumberSequenceGenerator.get_state_for_workflow(workflow_id, start_number, end_number, repeat_count, reset)
        
        # 현재 숫자 가져오기
        result = state.get_next()
        
        # 마지막 출력 값 저장
        state_key = f"{start_number}_{end_number}_{repeat_count}"
        NumberSequenceGenerator.save_last_output(workflow_id, state_key, result)
        
        # 파일에 상태 저장
        NumberSequenceGenerator.save_state_to_file()
        
        return (result,)

# 로그 파일 초기화 (모듈 로드 시 한 번만 실행)
if DEBUG_MODE:
    try:
        if os.path.exists(LOG_FILE):
            # 로그 파일이 너무 크면 초기화
            if os.path.getsize(LOG_FILE) > 1024 * 1024:  # 1MB 이상이면 초기화
                with open(LOG_FILE, "w", encoding="utf-8") as f:
                    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 로그 파일 초기화\n")
                    print(f"[NumberSequenceGenerator] 로그 파일 초기화: {LOG_FILE}")
        else:
            # 로그 파일이 없으면 생성
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 로그 파일 생성\n")
                print(f"[NumberSequenceGenerator] 로그 파일 생성: {LOG_FILE}")
            
    except Exception as e:
        print(f"[NumberSequenceGenerator] 초기화 오류: {e}")

log_debug("\n" + "="*50)
log_debug(f"NumberSequenceGenerator 모듈 로드됨: {time.strftime('%Y-%m-%d %H:%M:%S')}")
log_debug(f"로그 파일 경로: {LOG_FILE}")

NODE_CLASS_MAPPINGS = {
    "NumberSequenceGenerator": NumberSequenceGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NumberSequenceGenerator": "Number Sequence Generator"
}
