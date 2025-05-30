import unittest
from number_range_index import NumberRangeIndex

class TestNumberRangeIndex(unittest.TestCase):
    def setUp(self):
        self.node = NumberRangeIndex()
        
    def test_comprehensive_boundaries(self):
        # 경계값: 0, 10, 15, 20, 25, 30, 35, 40, 50, 60, 80
        # 이 테스트에서는 다양한 입력값에 대해 "L <= n < R" 모드에서 올바른 인덱스를 반환하는지 확인합니다.
        
        # 경계값 설정
        boundaries = [0, 10, 15, 20, 25, 30, 35, 40, 50, 60, 80]
        
        # 테스트 케이스: (입력값, 예상 인덱스)
        test_cases_base_0 = [
            (-5, 0),      # 첫 번째 경계값보다 작은 경우
            (0, 0),       # 첫 번째 경계값과 같은 경우
            (5, 0),       # 첫 번째와 두 번째 경계값 사이
            (10, 1),      # 두 번째 경계값과 같은 경우
            (12, 1),      # 두 번째와 세 번째 경계값 사이
            (15, 2),      # 세 번째 경계값과 같은 경우
            (18, 2),      # 세 번째와 네 번째 경계값 사이
            (20, 3),      # 네 번째 경계값과 같은 경우
            (22, 3),      # 네 번째와 다섯 번째 경계값 사이
            (25, 4),      # 다섯 번째 경계값과 같은 경우
            (27, 4),      # 다섯 번째와 여섯 번째 경계값 사이
            (30, 5),      # 여섯 번째 경계값과 같은 경우
            (32, 5),      # 여섯 번째와 일곱 번째 경계값 사이
            (35, 6),      # 일곱 번째 경계값과 같은 경우
            (38, 6),      # 일곱 번째와 여덟 번째 경계값 사이
            (40, 7),      # 여덟 번째 경계값과 같은 경우
            (45, 7),      # 여덟 번째와 아홉 번째 경계값 사이
            (50, 8),      # 아홉 번째 경계값과 같은 경우
            (55, 8),      # 아홉 번째와 열 번째 경계값 사이
            (60, 9),      # 열 번째 경계값과 같은 경우
            (70, 9),      # 열 번째와 열한 번째 경계값 사이
            (80, 10),     # 열한 번째 경계값과 같은 경우
            (100, 10),    # 마지막 경계값보다 큰 경우
        ]
        
        # "L <= n < R" 모드 테스트
        for number, expected_index in test_cases_base_0:
            result = self.node.get_range_index(
                number=number,
                base_type="L <= n < R",
                value_1=boundaries[0],
                value_2=boundaries[1],
                value_3=boundaries[2],
                value_4=boundaries[3],
                value_5=boundaries[4],
                value_6=boundaries[5],
                value_7=boundaries[6],
                value_8=boundaries[7],
                value_9=boundaries[8],
                value_10=boundaries[9],
                value_11=boundaries[10],
                value_12=0,
                value_13=0,
                value_14=0,
                value_15=0,
                default_index=0
            )
            self.assertEqual(result[0], expected_index, f"입력값 {number}에 대해 인덱스 {expected_index}가 예상되었지만 {result[0]}가 반환됨 (L <= n < R 모드)")
        
        # "L < n <= R" 모드 테스트
        test_cases_base_1 = [
            (-5, 0),     # 첫 번째 경계값보다 작은 경우 (범위에 속하지 않음)
            (0, 0),       # 첫 번째 경계값과 같은 경우 (첫 번째 범위에 속함)
            (5, 1),       # 첫 번째와 두 번째 경계값 사이 (두 번째 범위에 속함)
            (10, 1),      # 두 번째 경계값과 같은 경우 (두 번째 범위에 속함)
            (12, 2),      # 두 번째와 세 번째 경계값 사이 (세 번째 범위에 속함)
            (15, 2),      # 세 번째 경계값과 같은 경우 (세 번째 범위에 속함)
            (18, 3),      # 세 번째와 네 번째 경계값 사이 (네 번째 범위에 속함)
            (20, 3),      # 네 번째 경계값과 같은 경우 (네 번째 범위에 속함)
            (22, 4),      # 네 번째와 다섯 번째 경계값 사이 (다섯 번째 범위에 속함)
            (25, 4),      # 다섯 번째 경계값과 같은 경우 (다섯 번째 범위에 속함)
            (27, 5),      # 다섯 번째와 여섯 번째 경계값 사이 (여섯 번째 범위에 속함)
            (30, 5),      # 여섯 번째 경계값과 같은 경우 (여섯 번째 범위에 속함)
            (32, 6),      # 여섯 번째와 일곱 번째 경계값 사이 (일곱 번째 범위에 속함)
            (35, 6),      # 일곱 번째 경계값과 같은 경우 (일곱 번째 범위에 속함)
            (38, 7),      # 일곱 번째와 여덟 번째 경계값 사이 (여덟 번째 범위에 속함)
            (40, 7),      # 여덟 번째 경계값과 같은 경우 (여덟 번째 범위에 속함)
            (45, 8),      # 여덟 번째와 아홉 번째 경계값 사이 (아홉 번째 범위에 속함)
            (50, 8),      # 아홉 번째 경계값과 같은 경우 (아홉 번째 범위에 속함)
            (55, 9),      # 아홉 번째와 열 번째 경계값 사이 (열 번째 범위에 속함)
            (60, 9),      # 열 번째 경계값과 같은 경우 (열 번째 범위에 속함)
            (70, 10),     # 열 번째와 열한 번째 경계값 사이 (열한 번째 범위에 속함)
            (80, 10),     # 열한 번째 경계값과 같은 경우 (열한 번째 범위에 속함)
            (100, 11),    # 마지막 경계값보다 큰 경우 (마지막 범위 다음)
        ]
        
        for number, expected_index in test_cases_base_1:
            result = self.node.get_range_index(
                number=number,
                base_type="L < n <= R",
                value_1=boundaries[0],
                value_2=boundaries[1],
                value_3=boundaries[2],
                value_4=boundaries[3],
                value_5=boundaries[4],
                value_6=boundaries[5],
                value_7=boundaries[6],
                value_8=boundaries[7],
                value_9=boundaries[8],
                value_10=boundaries[9],
                value_11=boundaries[10],
                value_12=0,
                value_13=0,
                value_14=0,
                value_15=0,
                default_index=0
            )
            self.assertEqual(result[0], expected_index, f"입력값 {number}에 대해 인덱스 {expected_index}가 예상되었지만 {result[0]}가 반환됨 (L < n <= R 모드)")
    
    def test_base0_mode(self):
        # 테스트 케이스 1: 숫자 11, 경계값 [0, 10, 15, 20], "L <= n < R" 모드
        # 11은 10과 15 사이에 있으므로 인덱스 1이 반환되어야 함
        result = self.node.get_range_index(
            number=11,
            base_type="L <= n < R",
            value_1=0, value_2=10, value_3=15, value_4=20, value_5=30,
            value_6=0, value_7=0, value_8=0, value_9=0, value_10=0,
            value_11=0, value_12=0, value_13=0, value_14=0, value_15=0,
            default_index=0
        )
        self.assertEqual(result[0], 1, "11은 10과 15 사이에 있으므로 인덱스 1이 반환되어야 함")
        
        # 테스트 케이스 2: 숫자 5, 경계값 [0, 10, 15, 20], "L <= n < R" 모드
        # 5는 0과 10 사이에 있으므로 인덱스 0이 반환되어야 함
        result = self.node.get_range_index(
            number=5,
            base_type="L <= n < R",
            value_1=0, value_2=10, value_3=15, value_4=20, value_5=30,
            value_6=0, value_7=0, value_8=0, value_9=0, value_10=0,
            value_11=0, value_12=0, value_13=0, value_14=0, value_15=0,
            default_index=0
        )
        self.assertEqual(result[0], 0, "5는 0과 10 사이에 있으므로 인덱스 0이 반환되어야 함")
        
        # 테스트 케이스 3: 숫자 25, 경계값 [0, 10, 15, 20], "L <= n < R" 모드
        # 25는 20보다 크므로 마지막 인덱스 3이 반환되어야 함
        result = self.node.get_range_index(
            number=25,
            base_type="L <= n < R",
            value_1=0, value_2=10, value_3=15, value_4=20, value_5=30,
            value_6=0, value_7=0, value_8=0, value_9=0, value_10=0,
            value_11=0, value_12=0, value_13=0, value_14=0, value_15=0,
            default_index=0
        )
        self.assertEqual(result[0], 3, "25는 20보다 크므로 마지막 인덱스 3이 반환되어야 함")
    
    def test_base1_mode(self):
        # 테스트 케이스 4: 숫자 11, 경계값 [0, 10, 15, 20], "L < n <= R" 모드
        # 11은 10과 15 사이에 있으므로 인덱스 2가 반환되어야 함
        result = self.node.get_range_index(
            number=11,
            base_type="L < n <= R",
            value_1=0, value_2=10, value_3=15, value_4=20, value_5=30,
            value_6=0, value_7=0, value_8=0, value_9=0, value_10=0,
            value_11=0, value_12=0, value_13=0, value_14=0, value_15=0,
            default_index=0
        )
        self.assertEqual(result[0], 2, "11은 10과 15 사이에 있으므로 인덱스 2가 반환되어야 함")
        
        # 테스트 케이스 5: 숫자 -5, 경계값 [0, 10, 15, 20], "L < n <= R" 모드
        # -5는 0보다 작으므로 default_index가 반환되어야 함
        result = self.node.get_range_index(
            number=-5, 
            base_type="L < n <= R",
            value_1=0, value_2=10, value_3=15, value_4=20, 
            value_5=0, value_6=0, value_7=0, value_8=0, value_9=0, value_10=0,
            value_11=0, value_12=0, value_13=0, value_14=0, value_15=0,
            default_index=0
        )
        self.assertEqual(result[0], 0, "-5는 0보다 작으므로 default_index가 반환되어야 함")

if __name__ == "__main__":
    unittest.main()
