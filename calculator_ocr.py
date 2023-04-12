import cv2
import pytesseract
import pygetwindow as gw
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'  # Tesseract 실행 파일 경로

def get_calculator_result(calculator_window, show=False):
    x, y, width, height = calculator_window.left, calculator_window.top, calculator_window.width, calculator_window.height
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save('calculator_screenshot.png')

    img = cv2.imread('calculator_screenshot.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    start_row = 110
    end_row   = 175
    start_col =  10
    end_col   = 385

    result_area = gray[start_row:end_row, start_col:end_col]  # 계산기 결과 영역 (화면 해상도와 계산기 크기에 따라 변경해야 할 수 있음)

    # 영역을 원본 이미지에 표시
    cv2.rectangle(img, (start_col, start_row), (end_col, end_row), (0, 255, 0), 2)

    # 표시한 이미지 저장 및 출력
    cv2.imwrite('calculator_screenshot_with_area.png', img)
    if show: cv2.imshow('Result Area', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

    result_text = pytesseract.image_to_string(result_area, lang='eng', config='--psm 6').strip()

    return result_text

if __name__ == '__main__':
    # 계산기 애플리케이션 실행
    pyautogui.press('win')
    pyautogui.write('calc')
    pyautogui.press('enter')
    time.sleep(2)

    # 계산기 창을 찾음
    calculator = gw.getWindowsWithTitle('계산기')[0]

    # 계산기 창이 최소화되어 있다면 복원
    if calculator.isMinimized:
        calculator.restore()

    # 계산기 창을 활성화하고 조작하기 쉽게 위치 이동
    #calculator.activate()
    calculator.moveTo(0, 0)

    # 사칙연산 테스트
    tests = [
        ('1', '+', '2', '3'),
        ('4', '-', '2', '2'),
        ('2', '*', '3', '6'),
        ('9', '/', '3', '3')
    ]

    time.sleep(3)

    # 결과 확인
    for test in tests:
        time.sleep(1)  # 계산 결과가 나올 때까지 대기
        a, op, b, result = test
        pyautogui.press('escape')
        pyautogui.typewrite(a)
        pyautogui.press(op)
        pyautogui.typewrite(b)
        pyautogui.press('enter')

        recognized_result = get_calculator_result(calculator, True).strip()
        print(f"{a} {op} {b} = {result}, 인식된 결과: {recognized_result}")

    # 계산기 종료
    calculator.close()