import unittest
from switch_by_number import StringSwitchByNumber

class TestStringSwitchByNumber(unittest.TestCase):
    def setUp(self):
        self.node = StringSwitchByNumber()
    
    def test_valid_number_selection(self):
        # 유효한 범위 내의 숫자로 문자열 선택 테스트
        result = self.node.switch(
            number=3,
            string1="첫 번째", string2="두 번째", string3="세 번째", string4="네 번째", string5="다섯 번째",
            string6="여섯 번째", string7="일곱 번째", string8="여덟 번째", string9="아홉 번째", string10="열 번째",
            string11="열한 번째", string12="열두 번째", string13="열셋 번째", string14="열넷 번째", string15="열다섯 번째"
        )
        self.assertEqual(result[0], "세 번째", "숫자 3을 입력했을 때 세 번째 문자열이 반환되어야 함")
    
    def test_out_of_range_low(self):
        # 범위보다 작은 숫자 입력 시 기본값(1) 사용 테스트
        result = self.node.switch(
            number=0,  # 범위 밖(1보다 작음)
            string1="첫 번째", string2="두 번째", string3="세 번째", string4="네 번째", string5="다섯 번째",
            string6="여섯 번째", string7="일곱 번째", string8="여덟 번째", string9="아홉 번째", string10="열 번째",
            string11="열한 번째", string12="열두 번째", string13="열셋 번째", string14="열넷 번째", string15="열다섯 번째"
        )
        self.assertEqual(result[0], "첫 번째", "범위 밖 숫자(0)를 입력했을 때 기본값(1)에 해당하는 첫 번째 문자열이 반환되어야 함")
    
    def test_out_of_range_high(self):
        # 범위보다 큰 숫자 입력 시 기본값(1) 사용 테스트
        result = self.node.switch(
            number=20,  # 범위 밖(15보다 큼)
            string1="첫 번째", string2="두 번째", string3="세 번째", string4="네 번째", string5="다섯 번째",
            string6="여섯 번째", string7="일곱 번째", string8="여덟 번째", string9="아홉 번째", string10="열 번째",
            string11="열한 번째", string12="열두 번째", string13="열셋 번째", string14="열넷 번째", string15="열다섯 번째"
        )
        self.assertEqual(result[0], "첫 번째", "범위 밖 숫자(20)를 입력했을 때 기본값(1)에 해당하는 첫 번째 문자열이 반환되어야 함")
    
    def test_first_string(self):
        # 첫 번째 문자열 선택 테스트
        result = self.node.switch(
            number=1,
            string1="첫 번째", string2="두 번째", string3="세 번째", string4="네 번째", string5="다섯 번째",
            string6="여섯 번째", string7="일곱 번째", string8="여덟 번째", string9="아홉 번째", string10="열 번째",
            string11="열한 번째", string12="열두 번째", string13="열셋 번째", string14="열넷 번째", string15="열다섯 번째"
        )
        self.assertEqual(result[0], "첫 번째", "숫자 1을 입력했을 때 첫 번째 문자열이 반환되어야 함")
    
    def test_last_string(self):
        # 마지막(15번째) 문자열 선택 테스트
        result = self.node.switch(
            number=15,
            string1="첫 번째", string2="두 번째", string3="세 번째", string4="네 번째", string5="다섯 번째",
            string6="여섯 번째", string7="일곱 번째", string8="여덟 번째", string9="아홉 번째", string10="열 번째",
            string11="열한 번째", string12="열두 번째", string13="열셋 번째", string14="열넷 번째", string15="열다섯 번째"
        )
        self.assertEqual(result[0], "열다섯 번째", "숫자 15를 입력했을 때 열다섯 번째 문자열이 반환되어야 함")
    
    def test_added_strings(self):
        # 추가된 문자열(11-15) 선택 테스트
        test_cases = [
            (11, "열한 번째"),
            (12, "열두 번째"),
            (13, "열셋 번째"),
            (14, "열넷 번째"),
            (15, "열다섯 번째")
        ]
        
        for number, expected in test_cases:
            result = self.node.switch(
                number=number,
                string1="첫 번째", string2="두 번째", string3="세 번째", string4="네 번째", string5="다섯 번째",
                string6="여섯 번째", string7="일곱 번째", string8="여덟 번째", string9="아홉 번째", string10="열 번째",
                string11="열한 번째", string12="열두 번째", string13="열셋 번째", string14="열넷 번째", string15="열다섯 번째"
            )
            self.assertEqual(result[0], expected, f"숫자 {number}를 입력했을 때 {expected}가 반환되어야 함")
    
    def test_empty_strings(self):
        # 빈 문자열 처리 테스트
        result = self.node.switch(
            number=5,
            string1="", string2="", string3="", string4="", string5="비어있지 않은 문자열",
            string6="", string7="", string8="", string9="", string10="",
            string11="", string12="", string13="", string14="", string15=""
        )
        self.assertEqual(result[0], "비어있지 않은 문자열", "숫자 5를 입력했을 때 다섯 번째 문자열이 반환되어야 함")

if __name__ == "__main__":
    unittest.main()
