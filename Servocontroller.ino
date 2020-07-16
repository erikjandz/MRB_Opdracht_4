//code made on arduino IDE
#include <Servo.h>
Servo name_servo;

void setup(){
  name_servo.attach(7);
  Serial.begin(9600);
}

void loop(){
  int data = 0;
  while(true){
    if(Serial.available() > 0) {
      data = Serial.read();
      //90 is a standard value used to connect the serial port and therefore shouldn't control the servo,
      //if 90 is coincidentally the number to write the python code will write 91 instead
      if(data == 90){
        continue;
      }
      name_servo.write(data);
      delay(8);
    }
  }
}
