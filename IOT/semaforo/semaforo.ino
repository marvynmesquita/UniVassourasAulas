//Cria variaveis
int ledVermelho = 7;
int ledAmarelo = 6;
int ledVerde = 5;

//Função para piscar led amarelo
void piscaAmarelo(int tempo) {
  for (int i=0; i<10; i++){
    digitalWrite(ledAmarelo, HIGH); //Liga led amarelo
    delay(tempo); 
    digitalWrite(ledAmarelo, LOW); //Desliga led amarelo
    delay(tempo);
  }
}

void setup() {
  //Define pino dos leds
  pinMode(ledVermelho, OUTPUT);
  pinMode(ledAmarelo, OUTPUT);
  pinMode(ledAmarelo, OUTPUT);
}

void loop() {
  digitalWrite(ledVermelho, HIGH); //Liga led vermelho
  delay(20000);
  digitalWrite(ledVermelho, LOW);//Desliga led vermelho
  digitalWrite(ledVerde, HIGH);//Liga led verde
  delay(20000);
  digitalWrite(ledVerde, LOW);//Desliga led verde
  piscaAmarelo(150);
}
