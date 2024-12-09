# AutoSorter
쓰레기를 재미있게 버림으로써 쓰레기 분리수거율을 높이고자 기획된 프로젝트입니다. /This is a project designed to increase the waste separation rate by having fun disposing of trash.

-How to use : 
시연 영상 참고(main.py 실행)

&nbsp;  


# 📃 프로젝트 정보

### 1. 제작기간
'24.07.05 ~ '24.09.30

### 2. 참여 인원
> |                    Name                    |  Position   |
> | :----------------------------------------: | :---------: |
> | [태현수](https://github.com/xohyver/) |   AI develop  |
> | 곽주은 |  Hardware  |

### 3.[역할] : AI 개발자
- 시스템 설계 및 구현 :
병렬 Thread 및 Opencv 이용 실시간 웹캠 시스템 구축, Pygame 이용 안내방송 송출 설계 
- 데이터 수집 및 모델 학습 :
모델 학습을 위한 이미지 수집 및 Yolov5 커스텀 트레이닝

### 4. 사용 기술
> Python3  
> Opencv  
> Yolov5  
> Torch

&nbsp;  

# 📊 Structure
- 카메라가 사람의 머리 상단을 촬영함
- Yolov5 이용 객체 인식으로 머리 개수 파악
- 설정해둔 임계값 이상의 머리 감지시 안내방송 mp3 재생으로 인원 통제 유도

&nbsp;  


# 🔑 핵심기능

### 1. 최대인원 설정
> 프로그램 실행 후 사용자는 카메라가 비추는 공간의 최대 인원 수를 입력합니다.

### 2. 실시간 웹캠 탐지
> Opencv 및 병렬 Thread로 실시간 객체탐지를 수행하여 인원을 파악합니다.

&nbsp;  


# 문제 해결
### 1. 촬영각 설계
> 처음 카메라 각도를 하방 45도로 설계했으나, 먼 거리의 객체 인식 정확도 저하 등의 문제로 카메라각을 천장에서 바닥을 바라보는 각도로 변경하여 정확도를 향상시킴

### 2. 모델 부적합
> 공개 모델을 사용한 결과 사람의 얼굴까지 한번에 인식하여 얼굴이 가려지면 정확도가 저하됨. 따라서 머리 상단만을 라벨링한 데이터를 수집하여 모델을 생성함

&nbsp;  

# 📕 기타 자료

### 시연영상
https://youtu.be/7izh1vydHPA?si=Bczb0R-mfdPYqIDC

&nbsp;  


# Tips
### 1.안내음성의 성별을 바꿀 수 있습니다. ttswomanEng/ttsmanEng에 따라 각각 남성, 여성의 음성을 담고 있습니다. main.py에서  play_announcement함수 내에 음성파일 경로를 수정하세요.  

### 2. 만약 웹캠을 연결하고싶다면 main.py는 line 13, mainGUI.py는 line 85에서 cap = cv2.VideoCapture(0)를 카메라 인덱스에 맞게 변경하세요.  

### 3.mainGui.py는 Pyqt5를 사용하여 GUI가 존재하는 버전이고, main.py는 GUI가 존재하지 않는 버전입니다.
