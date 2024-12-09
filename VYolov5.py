import cv2
import torch
import numpy as np   #작동명령 중복을 막아야함. 그리고 모델 성능 ㅈ구려서 다시 만들어야할 듯 0이 병 1이 캔 2가 페트
import serial
import time
import pathlib

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path="C:/ai/AdditionalTask/ProjectVolunteer3/models/nongray.pt")

# 웹캠 설정
cap = cv2.VideoCapture(0)

# 시리얼 포트 설정
arduino = serial.Serial('COM7', 9600)



# 시리얼 전송 함수
def send_command(command):
    arduino.write(str(command).encode())

# 시간 추적을 위한 변수
last_capture_time = time.time()

# 실시간 웹캠 처리 루프
try:
    while True:
        current_time = time.time()
        elapsed_time = current_time - last_capture_time

        if elapsed_time >= 10:  # 5초마다 캡처
            ret, frame = cap.read()  # 프레임 캡처
            if not ret:
                break
            frame_rgb = frame[:, :, ::-1]  # BGR -> RGB 변환
            results = model(frame_rgb)  # 객체 탐지 수행

            for *box, conf, cls in results.xyxy[0]:  # 탐지 결과 처리
                # box 좌표 가져오기
                x1, y1, x2, y2 = map(int, box)
                # 네모 상자 그리기
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # 라벨 그리기
                label = f'{model.names[int(cls)]} {conf:.2f}'
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                # 클래스에 따라 시리얼 명령 전송
                if int(cls) == 0:  # bottle
                    send_command(0)

                elif int(cls) == 1:  # can
                    send_command(1)

                elif int(cls) == 2:  # pet
                    send_command(2)


                print(f'Sent data: {cls},{label}')

            # 화면에 표시
            cv2.imshow('Camera Feed', frame)
            time.sleep(10)
            # 마지막 캡처 시간을 현재 시간으로 업데이트
            last_capture_time = current_time

        # 'q' 키를 누르면 루프 중지
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    cap.release()
    arduino.close()
    cv2.destroyAllWindows()


