import unittest
from number_range_index import NumberRangeIndex

class TestNumberRangeIndexBoundary(unittest.TestCase):
    def setUp(self):
        self.node = NumberRangeIndex()
    
    def test_boundary_values(self):
        # "L <= n < R" 모드에서 경계값 [1, 10, 15, 20]을 사용하여 다양한 입력값 테스트
        
        # 테스트 케이스: (입력값, 예상 인덱스)
        test_cases = [
            (0, -1),   # 첫 번째 경계값보다 작은 값 -> default_index (-1)
            (1, 0),    # 첫 번째 경계값과 같은 값 -> 0
            (5, 0),    # 첫 번째와 두 번째 경계값 사이 -> 0
            (9, 0),    # 두 번째 경계값 바로 전 -> 0
            (10, 1),   # 두 번째 경계값과 같은 값 -> 1
            (11, 1),   # 두 번째와 세 번째 경계값 사이 -> 1
            (14, 1),   # 세 번째 경계값 바로 전 -> 1
            (15, 2),   # 세 번째 경계값과 같은 값 -> 2
            (16, 2),   # 세 번째와 네 번째 경계값 사이 -> 2
            (19, 2),   # 네 번째 경계값 바로 전 -> 2
            (20, 3),   # 네 번째 경계값과 같은 값 -> 3
            (25, 3),   # 마지막 경계값보다 큰 값 -> 3
        ]
        
        # 각 테스트 케이스 실행
        for number, expected_index in test_cases:
            result = self.node.get_range_index(
                number=number, 
                base_type="L <= n < R",
                value_1=1, value_2=10, value_3=15, value_4=20, 
                value_5=0, value_6=0, value_7=0, value_8=0, value_9=0, value_10=0,
                value_11=0, value_12=0, value_13=0, value_14=0, value_15=0,
                default_index=-1
            )
            self.assertEqual(result[0], expected_index, 
                            f"입력값 {number}에 대해 인덱스 {expected_index}가 예상되었지만 {result[0]}가 반환됨")
            print(f"입력값 {number} -> 인덱스 {result[0]} (예상: {expected_index})")
    
    def test_boundary_values_with_index_1(self):
        # "L <= n < R" 모드에서 경계값 [1, 10, 15, 20]을 사용하고 첫 번째 값을 인덱스 1로 설정
        # 입력값 1~9는 인덱스 1이 나오고, 10부터는 인덱스 2가 나오는지 테스트
        
        # 테스트 케이스: (입력값, 예상 인덱스)
        test_cases = [
            (0, 1),    # 첫 번째 경계값보다 작은 값 -> default_index (1)
            (1, 2),    # 첫 번째 경계값과 같은 값 -> 1+1=2
            (5, 2),    # 첫 번째와 두 번째 경계값 사이 -> 1+1=2
            (9, 2),    # 두 번째 경계값 바로 전 -> 1+1=2
            (10, 3),   # 두 번째 경계값과 같은 값 -> 2+1=3
            (11, 3),   # 두 번째와 세 번째 경계값 사이 -> 2+1=3
            (14, 3),   # 세 번째 경계값 바로 전 -> 2+1=3
            (15, 4),   # 세 번째 경계값과 같은 값 -> 3+1=4
            (16, 4),   # 세 번째와 네 번째 경계값 사이 -> 3+1=4
            (19, 4),   # 네 번째 경계값 바로 전 -> 3+1=4
            (20, 5),   # 네 번째 경계값과 같은 값 -> 4+1=5
            (25, 5),   # 마지막 경계값보다 큰 값 -> 4+1=5
        ]
        
        # 각 테스트 케이스 실행
        for number, expected_index in test_cases:
            result = self.node.get_range_index(
                number=number, 
                base_type="L <= n < R",
                value_1=1, value_2=10, value_3=15, value_4=20, 
                value_5=0, value_6=0, value_7=0, value_8=0, value_9=0, value_10=0,
                value_11=0, value_12=0, value_13=0, value_14=0, value_15=0,
                default_index=1  # 기본 인덱스를 1로 설정
            )
            self.assertEqual(result[0], expected_index, 
                            f"입력값 {number}에 대해 인덱스 {expected_index}가 예상되었지만 {result[0]}가 반환됨")
            print(f"입력값 {number} -> 인덱스 {result[0]} (예상: {expected_index})")

if __name__ == "__main__":
    unittest.main()
