# PyAutoGUI를 사용한 계산기 사용 예시

PyAutoGUI, PyGetWindow, OpenCV 및 pytesseract를 사용하여 계산기 애플리케이션의 키보드 입력 및 결과 인식을 처리합니다.

## 설치방법

1. 저장소를 클론(clone)하거나 다운로드하세요.

2. 프로젝트 디렉토리로 이동한 후, 가상 환경(virtual environment)을 생성하고 활성화합니다.

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
source .venv/bin/activate  # macOS, Linux
```

3. 필요한 라이브러리를 설치합니다.
```bash
pip install -r requirements.txt
```

4. pytesseract를 사용하기 위해 Tesseract OCR을 설치하고 시스템 환경 변수 PATH에 Tesseract 설치 디렉토리의 'bin' 폴더를 추가합니다.

5. 이제 프로젝트를 실행할 준비가 되었습니다. 예제 코드를 실행하려면 다음 명령어를 사용하세요.
```bash
python calculator_ocr.py
```