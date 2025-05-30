import unittest
import os
import json
from number_sequence_generator import NumberSequenceGenerator, SequenceState

class TestNumberSequenceGenerator(unittest.TestCase):
    def setUp(self):
        # 각 테스트 전에 상태 초기화
        NumberSequenceGenerator.states = {}
        NumberSequenceGenerator.last_outputs = {}
        NumberSequenceGenerator.current_workflow_id = "test_workflow"
        
        # 상태 파일이 있으면 삭제
        if os.path.exists(NumberSequenceGenerator.STATE_FILE):
            os.remove(NumberSequenceGenerator.STATE_FILE)
            
        self.generator = NumberSequenceGenerator()
    
    def test_basic_sequence(self):
        """기본 시퀀스 생성 테스트 (1~3, 반복 1회)"""
        # 1, 2, 3, 1, 2, 3 순서로 생성되어야 함
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 2)
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 3)
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 2)
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 3)
    
    def test_repeated_sequence(self):
        """반복 시퀀스 생성 테스트 (1~3, 반복 2회)"""
        # 1, 1, 2, 2, 3, 3, 1, 1 순서로 생성되어야 함
        self.assertEqual(self.generator.generate_number(1, 3, 2, "no")[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 2, "no")[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 2, "no")[0], 2)
        self.assertEqual(self.generator.generate_number(1, 3, 2, "no")[0], 2)
        self.assertEqual(self.generator.generate_number(1, 3, 2, "no")[0], 3)
        self.assertEqual(self.generator.generate_number(1, 3, 2, "no")[0], 3)
        self.assertEqual(self.generator.generate_number(1, 3, 2, "no")[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 2, "no")[0], 1)
    
    def test_range_validation(self):
        """범위 검증 테스트 (시작 숫자가 종료 숫자보다 큰 경우)"""
        # 시작 숫자(10)가 종료 숫자(5)보다 크면 값이 교환되어야 함
        # 따라서 5, 6, 7, 8, 9, 10 순서로 생성되어야 함
        self.assertEqual(self.generator.generate_number(10, 5, 1, "no")[0], 5)
        self.assertEqual(self.generator.generate_number(10, 5, 1, "no")[0], 6)
        self.assertEqual(self.generator.generate_number(10, 5, 1, "no")[0], 7)
        self.assertEqual(self.generator.generate_number(10, 5, 1, "no")[0], 8)
        self.assertEqual(self.generator.generate_number(10, 5, 1, "no")[0], 9)
        self.assertEqual(self.generator.generate_number(10, 5, 1, "no")[0], 10)
        self.assertEqual(self.generator.generate_number(10, 5, 1, "no")[0], 5)
    
    def test_change_range(self):
        """범위 변경 테스트"""
        # 처음에 1~3 범위 사용
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 2)
        
        # 범위를 5~7로 변경 (새로운 범위이므로 새로운 상태가 생성됨)
        self.assertEqual(self.generator.generate_number(5, 7, 1, "no")[0], 5)
        self.assertEqual(self.generator.generate_number(5, 7, 1, "no")[0], 6)
        self.assertEqual(self.generator.generate_number(5, 7, 1, "no")[0], 7)
        self.assertEqual(self.generator.generate_number(5, 7, 1, "no")[0], 5)
        
        # 원래 범위(1~3)로 돌아가면 이전 상태가 유지되어야 함
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 3)  # 이전에 1, 2까지 진행했으므로 3이 나와야 함
    
    def test_change_repeat(self):
        """반복 횟수 변경 테스트"""
        # 처음에 반복 1회 사용
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 2)
        
        # 반복 횟수를 2회로 변경 (다른 파라미터 조합이므로 새로운 상태가 생성됨)
        self.assertEqual(self.generator.generate_number(1, 3, 2, "no")[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 2, "no")[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 2, "no")[0], 2)
        
        # 원래 반복 횟수(1회)로 돌아가면 이전 상태가 유지되어야 함
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 3)  # 이전에 1, 2까지 진행했으므로 3이 나와야 함

    def test_reset_feature(self):
        """리셋 기능 테스트"""
        # 시퀀스 시작
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 2)
        
        # 리셋 요청
        self.assertEqual(self.generator.generate_number(1, 3, 1, "yes")[0], 1)  # 리셋되어 다시 1부터 시작
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 2)
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 3)
        
        # 다시 리셋
        self.assertEqual(self.generator.generate_number(1, 3, 1, "yes")[0], 1)  # 다시 리셋
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 2)
    
    def test_state_persistence(self):
        """상태 유지 테스트"""
        # 서로 다른 인스턴스를 생성해도 상태는 클래스 변수에 저장되므로 유지되어야 함
        generator1 = NumberSequenceGenerator()
        generator2 = NumberSequenceGenerator()
        
        # generator1으로 시퀀스 시작
        self.assertEqual(generator1.generate_number(1, 3, 1, "no")[0], 1)
        self.assertEqual(generator1.generate_number(1, 3, 1, "no")[0], 2)
        
        # generator2로 같은 파라미터 사용 시 이어서 진행되어야 함
        self.assertEqual(generator2.generate_number(1, 3, 1, "no")[0], 3)
        self.assertEqual(generator2.generate_number(1, 3, 1, "no")[0], 1)
        
        # generator1으로 다시 호출해도 상태가 유지되어야 함
        self.assertEqual(generator1.generate_number(1, 3, 1, "no")[0], 2)

    def test_file_persistence(self):
        """파일 기반 상태 저장 테스트"""
        # 첫 번째 시퀀스 생성
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 2)
        
        # 상태 파일이 생성되었는지 확인
        self.assertTrue(os.path.exists(NumberSequenceGenerator.STATE_FILE))
        
        # 상태 디셔너리 초기화
        NumberSequenceGenerator.states = {}
        NumberSequenceGenerator.last_outputs = {}
        
        # 파일에서 상태 로드
        NumberSequenceGenerator.load_state_from_file()
        
        # 상태가 유지되어야 함
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 3)  # 이전에 1, 2까지 생성했으므로 3이 나와야 함
    
    def test_workflow_isolation(self):
        """워크플로우 분리 테스트"""
        # 첫 번째 워크플로우
        NumberSequenceGenerator.current_workflow_id = "workflow1"
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 1)
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 2)
        
        # 두 번째 워크플로우 (도입)
        NumberSequenceGenerator.current_workflow_id = "workflow2"
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 1)  # 다른 워크플로우이므로 1부터 시작
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 2)
        
        # 첫 번째 워크플로우로 돌아가면 이전 상태가 유지되어야 함
        NumberSequenceGenerator.current_workflow_id = "workflow1"
        self.assertEqual(self.generator.generate_number(1, 3, 1, "no")[0], 3)  # 이전에 1, 2까지 생성했으므로 3이 나와야 함

if __name__ == '__main__':
    unittest.main()
