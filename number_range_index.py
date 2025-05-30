class NumberRangeIndex:
    """
    Number Range Index Node: Determines which range a number belongs to and returns the corresponding index.
    
    This node checks which range the input number belongs to among the specified boundary values and returns the index of that range.
    Up to 15 boundary values can be specified, and only non-zero values are treated as valid boundaries.
    The boundary values are automatically sorted to calculate the ranges.
    
    There are two methods for calculating ranges:
    1. L <= n < R: Range from lower bound (inclusive) to upper bound (exclusive)
    2. L < n <= R: Range from lower bound (exclusive) to upper bound (inclusive)
    
    The default_index parameter determines the starting point of the result value. The default is 0.
    For values that do not belong to any range, default_index is returned.
    For values that belong to a range, default_index + range index is returned.
    
    Usage examples:
    - With boundary values [10, 20, 30] and base_type "L <= n < R":
      - Input value 5 -> default_index (not in any range)
      - Input value 10 -> default_index + 0 (first range)
      - Input value 15 -> default_index + 0 (first range)
      - Input value 20 -> default_index + 1 (second range)
      - Input value 35 -> default_index + 2 (beyond the last range)
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "number": ("INT", {"default": 5}),
                "base_type": (["L <= n < R", "L < n <= R"], {"default": "L <= n < R"}),
                "value_1": ("INT", {"default": 1}),
                "value_2": ("INT", {"default": 10}),
                "value_3": ("INT", {"default": 20}),
                "value_4": ("INT", {"default": 30}),
                "value_5": ("INT", {"default": 40}),
                "value_6": ("INT", {"default": 50}),
                "value_7": ("INT", {"default": 60}),
                "value_8": ("INT", {"default": 70}),
                "value_9": ("INT", {"default": 80}),
                "value_10": ("INT", {"default": 90}),
                "value_11": ("INT", {"default": 100}),
                "value_12": ("INT", {"default": 110}),
                "value_13": ("INT", {"default": 120}),
                "value_14": ("INT", {"default": 130}),
                "value_15": ("INT", {"default": 140}),
                "default_index": ("INT", {"default": 0}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = "INDEX"
    FUNCTION = "get_range_index"
    CATEGORY = "Logic-Support"

    def get_range_index(self, number, base_type, 
                        value_1, value_2, value_3, value_4, value_5, 
                        value_6, value_7, value_8, value_9, value_10, 
                        value_11, value_12, value_13, value_14, value_15, 
                        default_index=0):
        # 경계값 목록 생성
        values = [value_1, value_2, value_3, value_4, value_5, 
                 value_6, value_7, value_8, value_9, value_10,
                 value_11, value_12, value_13, value_14, value_15]
        # 중복 제거 및 정렬
        # 0도 유효한 경계값으로 처리
        filtered_values = list(set(values))
        # 경계값가 없는 경우 처리
        if not filtered_values:
            return (default_index,)
        
        # 경계값 오름차순 정렬
        filtered_values.sort()
        
        # 기준 타입 확인 (L <= n < R 또는 L < n <= R)
        is_base_0 = base_type == "L <= n < R"
        
        # 범위 인덱스 계산
        range_index = default_index  # 기본값으로 초기화
        
        # 첫 번째 경계값보다 작은 경우
        if number < filtered_values[0]:
            return (default_index,)  # 어떤 범위에도 속하지 않음
        
        # 마지맅 경계값보다 큰 경우
        if number > filtered_values[-1]:
            # 마지맅 범위에 속함
            if is_base_0:
                return (default_index + len(filtered_values) - 1,)  # L <= n < R
            else:
                return (default_index + len(filtered_values),)  # L < n <= R
        
        # 경계값과 정확히 일치하는 경우 처리
        for i, val in enumerate(filtered_values):
            if number == val:
                if is_base_0 or i > 0:  # L <= n < R 또는 첫 번째가 아닌 경계값인 경우
                    return (default_index + i,)
                else:  # L < n <= R이고 첫 번째 경계값인 경우
                    return (default_index,)
        
        # 경계값 사이에 있는 경우
        for i in range(len(filtered_values) - 1):
            if is_base_0:  # L <= n < R
                if filtered_values[i] <= number < filtered_values[i+1]:
                    return (default_index + i,)
            else:  # L < n <= R
                if filtered_values[i] < number <= filtered_values[i+1]:
                    return (default_index + i+1,)
        
        # 어떤 범위에도 포함되지 않는 경우 (이 부분은 실행되지 않아야 함)
        return (default_index,)
    
    # 더 이상 필요하지 않음

NODE_CLASS_MAPPINGS = {
    "NumberRangeIndex": NumberRangeIndex
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NumberRangeIndex": "Number Range Index"
}
