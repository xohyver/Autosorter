# AutoSorter
쓰레기를 재미있게 버림으로써 쓰레기 분리수거율을 높이고자 기획된 프로젝트입니다. /This is a project designed to increase the waste separation rate by having fun disposing of trash.

-How to use : 
Tips 1 참고(main.py 실행)

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
Opencv와 Yolov5를 활용하여 실시간 객체 탐지 시스템 구축함.\n
인식된 객체의 클래스에 따라 아두이노에 신호를 전송하여 360도 서보모터와 기어를 통해 쓰레기 분류를 위한 동작 실행. 
또한 실제 설치를 위해 공간을 적게 차지하며 객체탐지를 수행할 수 있도록 미니 pc인 Intel nuc를 쓰레기통 내부에 탑재함.

- 데이터 수집 및 모델 학습 :
교내 매점 환경 특성 상 시중에 드문 물품들이 많고, 판매되는 물품의 종류가 어느정도 정해져있음. 
따라서 대부분의 쓰레기에 높은 정확도를 보일 수 있도록 직접 쓰레기 이미지를 수집하기로 함.

### 4. 사용 기술
> Python3  
> Opencv  
> Yolov5  
> Torch
> Serial
> Arduino

&nbsp;  

# 📊 Structure
- 카메라가 쓰레기통 내부를 촬영
- Yolov5를 통한 객체인식으로 쓰레기의 클래스 감지
- 감지된 클래스 넘버에 따라 아두이노에 시리얼 통신을 통해 코드 전송, 각 코드에 따라 서보모터를 작동
- 서보모터에 장착된 기어와 챔버에 달린 레일이 기어와 맞물려 좌우로 움직이며 쓰레기를 분류함(내부 모터 동작행

&nbsp;  


# 문제 해결
### 1. CNN 성능 저하
> 처음 설계는 CNN을 통한 이미지 분류 알고리즘을 계획했으나, 데이터를 수집하여 학습한 결과 정확도가 저조하고, 모델의 구조를 수차례 변경했음에도 70%를 넘지 못함. 
이를 해결하기위해 관련 도서와 인터넷을 탐색한 결과 쓰레기 분류 목적인 CNN 알고리즘 학습에 2000장의 이미지는 너무 적다는 결론을 도출함. 2인 팀 프로젝트였기에 더 많은 데이터 수집은 어렵다고 판단하여, 객체탐지알고리즘을 통해 이미지 분류와 같은 효과를 얻고자 함. Yolov5를 통해 pretrained 된 모델을 전이학습하여, 적은 데이터로 0.986의 정확도의 모델을 생성함.

### 2. 모터 동작 중 객체탐지 수행 문제
> 모터가 동작 중 객체탐지가 수행되어 카메라가 학습된 환경과 완전히 다른 환경에 놓이게 되고, 객체 탐지 오류를 일으킴. 따라서 카메라가 직접적으로 비추는 챔버가 우선적으로 복귀하도록 하고, time 라이브러리와 if문을 통해 객체 인식 시 10초간 프로그램을 일시정지 시켜 문제를 해결함.


### 3. 서보모터 전력 부족
> 챔버를 톱니바퀴를 통해 서보모터로 이동시킬 때, 강한 토크를 위한 15v전압이 필요함. 따라서 아두이노에 외부 전력선을 연결하여 모터 출력 문제를 해결함.

&nbsp;  

# 📕 기타 자료
### 내부구조
공간을 적게 차지하며 객체탐지를 수행할 수 있도록 미니 pc인 Intel nuc를 쓰레기통 내부에 탑재함.
![KakaoTalk_20241210_110105790](https://github.com/user-attachments/assets/78c23b17-984b-422b-8163-783b4ab2c853)

### 내부 모터 동작 영상
모터에 연결된 기어와 챔버의 레일이 맞물려 돌아가도록 설계함.
https://youtube.com/shorts/era5PjpsWZY?feature=share

### 최종 시연영상
[https://youtu.be/7izh1vydHPA?si=Bczb0R-mfdPYqIDC](https://youtu.be/nBscDK_WJRA)

&nbsp;  


# Tips
### 1.fincode.ino에서 모터 핀번호를 지정하고 아두이노에 업로드한 후, main.py의 line 11에서 모델 경로 변경 및 line 17의 아두이노가 연결된 포트 번호를 지정한 다 실행하여 사용할 수 있습니다.  

### 2. 만약 웹캠을 연결하고싶다면 main.py는 line 13, mainGUI.py는 line 85에서 cap = cv2.VideoCapture(0)를 카메라 인덱스에 맞게 변경하세요.  


