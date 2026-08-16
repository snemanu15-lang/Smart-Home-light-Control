#define RELAY_PIN 23

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);

  Serial.begin(115200);
}

void loop() {
  // Turn light ON
  digitalWrite(RELAY_PIN, HIGH);
  Serial.println("Light ON");
  delay(5000);

  // Turn light OFF
  digitalWrite(RELAY_PIN, LOW);
  Serial.println("Light OFF");
  delay(5000);
}
