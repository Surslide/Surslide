//THIS OBSTACLE AVOIDER CAR CODE CAN FAIL IF USED IN ANOTHER CAR, THE WEIGHT, BATTERY POWER AND OTHER FACTORS CAN AFFECT THE RESULTS
//To use this code with a different car, adjust the millisecondsPerDegree constant according to the car's turning speed.

// --- OBSTACLE AVOIDER CAR PLAN --- //
//--hardware mapping
//servo and sonar infront using analogic pins, arduino in the middle, L298n and battery in the back using digital pins, motor DC below the car in both sides of the middle
//--code logic
//car keeps moving forward while continuously checking the distance ahead
//if an obstacle closer than 31 centimeters is detected, the car stops and checks both left and right
//the car chooses the path with the largest distance and above 30 centimeters
//if the difference between left and right is 1 centimeter or less and both are above 30 centimeters, choose one randomly
//if left and right are both below 31 centimeters, move slightly backward and rotate 180 degrees
//after rotating, the car keeps moving forward in small steps while scanning the sides until it finds an open lateral path
//once an open side is detected, the car turns toward it and returns to the normal obstacle avoidance behavior

//Future improvements: Use case methods

// --- LIBS --- //
#include <Servo.h>
Servo myServo;

// --- CONSTANTS --- //
const int minimumDistanceCm = 31;
const int motorSpeed = 125;
const int leftAngle = 10;
const int rightAngle = 170;
const float millisecondsPerDegree = 4;
//L298n pins
const int ENA = 5; //PWM
const int IN1 = 2; //Digital or Analogic
const int IN2 = 3; //Digital or Analogic
const int IN3 = 4; //Digital or Analogic
const int IN4 = 7; //Digital or Analogic
const int ENB = 6; //PWM
//servo pins
const int pinServo = 9; //Digital or PWM
//sonar pins
const int pinTrig = 10; //Digital or Analogic
const int pinEcho = 11; //Digital or Analogic
//random generator pin
const int randomPin = A0; //Analogic

// --- VARIABLES --- //
float leftDistance = 0;
float rightDistance = 0;
float frontDistance = 0;
bool inCorridor = false;
unsigned long corridorTimer = 0;

// --- FUNCTIONS(NON ARDUINO NATIVES) --- //
//behavior
void decision() {
  //left and right blocked
  if (leftDistance < minimumDistanceCm && rightDistance < minimumDistanceCm && !inCorridor) {
    backward();
    delay(100);
    brake(100);
    uTurn();
    inCorridor = true;
    corridorEscapeMode();
    inCorridor = false;
  }
  //left and right free, small difference
  else if (abs(leftDistance - rightDistance) <= 1 && rightDistance >= minimumDistanceCm && leftDistance >= minimumDistanceCm) {
    chooseRandomDirection();
  }
  //left free
  else if (leftDistance > rightDistance && leftDistance >= minimumDistanceCm) {
    turnLeft(80);
    brake(100);
  }
  //right free
  else if (rightDistance > leftDistance && rightDistance >= minimumDistanceCm) {
    turnRight(80);
    brake(100);
  }
}
void chooseRandomDirection() {
  if (random(2) == 0) {
    turnLeft(80);
    brake(100);
  } 
  else {
    turnRight(80);
    brake(100);
  }
}
void obstacleAvoider() {
  frontDistance = calculateDistance();
  if (frontDistance < minimumDistanceCm && !inCorridor){
    brake(100);
    scanSides();
    decision();
  }
  else if (frontDistance < minimumDistanceCm && inCorridor) {
    brake(100);
    backward();
    delay(100);
    brake(100);
    uTurn();
  }
}
void corridorEscapeMode() {
  while (leftDistance < minimumDistanceCm && rightDistance < minimumDistanceCm) {
    obstacleAvoider();
    forward();
    if (millis() - corridorTimer >= 200) {
      brake(100);
      scanSides();
      decision();
      corridorTimer = millis();
    }
  }
}
//movement
void forward() {
  //left wheel
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  //right wheel
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  //speed of left and right wheel
  analogWrite(ENB, motorSpeed);
  analogWrite(ENA, motorSpeed);
}
void turnRight(int angle) {
  //left wheel
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  //right wheel
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  //speed of left and right wheel
  analogWrite(ENB, motorSpeed);
  analogWrite(ENA, motorSpeed);
  //turning to the specific angle
  delay(angle * millisecondsPerDegree);
}
void turnLeft(int angle) {
  //left wheel
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  //right wheel
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  //speed of left and right wheel
  analogWrite(ENB, motorSpeed);
  analogWrite(ENA, motorSpeed);
  //turning to the specific angle
  delay(angle * millisecondsPerDegree);
}
void uTurn() {
  turnRight(180);
}
void brake(int brakeTime) {
  //left wheel
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, HIGH);
  //right wheel
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, HIGH);
  //speed of left and right wheel
  analogWrite(ENB, motorSpeed);
  analogWrite(ENA, motorSpeed);
  //time of brake
  delay(brakeTime);
}
void backward() {
  //left wheel
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  //right wheel
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  //speed of left and right wheel
  analogWrite(ENB, motorSpeed);
  analogWrite(ENA, motorSpeed);
}
//sensors
void scanSides() {
  myServo.write(leftAngle);
  delay(500);
  leftDistance = calculateDistance();
  myServo.write(rightAngle);
  delay(500);
  rightDistance = calculateDistance();
  myServo.write(90);
  delay(500);
}
float calculateDistance() {
  //send sound
  digitalWrite(pinTrig, LOW);
  delayMicroseconds(2);
  digitalWrite(pinTrig, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinTrig, LOW);
  //calculates distance
  unsigned long duration = pulseIn(pinEcho, HIGH, 30000);
  if (duration != 0) {
    return duration * 0.0342 / 2;
  }
  return 999;
}

// --- CODE --- //
void setup() {
  randomSeed(analogRead(randomPin));
  //L298n
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENB, OUTPUT);
  //servo
  myServo.attach(pinServo);
  //sonar
  pinMode(pinTrig, OUTPUT);
  pinMode(pinEcho, INPUT);
}

void loop() {
  obstacleAvoider();
  forward();
}
