#include <Servo.h>
Servo v1;
Servo v2;
//180이 오른쪽(시계방향 회전)
void setup() {
  Serial.begin(9600);
  v1.attach(6);
  v2.attach(7);
}

void loop() {
  if(Serial.available() > 0) {  // 시리얼 데이터를 받을 수 있을 때
    int command = Serial.parseInt(); // 정수로 받음   위는 3200 아래는 2500
    switch (command) {
      case 0:
        v1.write(180); //BOTTLE
        delay(3200);
        v1.write(90);
        delay(400);
        v1.write(0);
        delay(3200);
        v1.write(90);
        delay(400);


        v2.write(0); //가운데로 떨구기
        delay(2500);
        v2.write(90);
        delay(400);
        v2.write(180);
        delay(2500);
        v2.write(90);
        delay(400);
        break;
      case 1:  //CAN
        v1.write(180); 
        delay(3200);  //same
        v1.write(90);
        delay(400);
        v1.write(0);
        delay(3200);
        v1.write(90);
        delay(400);


        v2.write(180);
        delay(2500);
        v2.write(90);
        delay(400);
        v2.write(0);
        delay(2500);
        v2.write(90);
        delay(400);
        break;
  
      case 2:
        v1.write(0); //페트니깐 오른쪽으로 밀기(시계방향)
        delay(3200);   //same 끝
        v1.write(90);
        delay(400);
        v1.write(180);
        delay(3200);
        v1.write(90);
        delay(400);
        break; 
    }
  }
}

