/*
  Citation
  https://thestempedia.com/docs/dabble/game-pad-module/
*/
#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE
#include <DabbleESP32.h>

#include "ESP32_Servo.h"

Servo myservo;         

int pos = 0;    
int servoPin = 14;
int i = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);      // make sure your Serial Monitor is also set at this baud rate.
  Dabble.begin("DemoDevice");       //set bluetooth name of your device
  pinMode(15, OUTPUT);
    pinMode(LED_BUILTIN, OUTPUT);
  myservo.attach(servoPin);
  i = 90;

}

void loop() {
  Dabble.processInput();             //this function is used to refresh data obtained from smartphone.Hence calling this function is mandatory in order to get data properly from your mobile.
  //Serial.print("KeyPressed: ");
  if (GamePad.isUpPressed())
  {
    Serial.print("Up ");
    Serial.println(i);
    i = 90;
    myservo.write(i);
    delay(15);
    digitalWrite(LED_BUILTIN, HIGH);
  }

  if (GamePad.isDownPressed())
  {
    Serial.print("Down ");
    Serial.println(i);
    i = -50;
    myservo.write(i);
    delay(15);
    digitalWrite(LED_BUILTIN, LOW);
  }

  if (GamePad.isLeftPressed())
  {
    Serial.print("Left");
    Serial.println(i);
    i = i - 1;
    myservo.write(i);
    delay(15);
  }

  if (GamePad.isRightPressed())
  {
    Serial.print("Right");
    Serial.println(i);
    i = i + 1;
    myservo.write(i);
    delay(15);
  }

  if (GamePad.isSquarePressed())
  {
    Serial.print("Square ");
    Serial.println(i);
    i = 50;
    myservo.write(i);
    delay(15);
  }


}
