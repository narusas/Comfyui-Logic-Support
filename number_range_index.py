class NumberRangeIndex:
    """
    숫자 범위 인덱스 노드: 입력된 숫자가 어떤 범위에 속하는지 확인하고 해당 범위의 인덱스를 출력합니다.
    숫자 범위는 자동으로 계산되며, 범위의 수는 입력된 경계값의 수에 따라 결정됩니다.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "number": ("INT", {"default": 5}),
                "base_type": (["base 0", "base 1"], {"default": "base 0"}),
                "value_1": ("INT", {"default": 0}),
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
                "default_index": ("INT", {"default": -1}),
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
                        default_index):
        # 경계값들을 리스트로 정리
        values = [value_1, value_2, value_3, value_4, value_5, 
                 value_6, value_7, value_8, value_9, value_10,
                 value_11, value_12, value_13, value_14, value_15]
        
        # 유효한 경계값만 필터링 (0이 아닌 값만 포함)
        filtered_values = [v for v in values if v != 0]
        
        # 경계값이 없으면 기본 인덱스 반환
        if not filtered_values:
            return (default_index,)
        
        # 경계값 정렬
        filtered_values.sort()
        
        # base_type에 따라 범위 체크 방식 결정
        is_base_0 = base_type == "base 0"
        
        # 마지막 경계값보다 크면 마지막 인덱스 반환
        if number >= filtered_values[-1]:
            if is_base_0:
                return (len(filtered_values) - 1,)
            else:
                return (len(filtered_values),)
        
        # 각 범위 체크
        for i in range(len(filtered_values) - 1):
            # 현재 경계값과 다음 경계값 사이에 있는지 확인
            if is_base_0:
                # base 0: value_i <= number < value_i+1
                if filtered_values[i] <= number < filtered_values[i+1]:
                    return (i,)
            else:
                # base 1: value_i < number <= value_i+1
                if filtered_values[i] < number <= filtered_values[i+1]:
                    return (i+1,)
        
        # 첫 번째 경계값보다 작은 경우
        if number < filtered_values[0]:
            if is_base_0:
                return (0,)  # base 0에서는 처음 범위에 포함
            else:
                return (default_index,)  # base 1에서는 어떤 범위에도 포함되지 않음
        
        # 어떤 범위에도 속하지 않으면 기본 인덱스 반환
        return (default_index,)
    
    # 더 이상 필요하지 않음

NODE_CLASS_MAPPINGS = {
    "NumberRangeIndex": NumberRangeIndex
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NumberRangeIndex": "Number Range Index"
}
