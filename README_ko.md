# ComfyUI Logic Support

ComfyUI 워크플로우 기능을 향상시키기 위한 로직 및 유틸리티 노드 모음입니다.

## 개요

ComfyUI Logic Support는 ComfyUI 워크플로우를 향상시키기 위한 다양한 로직 및 유틸리티 노드를 제공하는 커스텀 노드 확장입니다. 이 노드들을 통해 더 복잡한 조건부 로직, 문자열 조작 및 숫자 연산을 수행할 수 있습니다.

## 설치 방법

1. 이 저장소를 ComfyUI의 custom_nodes 디렉토리에 클론합니다:
   ```bash
   cd /path/to/ComfyUI/custom_nodes
   git clone https://github.com/yourusername/Comfyui-Logic-Support.git
   ```

2. ComfyUI를 재시작하거나, 이미 실행 중이라면 페이지를 새로고침합니다.

## 노드 설명

### NumberRangeIndex

입력된 숫자가 어떤 범위에 속하는지 확인하고 해당 범위의 인덱스를 출력합니다.

- **입력**:
  - `number`: 확인할 입력 숫자
  - `base_type`: 범위 계산 방식 ("L <= n < R" 또는 "L < n <= R")
  - `value_1`부터 `value_15`: 범위의 경계값
  - `default_index`: 결과의 시작 인덱스 (기본값: 0)

- **출력**:
  - `INDEX`: 숫자가 속한 범위의 인덱스

### BooleanIndexAdder

15개의 boolean 값 중 true인 첫 번째 값의 인덱스를 입력 숫자에 더합니다.

- **입력**:
  - `base_number`: 인덱스를 더할 기본 숫자
  - `bool1`부터 `bool15`: Boolean 입력값
  
- **출력**:
  - `NUMBER`: 인덱스를 기본 숫자에 더한 결과

### NumberConditionChecker

입력된 숫자가 지정된 범위 안에 들어오면 true, 아니면 false를 출력합니다.

- **입력**:
  - `lower_value`: 하한값
  - `lower_op`: 하한 연산자 ("NONE", "<", "<=")
  - `number`: 확인할 숫자
  - `upper_op`: 상한 연산자 ("NONE", "<", "<=")
  - `upper_value`: 상한값
  
- **출력**:
  - `BOOLEAN`: 숫자가 모든 조건을 만족하면 True, 그렇지 않으면 False

### StringConcatenator

최대 15개의 문자열을 입력받아 지정된 구분자로 연결하여 하나의 문자열로 출력합니다.

- **입력**:
  - `separator_type`: 구분자 유형 ("EMPTY", "COMMA", "SPACE", "PIPE")
  - `string1`부터 `string15`: 연결할 문자열
  
- **출력**:
  - `STRING`: 연결된 문자열

### StringSwitchByNumber

숫자 입력에 따라 해당 인덱스의 문자열을 출력합니다. 최대 15개의 문자열을 지원합니다.

- **입력**:
  - `number`: 출력할 문자열의 인덱스 (1부터 시작)
  - `string1`부터 `string15`: 사용 가능한 문자열
  
- **출력**:
  - `STRING`: 선택된 문자열

## 사용 예시

### NumberRangeIndex를 이용한 조건부 처리

```
[숫자 입력: 15] → [NumberRangeIndex] → [인덱스에 따른 추가 처리]
```

### StringConcatenator를 이용한 동적 텍스트 생성

```
[텍스트 입력 1: "안녕하세요"] → [StringConcatenator: SPACE] → [출력: "안녕하세요 세계"]
[텍스트 입력 2: "세계"] ↗
```

### BooleanIndexAdder를 이용한 조건부 로직

```
[기본 숫자: 10] → [BooleanIndexAdder] → [출력: 12]
[Boolean 입력 1: False] ↗
[Boolean 입력 2: True] ↗
```

## 라이센스

MIT License

## 기여하기

기여는 언제나 환영합니다! Pull Request를 제출해 주세요.
