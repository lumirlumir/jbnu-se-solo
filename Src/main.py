# Import
import unittest

# Func
def capitalize_first_letter(string):
    if type(string) == str and string != '' and 'a' <= string[0] and string[0] <= 'z':
        return string[0].upper() + string[1:]
    else:
        return string
    
# Test
class test_capitalize_first_letter(unittest.TestCase):
    # test_validation
    def test_validation_firstLetterLower(self): # 첫 번째 글자가 영문 소문자인 문자열
        self.assertEqual(capitalize_first_letter('a'), 'A') # 문자열 길이 1
        self.assertEqual(capitalize_first_letter('abc'), 'Abc') # 문자열 길이 2 이상
        self.assertEqual(capitalize_first_letter('aBc'), 'ABc')
        self.assertEqual(capitalize_first_letter('a~C'), 'A~C')
        self.assertEqual(capitalize_first_letter('a~3D'), 'A~3D')
        self.assertEqual(capitalize_first_letter('hello'), 'Hello')
        
    def test_validation_firstLetterUpper(self): # 첫 번째 글자가 영문 대문자인 문자열
        self.assertEqual(capitalize_first_letter('A'), 'A') # 문자열 길이 1
        self.assertEqual(capitalize_first_letter('Abc'), 'Abc') # 문자열 길이 2 이상
        self.assertEqual(capitalize_first_letter('ABc'), 'ABc')
        self.assertEqual(capitalize_first_letter('A~C'), 'A~C')
        self.assertEqual(capitalize_first_letter('A~3d'), 'A~3d')
        self.assertEqual(capitalize_first_letter('Hello'), 'Hello')

    def test_validation_firstLetterOthers(self): # 첫 번째 글자가 영문자 이외인 문자열
        self.assertEqual(capitalize_first_letter('!'), '!') # 문자열 길이 1
        self.assertEqual(capitalize_first_letter('1'), '1') # 문자열 길이 1
        self.assertEqual(capitalize_first_letter('!bc'), '!bc') # 문자열 길이 2 이상
        self.assertEqual(capitalize_first_letter('1Bc'), '1Bc')
        self.assertEqual(capitalize_first_letter('!~3'), '!~3')
        self.assertEqual(capitalize_first_letter('~B3d'), '~B3d')
        self.assertEqual(capitalize_first_letter('#ello'), '#ello')

    def test_validation_blank(self): # 공백 문자열 
        self.assertEqual(capitalize_first_letter(''), '') # 공백 길이 0
        self.assertEqual(capitalize_first_letter(' '), ' ') # 공백 길이 1
        self.assertEqual(capitalize_first_letter('  '), '  ') # 공백 길이 2 이상
    
    # test_defect
    def test_defect_integer(self): # 정수 자료형
        self.assertEqual(capitalize_first_letter(123), 123)
        self.assertEqual(capitalize_first_letter(0), 0)
        self.assertEqual(capitalize_first_letter(-123), -123)
    
    def test_defect_float(self): # 실수 자료형
        self.assertEqual(capitalize_first_letter(3.24), 3.24)
        self.assertEqual(capitalize_first_letter(0.00), 0.00)
        self.assertEqual(capitalize_first_letter(-3.24), -3.24)
        
    def test_defect_complex(self): # 복소수 자료형
        self.assertEqual(capitalize_first_letter(1j), 1j)
        
    def test_defect_boolean(self): # 불린 자료형
        self.assertEqual(capitalize_first_letter(True), True)
        self.assertEqual(capitalize_first_letter(False), False)
        
    def test_defect_list(self): # 리스트 자료형
        self.assertEqual(capitalize_first_letter([1, 2, 3]), [1, 2, 3])
        
    def test_defect_tuple(self): # 튜플 자료형
        self.assertEqual(capitalize_first_letter((1, 2, 3)), (1, 2, 3))
        
    def test_defect_dictionary(self): # 딕셔너리 자료형
        self.assertEqual(capitalize_first_letter({1: 1, 2: 2, 3: 3}), {1: 1, 2: 2, 3: 3})    
        
    def test_defect_set(self): # 집합 자료형
        self.assertEqual(capitalize_first_letter({1, 2, 3}), {1, 2, 3})

# Main
if __name__ == '__main__':
    unittest.main()