import unittest
import pyautogui
import pygetwindow as gw
import time
from pytesseract import image_to_string
from calculator_ocr import get_calculator_result

class TestCalculatorOperations(unittest.TestCase):

    def setUp(self):
        # 계산기를 실행해 놓는다.
        # time.sleep(2)
        # pyautogui.press('win')
        # pyautogui.write('calc')
        # pyautogui.press('enter')
        # time.sleep(2)

        # 계산기 창을 찾음
        self.calculator = gw.getWindowsWithTitle('계산기')[0]

        # 계산기 창이 최소화되어 있다면 복원
        if self.calculator.isMinimized:
            self.calculator.restore()

        self.calculator.activate()
        self.calculator.moveTo(0, 0)        

    def tearDown(self):
        # self.calculator.close()
        # time.sleep(2)
        pass

    def test_addition(self):
        pyautogui.press('escape')
        pyautogui.write('1')
        pyautogui.press('+')
        pyautogui.write('2')
        pyautogui.press('enter')
        time.sleep(1)

        result = get_calculator_result(self.calculator)
        self.assertEqual(result, '3', "1 + 2 should equal 3")

    def test_subtraction(self):
        pyautogui.press('escape')
        pyautogui.write('4')
        pyautogui.press('-')
        pyautogui.write('2')
        pyautogui.press('enter')
        time.sleep(1)

        result = get_calculator_result(self.calculator)
        self.assertEqual(result, '2', "4 - 2 should equal 2")

    def test_multiplication(self):
        pyautogui.press('escape')
        pyautogui.write('2')
        pyautogui.press('*')
        pyautogui.write('3')
        pyautogui.press('enter')
        time.sleep(1)

        result = get_calculator_result(self.calculator)
        self.assertEqual(result, '6', "2 * 3 should equal 6")

    def test_division(self):
        pyautogui.press('escape')
        pyautogui.write('9')
        pyautogui.press('/')
        pyautogui.write('3')
        pyautogui.press('enter')
        time.sleep(1)

        result = get_calculator_result(self.calculator)
        self.assertEqual(result, '3', "9 / 3 should equal 3")

if __name__ == '__main__':
    unittest.main()
