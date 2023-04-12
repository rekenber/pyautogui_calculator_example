import pygetwindow as gw
import pyautogui
import time

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

for test in tests:
    time.sleep(1)  # 계산 결과가 나올 때까지 대기
    a, op, b, result = test
    pyautogui.press('escape')
    pyautogui.typewrite(a)
    pyautogui.press(op)
    pyautogui.typewrite(b)
    pyautogui.press('enter')

    # 계산 결과를 얻을 수 없기 때문에 결과 확인을 수동으로 해야 함
    print(f"{a} {op} {b} = {result}")

# 계산기 종료
calculator.close()

# 참조
# https://github.com/jasonogayon/hw-win-calc-pyautogui/blob/master/CalculatorTests.py