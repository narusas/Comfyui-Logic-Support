import unittest
from boolean_index_adder import BooleanIndexAdder

class TestBooleanIndexAdder(unittest.TestCase):
    def setUp(self):
        self.node = BooleanIndexAdder()
    
    def test_no_true_values(self):
        # 모든 boolean 값이 False인 경우, base_number가 그대로 반환되어야 함
        result = self.node.add_index(
            base_number=10,
            bool1=False, bool2=False, bool3=False, bool4=False, bool5=False,
            bool6=False, bool7=False, bool8=False, bool9=False, bool10=False,
            bool11=False, bool12=False, bool13=False, bool14=False, bool15=False
        )
        self.assertEqual(result[0], 10, "모든 값이 False일 때 base_number가 그대로 반환되어야 함")
    
    def test_first_true_value(self):
        # 첫 번째 값이 True인 경우, base_number + 1이 반환되어야 함
        result = self.node.add_index(
            base_number=10,
            bool1=True, bool2=False, bool3=False, bool4=False, bool5=False,
            bool6=False, bool7=False, bool8=False, bool9=False, bool10=False,
            bool11=False, bool12=False, bool13=False, bool14=False, bool15=False
        )
        self.assertEqual(result[0], 11, "첫 번째 값이 True일 때 base_number + 1이 반환되어야 함")
    
    def test_middle_true_value(self):
        # 중간 값이 True인 경우, base_number + 해당 인덱스가 반환되어야 함
        result = self.node.add_index(
            base_number=10,
            bool1=False, bool2=False, bool3=False, bool4=False, bool5=False,
            bool6=False, bool7=True, bool8=False, bool9=False, bool10=False,
            bool11=False, bool12=False, bool13=False, bool14=False, bool15=False
        )
        self.assertEqual(result[0], 17, "7번째 값이 True일 때 base_number + 7이 반환되어야 함")
    
    def test_last_true_value(self):
        # 마지막 값이 True인 경우, base_number + 15가 반환되어야 함
        result = self.node.add_index(
            base_number=10,
            bool1=False, bool2=False, bool3=False, bool4=False, bool5=False,
            bool6=False, bool7=False, bool8=False, bool9=False, bool10=False,
            bool11=False, bool12=False, bool13=False, bool14=False, bool15=True
        )
        self.assertEqual(result[0], 25, "15번째 값이 True일 때 base_number + 15가 반환되어야 함")
    
    def test_multiple_true_values(self):
        # 여러 값이 True인 경우, 첫 번째 True 값의 인덱스가 사용되어야 함
        result = self.node.add_index(
            base_number=10,
            bool1=False, bool2=False, bool3=True, bool4=False, bool5=True,
            bool6=False, bool7=True, bool8=False, bool9=True, bool10=False,
            bool11=True, bool12=False, bool13=True, bool14=False, bool15=True
        )
        self.assertEqual(result[0], 13, "여러 값이 True일 때 첫 번째 True 값(3번째)의 인덱스가 사용되어야 함")
    
    def test_negative_base_number(self):
        # base_number가 음수인 경우
        result = self.node.add_index(
            base_number=-10,
            bool1=False, bool2=False, bool3=False, bool4=True, bool5=False,
            bool6=False, bool7=False, bool8=False, bool9=False, bool10=False,
            bool11=False, bool12=False, bool13=False, bool14=False, bool15=False
        )
        self.assertEqual(result[0], -6, "base_number가 -10이고 4번째 값이 True일 때 -10 + 4 = -6이 반환되어야 함")
    
    def test_added_boolean_values(self):
        # 추가된 boolean 값(11-15)이 제대로 작동하는지 테스트
        result = self.node.add_index(
            base_number=5,
            bool1=False, bool2=False, bool3=False, bool4=False, bool5=False,
            bool6=False, bool7=False, bool8=False, bool9=False, bool10=False,
            bool11=False, bool12=True, bool13=False, bool14=False, bool15=False
        )
        self.assertEqual(result[0], 17, "12번째 값이 True일 때 base_number + 12 = 5 + 12 = 17이 반환되어야 함")

if __name__ == "__main__":
    unittest.main()
