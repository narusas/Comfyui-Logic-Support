import unittest
from number_condition_checker import NumberConditionChecker

class TestNumberConditionChecker(unittest.TestCase):
    def setUp(self):
        self.node = NumberConditionChecker()
    
    def test_lower_bound_less_than(self):
        # 하한 조건: < (미만)
        # 테스트 케이스: 5 < 10 (참)
        result = self.node.check_condition(
            lower_value=5,
            lower_op="<",
            number=10,
            upper_op="NONE",
            upper_value=0
        )
        self.assertTrue(result[0], "5 < 10은 참이어야 함")
        
        # 테스트 케이스: 10 < 10 (거짓)
        result = self.node.check_condition(
            lower_value=10,
            lower_op="<",
            number=10,
            upper_op="NONE",
            upper_value=0
        )
        self.assertFalse(result[0], "10 < 10은 거짓이어야 함")
        
        # 테스트 케이스: 15 < 10 (거짓)
        result = self.node.check_condition(
            lower_value=15,
            lower_op="<",
            number=10,
            upper_op="NONE",
            upper_value=0
        )
        self.assertFalse(result[0], "15 < 10은 거짓이어야 함")
    
    def test_lower_bound_less_than_or_equal(self):
        # 하한 조건: <= (이하)
        # 테스트 케이스: 5 <= 10 (참)
        result = self.node.check_condition(
            lower_value=5,
            lower_op="<=",
            number=10,
            upper_op="NONE",
            upper_value=0
        )
        self.assertTrue(result[0], "5 <= 10은 참이어야 함")
        
        # 테스트 케이스: 10 <= 10 (참)
        result = self.node.check_condition(
            lower_value=10,
            lower_op="<=",
            number=10,
            upper_op="NONE",
            upper_value=0
        )
        self.assertTrue(result[0], "10 <= 10은 참이어야 함")
        
        # 테스트 케이스: 15 <= 10 (거짓)
        result = self.node.check_condition(
            lower_value=15,
            lower_op="<=",
            number=10,
            upper_op="NONE",
            upper_value=0
        )
        self.assertFalse(result[0], "15 <= 10은 거짓이어야 함")
    
    def test_upper_bound_less_than(self):
        # 상한 조건: < (미만)
        # 테스트 케이스: 5 < 10 (참)
        result = self.node.check_condition(
            lower_value=0,
            lower_op="NONE",
            number=5,
            upper_op="<",
            upper_value=10
        )
        self.assertTrue(result[0], "5 < 10은 참이어야 함")
        
        # 테스트 케이스: 10 < 10 (거짓)
        result = self.node.check_condition(
            lower_value=0,
            lower_op="NONE",
            number=10,
            upper_op="<",
            upper_value=10
        )
        self.assertFalse(result[0], "10 < 10은 거짓이어야 함")
        
        # 테스트 케이스: 15 < 10 (거짓)
        result = self.node.check_condition(
            lower_value=0,
            lower_op="NONE",
            number=15,
            upper_op="<",
            upper_value=10
        )
        self.assertFalse(result[0], "15 < 10은 거짓이어야 함")
    
    def test_upper_bound_less_than_or_equal(self):
        # 상한 조건: <= (이하)
        # 테스트 케이스: 5 <= 10 (참)
        result = self.node.check_condition(
            lower_value=0,
            lower_op="NONE",
            number=5,
            upper_op="<=",
            upper_value=10
        )
        self.assertTrue(result[0], "5 <= 10은 참이어야 함")
        
        # 테스트 케이스: 10 <= 10 (참)
        result = self.node.check_condition(
            lower_value=0,
            lower_op="NONE",
            number=10,
            upper_op="<=",
            upper_value=10
        )
        self.assertTrue(result[0], "10 <= 10은 참이어야 함")
        
        # 테스트 케이스: 15 <= 10 (거짓)
        result = self.node.check_condition(
            lower_value=0,
            lower_op="NONE",
            number=15,
            upper_op="<=",
            upper_value=10
        )
        self.assertFalse(result[0], "15 <= 10은 거짓이어야 함")
    
    def test_both_bounds(self):
        # 하한과 상한 조건 모두 사용
        # 테스트 케이스: 5 <= 7 < 10 (참)
        result = self.node.check_condition(
            lower_value=5,
            lower_op="<=",
            number=7,
            upper_op="<",
            upper_value=10
        )
        self.assertTrue(result[0], "5 <= 7 < 10은 참이어야 함")
        
        # 테스트 케이스: 5 <= 5 < 10 (참)
        result = self.node.check_condition(
            lower_value=5,
            lower_op="<=",
            number=5,
            upper_op="<",
            upper_value=10
        )
        self.assertTrue(result[0], "5 <= 5 < 10은 참이어야 함")
        
        # 테스트 케이스: 5 <= 10 < 10 (거짓, 상한 조건 위반)
        result = self.node.check_condition(
            lower_value=5,
            lower_op="<=",
            number=10,
            upper_op="<",
            upper_value=10
        )
        self.assertFalse(result[0], "5 <= 10 < 10은 거짓이어야 함 (상한 조건 위반)")
        
        # 테스트 케이스: 5 <= 4 < 10 (거짓, 하한 조건 위반)
        result = self.node.check_condition(
            lower_value=5,
            lower_op="<=",
            number=4,
            upper_op="<",
            upper_value=10
        )
        self.assertFalse(result[0], "5 <= 4 < 10은 거짓이어야 함 (하한 조건 위반)")
    
    def test_no_bounds(self):
        # 하한과 상한 조건 모두 NONE
        result = self.node.check_condition(
            lower_value=0,
            lower_op="NONE",
            number=100,
            upper_op="NONE",
            upper_value=0
        )
        self.assertTrue(result[0], "조건이 없을 때는 항상 참이어야 함")
    
    def test_negative_numbers(self):
        # 음수 테스트
        # 테스트 케이스: -10 <= -5 < 0 (참)
        result = self.node.check_condition(
            lower_value=-10,
            lower_op="<=",
            number=-5,
            upper_op="<",
            upper_value=0
        )
        self.assertTrue(result[0], "-10 <= -5 < 0은 참이어야 함")
        
        # 테스트 케이스: -10 <= -15 < 0 (거짓, 하한 조건 위반)
        result = self.node.check_condition(
            lower_value=-10,
            lower_op="<=",
            number=-15,
            upper_op="<",
            upper_value=0
        )
        self.assertFalse(result[0], "-10 <= -15 < 0은 거짓이어야 함 (하한 조건 위반)")

if __name__ == "__main__":
    unittest.main()
