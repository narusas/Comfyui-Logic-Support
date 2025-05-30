import unittest
from number_sequence_generator import NumberSequenceGenerator

class TestNumberSequenceGenerator(unittest.TestCase):
    def setUp(self):
        # 각 테스트 전에 클래스 변수 초기화
        NumberSequenceGenerator.current_number = 1
        NumberSequenceGenerator.current_repeat = 1
        self.generator = NumberSequenceGenerator()
    
    def test_basic_sequence(self):
        """기본 시퀀스 생성 테스트 (1~3, 반복 1회)"""
        # 1, 2, 3, 1, 2, 3 순서로 생성되어야 함
        self.assertEqual(self.generator.generate_number(1, 3, 1)[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 1)[0], 2)
        self.assertEqual(self.generator.generate_number(1, 3, 1)[0], 3)
        self.assertEqual(self.generator.generate_number(1, 3, 1)[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 1)[0], 2)
        self.assertEqual(self.generator.generate_number(1, 3, 1)[0], 3)
    
    def test_repeated_sequence(self):
        """반복 시퀀스 생성 테스트 (1~3, 반복 2회)"""
        # 1, 1, 2, 2, 3, 3, 1, 1 순서로 생성되어야 함
        self.assertEqual(self.generator.generate_number(1, 3, 2)[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 2)[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 2)[0], 2)
        self.assertEqual(self.generator.generate_number(1, 3, 2)[0], 2)
        self.assertEqual(self.generator.generate_number(1, 3, 2)[0], 3)
        self.assertEqual(self.generator.generate_number(1, 3, 2)[0], 3)
        self.assertEqual(self.generator.generate_number(1, 3, 2)[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 2)[0], 1)
    
    def test_range_validation(self):
        """범위 검증 테스트 (시작 숫자가 종료 숫자보다 큰 경우)"""
        # 시작 숫자(10)가 종료 숫자(5)보다 크면 값이 교환되어야 함
        # 따라서 5, 6, 7, 8, 9, 10 순서로 생성되어야 함
        self.assertEqual(self.generator.generate_number(10, 5, 1)[0], 5)
        self.assertEqual(self.generator.generate_number(10, 5, 1)[0], 6)
        self.assertEqual(self.generator.generate_number(10, 5, 1)[0], 7)
        self.assertEqual(self.generator.generate_number(10, 5, 1)[0], 8)
        self.assertEqual(self.generator.generate_number(10, 5, 1)[0], 9)
        self.assertEqual(self.generator.generate_number(10, 5, 1)[0], 10)
        self.assertEqual(self.generator.generate_number(10, 5, 1)[0], 5)
    
    def test_change_range(self):
        """범위 변경 테스트"""
        # 처음에 1~3 범위 사용
        self.assertEqual(self.generator.generate_number(1, 3, 1)[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 1)[0], 2)
        
        # 범위를 5~7로 변경
        self.assertEqual(self.generator.generate_number(5, 7, 1)[0], 5)
        self.assertEqual(self.generator.generate_number(5, 7, 1)[0], 6)
        self.assertEqual(self.generator.generate_number(5, 7, 1)[0], 7)
        self.assertEqual(self.generator.generate_number(5, 7, 1)[0], 5)
    
    def test_change_repeat(self):
        """반복 횟수 변경 테스트"""
        # 처음에 반복 1회 사용
        self.assertEqual(self.generator.generate_number(1, 3, 1)[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 1)[0], 2)
        
        # 반복 횟수를 2회로 변경
        # 현재 숫자는 3이고, 반복 횟수는 1이므로 3이 한 번 더 출력되어야 함
        self.assertEqual(self.generator.generate_number(1, 3, 2)[0], 3)
        self.assertEqual(self.generator.generate_number(1, 3, 2)[0], 3)
        
        # 다음 숫자인 1이 2번 반복되어야 함
        self.assertEqual(self.generator.generate_number(1, 3, 2)[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 2)[0], 1)

if __name__ == '__main__':
    unittest.main()
