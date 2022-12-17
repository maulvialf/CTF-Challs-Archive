char * flag = "REDACTED";
String curr;
int out0=46, out1=47, out2=48, out3=49, out4=50, out5=51, out6=52, out7=53;
int in0=24, in1=25, in2=26, in3=27, in4=28, in5=29, in6=30, in7=35;
int i;

String get_output(String bits) {
    String output;
    digitalWrite(out0, ((bits[7] == '1')? HIGH : LOW));
    digitalWrite(out1, ((bits[6] == '1')? HIGH : LOW));
    digitalWrite(out2, ((bits[5] == '1')? HIGH : LOW));
    digitalWrite(out3, ((bits[4] == '1')? HIGH : LOW));
    digitalWrite(out4, ((bits[3] == '1')? HIGH : LOW));
    digitalWrite(out5, ((bits[2] == '1')? HIGH : LOW));
    digitalWrite(out6, ((bits[1] == '1')? HIGH : LOW));
    digitalWrite(out7, ((bits[0] == '1')? HIGH : LOW));
    
    delay(500);
    output += String(digitalRead(in7));
    output += String(digitalRead(in6));
    output += String(digitalRead(in5));
    output += String(digitalRead(in4));
    output += String(digitalRead(in3));
    output += String(digitalRead(in2));
    output += String(digitalRead(in1));
    output += String(digitalRead(in0));
    return output;
}

//converts a given number into binary
String binary(int number) {
  String r;
  while(number!=0) {
    r = (number % 2 == 0 ? "0" : "1")+r; 
    number /= 2;
  }
  while ((int) r.length() < 8) {
    r = "0"+r;
  }
  return r;
}

void setup() {
  i = 0;
  pinMode(out0, OUTPUT);
  pinMode(out1, OUTPUT);
  pinMode(out2, OUTPUT);
  pinMode(out3, OUTPUT);
  pinMode(out4, OUTPUT);
  pinMode(out5, OUTPUT);
  pinMode(out6, OUTPUT);
  pinMode(out7, OUTPUT);

  pinMode(in0, INPUT);
  pinMode(in1, INPUT);
  pinMode(in2, INPUT);
  pinMode(in3, INPUT);
  pinMode(in4, INPUT);
  pinMode(in5, INPUT);
  pinMode(in6, INPUT);
  pinMode(in7, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (i < strlen(flag)) {
    curr = binary(flag[i]);
    Serial.println(get_output(curr));
    delay(500);
    i++;
  }
}
