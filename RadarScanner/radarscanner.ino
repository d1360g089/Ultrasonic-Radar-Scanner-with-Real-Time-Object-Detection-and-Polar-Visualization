
#include <Servo.h>
#include <LiquidCrystal.h>


int servoPin = 9;
float angle = 0;
Servo myServo;
int step = 15;


//UltraSonic Sensor
int trigPin = 11;
int echoPin = 10;
float pingTravelTime;
float distance;

//lcd Setup
int rs = 7;
int en = 8;
int d4 = 6;
int d5 = 5;
int d6 = 4;
int d7 = 3;

LiquidCrystal lcd(rs,en,d4,d5,d6,d7);

int buzzPin = 2;

int xPin = A0;
int sPin = 12;
int xVal;
int sVal;

float joystickAngle;
float alpha = .1;




void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzPin, OUTPUT);
  lcd.begin(16,2);
  pinMode(xPin, INPUT);
  pinMode(sPin, INPUT);
  digitalWrite(sPin, HIGH);

}

void loop() {

  digitalWrite(trigPin, LOW);
  delayMicroseconds(100);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(100);
  digitalWrite(trigPin, LOW);
  pingTravelTime = pulseIn(echoPin, HIGH);
  delay(25);


  distance = (4.25/700.)*pingTravelTime + .786;

  Serial.print(distance);
  Serial.print(",");
  Serial.println(angle);
  
  lcd.setCursor(0,0);
  lcd.print("Distance:");
  lcd.print(distance);
  lcd.print("in");

  lcd.setCursor(0,1);
  lcd.print("Angle:");
  lcd.print(angle);
  delay(300);
  lcd.clear();


  xVal = analogRead(xPin);
  sVal = digitalRead(sPin);



  //Joystick control 
  /*
  
  joystickAngle = (-180./1023.) * xVal + 180;

  myServo.write(joystickAngle);

  if (joystickAngle >= 180){
    joystickAngle = 180;

  }

  if (joystickAngle <= 0){
    joystickAngle = 0;

  }
  
  */
  


  
  //Autonomous movement
  myServo.write(angle);

  angle = angle + step;

  if (angle >= 180 || angle <= 0){
    step = -step;

  }



  delay(10);

 
  if (distance <= 3.00){
    // Stop Servo
    myServo.write(angle);
    
    
    lcd.setCursor(4,0);
    lcd.write("Warning!!");
    lcd.setCursor(0,1);
    lcd.write("Object Detected");
    delay(350);


    //activebuzz
    digitalWrite(buzzPin, HIGH);
    delay(500);
    digitalWrite(buzzPin, LOW);
    delay(500);

    lcd.clear();


    
  }

  
  

}
