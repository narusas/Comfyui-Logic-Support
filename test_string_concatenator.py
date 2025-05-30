import unittest
from string_concatenator import StringConcatenator

class TestStringConcatenator(unittest.TestCase):
    def setUp(self):
        self.node = StringConcatenator()
    
    def test_concatenate_all_strings(self):
        # 모든 문자열이 있는 경우
        result = self.node.concatenate(
            string1="안녕", string2="하세요", string3="반갑", string4="습니다", string5="테스트",
            string6="입니다", string7="문자열", string8="연결", string9="노드", string10="테스트",
            string11="중", string12="입니다", string13="잘", string14="작동", string15="하네요",
            separator_type="EMPTY"
        )
        self.assertEqual(result[0], "안녕하세요반갑습니다테스트입니다문자열연결노드테스트중입니다잘작동하네요", 
                         "모든 문자열이 EMPTY 구분자로 연결되어야 함")
    
    def test_concatenate_with_comma_separator(self):
        # 구분자가 있는 경우
        result = self.node.concatenate(
            string1="안녕", string2="하세요", string3="반갑", string4="습니다", string5="테스트",
            string6="입니다", string7="문자열", string8="연결", string9="노드", string10="테스트",
            string11="중", string12="입니다", string13="잘", string14="작동", string15="하네요",
            separator_type="COMMA"
        )
        self.assertEqual(result[0], "안녕,하세요,반갑,습니다,테스트,입니다,문자열,연결,노드,테스트,중,입니다,잘,작동,하네요", 
                         "모든 문자열이 쉼표로 구분되어 연결되어야 함")
    
    def test_concatenate_with_pipe_separator(self):
        # 일부 문자열이 비어있는 경우
        result = self.node.concatenate(
            string1="첫 번째", string2="", string3="세 번째", string4="", string5="다섯 번째",
            string6="", string7="일곱 번째", string8="", string9="아홉 번째", string10="",
            string11="열한 번째", string12="", string13="열셋 번째", string14="", string15="열다섯 번째",
            separator_type="PIPE"
        )
        self.assertEqual(result[0], "첫 번째|세 번째|다섯 번째|일곱 번째|아홉 번째|열한 번째|열셋 번째|열다섯 번째", 
                         "비어있지 않은 문자열만 파이프(|) 구분자로 연결되어야 함")
    
    def test_concatenate_only_required_strings(self):
        # 필수 문자열만 있는 경우
        result = self.node.concatenate(
            string1="첫 번째", string2="두 번째", string3="세 번째", string4="네 번째", string5="다섯 번째",
            separator_type="SPACE"
        )
        self.assertEqual(result[0], "첫 번째 두 번째 세 번째 네 번째 다섯 번째", 
                         "필수 문자열만 공백 구분자로 연결되어야 함")
    
    def test_concatenate_single_string(self):
        # 하나의 문자열만 있는 경우
        result = self.node.concatenate(
            string1="외로운 문자열", string2="", string3="", string4="", string5="",
            separator_type="COMMA"
        )
        self.assertEqual(result[0], "외로운 문자열", 
                         "하나의 문자열만 있는 경우 그대로 반환되어야 함")
    
    def test_concatenate_all_empty_strings(self):
        # 모든 문자열이 비어있는 경우
        result = self.node.concatenate(
            string1="", string2="", string3="", string4="", string5="",
            string6="", string7="", string8="", string9="", string10="",
            string11="", string12="", string13="", string14="", string15="",
            separator_type="COMMA"
        )
        self.assertEqual(result[0], "", 
                         "모든 문자열이 비어있는 경우 빈 문자열이 반환되어야 함")

if __name__ == "__main__":
    unittest.main()
