import unittest
from number_range_index import NumberRangeIndex

class TestNumberRangeIndexDebug(unittest.TestCase):
    def setUp(self):
        self.node = NumberRangeIndex()
    
    def test_debug_values(self):
        """
        디버깅용 테스트: 다양한 입력값에 대한 결과를 출력합니다.
        """
        # 테스트 케이스: (입력값, 경계값 목록, 기본 인덱스)
        test_cases = [
            # 기본 인덱스 = -1 (기본값)
            (0, [1, 10, 15, 20], -1),
            (1, [1, 10, 15, 20], -1),
            (5, [1, 10, 15, 20], -1),
            (10, [1, 10, 15, 20], -1),
            (15, [1, 10, 15, 20], -1),
            (20, [1, 10, 15, 20], -1),
            (25, [1, 10, 15, 20], -1),
            
            # 기본 인덱스 = 1
            (0, [1, 10, 15, 20], 1),
            (1, [1, 10, 15, 20], 1),
            (5, [1, 10, 15, 20], 1),
            (10, [1, 10, 15, 20], 1),
            (15, [1, 10, 15, 20], 1),
            (20, [1, 10, 15, 20], 1),
            (25, [1, 10, 15, 20], 1),
        ]
        
        print("\n==== L <= n < R 모드 테스트 ====")
        for number, values, default_index in test_cases:
            result = self.node.get_range_index(
                number=number, 
                base_type="L <= n < R",
                value_1=values[0], value_2=values[1], value_3=values[2], value_4=values[3], 
                value_5=0, value_6=0, value_7=0, value_8=0, value_9=0, value_10=0,
                value_11=0, value_12=0, value_13=0, value_14=0, value_15=0,
                default_index=default_index
            )
            print(f"입력값: {number}, 경계값: {values}, 기본 인덱스: {default_index} => 결과: {result[0]}")

if __name__ == "__main__":
    unittest.main()
