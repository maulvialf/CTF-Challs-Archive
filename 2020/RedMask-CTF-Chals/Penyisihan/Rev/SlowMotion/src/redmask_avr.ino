const int inputPin = 3;
const int readyPin = 2;
const int ledStatusPin = 13;
const unsigned char sice[32] = {
   27,  23,   1,   9,  12,  18,  24,  16,  75,
  111, 110,   3,   7, 106,  61,  27,  13,  17,
   58,  47,  21,  23,  45,  44,  22,   6,  12,
    1,  10,  59,   0,   3
};

int bitCounter = 0;
int pos = 0;
unsigned char key = 0x69;
unsigned char state = 0;

unsigned char* input;

void setup() {
  Serial.begin(115200);

  input = (unsigned char*)malloc(32);
  pinMode(readyPin, INPUT);
  pinMode(inputPin, INPUT);
  pinMode(ledStatusPin, OUTPUT);
}

void loop() {
  digitalWrite(ledStatusPin, HIGH);

  if (bitCounter == -1) {
    input[pos] = state ^ key;
    key ^= input[pos++];
    state = 0;
    bitCounter = 7;
  }

  if (memcmp(input, sice, 32) == 0) {
    // redmask{0_125_byte_per_second__}
    Serial.println("sice. got flag.");
  }

  if (digitalRead(readyPin) == HIGH) {
    digitalWrite(ledStatusPin, LOW);
    state |= digitalRead(inputPin) << bitCounter--;
    delay(1000);
  }
}

