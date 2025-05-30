import unittest
from number_range_index import NumberRangeIndex

class TestNumberRangeIndexIssue(unittest.TestCase):
    def setUp(self):
        self.node = NumberRangeIndex()
    
    def test_specific_case(self):
        # 테스트 케이스: 숫자 11, 경계값 [1, 10, 15, 20], "L <= n < R" 모드, default_index=0
        result = self.node.get_range_index(
            number=11, 
            base_type="L <= n < R",
            value_1=1, value_2=10, value_3=15, value_4=20, 
            value_5=0, value_6=0, value_7=0, value_8=0, value_9=0, value_10=0,
            value_11=0, value_12=0, value_13=0, value_14=0, value_15=0,
            default_index=0
        )
        print(f"결과 (default_index=0): {result[0]}")
        
        # 테스트 케이스: 숫자 11, 경계값 [1, 10, 15, 20], "L <= n < R" 모드, default_index=1
        result = self.node.get_range_index(
            number=11, 
            base_type="L <= n < R",
            value_1=1, value_2=10, value_3=15, value_4=20, 
            value_5=0, value_6=0, value_7=0, value_8=0, value_9=0, value_10=0,
            value_11=0, value_12=0, value_13=0, value_14=0, value_15=0,
            default_index=1
        )
        print(f"결과 (default_index=1): {result[0]}")
        
        # 디버깅을 위한 코드 추가
        # 경계값 목록 확인
        values = [1, 10, 15, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        filtered_values = [v for v in values if v != 0]
        filtered_values.sort()
        print(f"필터링된 경계값: {filtered_values}")
        
        # 11이 어느 범위에 속하는지 확인
        for i in range(len(filtered_values) - 1):
            if filtered_values[i] <= 11 < filtered_values[i+1]:
                print(f"11은 {filtered_values[i]}와 {filtered_values[i+1]} 사이에 있음 (인덱스 {i})")
                print(f"원래 값 목록에서의 인덱스: {values.index(filtered_values[i])}")

if __name__ == "__main__":
    unittest.main()
