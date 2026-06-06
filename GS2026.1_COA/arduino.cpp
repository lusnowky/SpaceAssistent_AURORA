/*
 * ============================================================
 *  SISTEMA IoT - MONITORAMENTO DE CÁPSULA ESPACIAL
 *  UTILIZADO NO ARDUINO DENTRO DO TINKERCAD
 *  LINK DO PROJETO: https://www.tinkercad.com/things/hhbg2m4zzBh-sistema-iot-coa-by-lucas-neves?sharecode=nQLW0ARAjjmXLLUJx176xJBZ-ugm1uUvb0MJ4T7PW-k
 * ============================================================
 *  LCD pinos : RS=12, EN=11, D4=10, D5=9, D6=8, D7=7  (PADRÃO TINKERCAD)
 *  TMP36     : A0
 *  LDR       : A1
 *  Potenc.   : A2
 *  LED Verde : 2
 *  LED Amar. : 3
 *  LED Verm. : 4
 *  Buzzer    : 5   
 * ============================================================
 */

#include <LiquidCrystal.h>

// ── Pinos ──
#define TMP36_PIN    A0
#define LDR_PIN      A1
#define VIBR_PIN     A2

#define LED_VERDE    2
#define LED_AMARELO  3
#define LED_VERMELHO 4
#define BUZZER_PIN   5

// LCD: RS, EN, D4, D5, D6, D7
LiquidCrystal lcd(12, 11, 10, 9, 8, 7);

// ── Limites de alerta ──────────────────────────────────────
const float TEMP_ALERTA = 35.0;
const float TEMP_PERIGO = 45.0;
const int   LUZ_MIN     = 100;
const int   VIBR_MAX    = 600;

// ── Variáveis ──────────────────────────────────────────────
float temperatura  = 0.0;
int   luminosidade = 0;
int   vibracao     = 0;
int   tela         = 0;
unsigned long ultimaLeitura   = 0;
unsigned long ultimaTrocaTela = 0;

// ── Ícones personalizados ──────────────────────────────────
byte iconTemp[8] = {0b00100,0b01010,0b01010,0b01110,0b01110,0b11111,0b11111,0b01110};
byte iconLuz[8]  = {0b00100,0b10101,0b01110,0b11111,0b11111,0b01110,0b10101,0b00100};
byte iconVibr[8] = {0b10001,0b01010,0b00100,0b01010,0b10001,0b01010,0b00100,0b01010};

// ══════════════════════════════════════════════════════════
void setup() {
  Serial.begin(9600);

  lcd.begin(16, 2);
  lcd.createChar(0, iconTemp);
  lcd.createChar(1, iconLuz);
  lcd.createChar(2, iconVibr);

  pinMode(LED_VERDE,    OUTPUT);
  pinMode(LED_AMARELO,  OUTPUT);
  pinMode(LED_VERMELHO, OUTPUT);
  pinMode(BUZZER_PIN,   OUTPUT);

  // Boot screen
  lcd.setCursor(3, 0);
  lcd.print("CAPSULA v2.0");
  lcd.setCursor(1, 1);
  lcd.print("FIAP GS 2026");
  digitalWrite(LED_VERDE, HIGH);
  delay(2500);
  lcd.clear();
  digitalWrite(LED_VERDE, LOW);
}

// ══════════════════════════════════════════════════════════
void loop() {
  unsigned long agora = millis();

  if (agora - ultimaLeitura >= 2000) {
    ultimaLeitura = agora;
    lerSensores();
    enviarSerial();
    atualizarAlertas();
  }

  if (agora - ultimaTrocaTela >= 3000) {
    ultimaTrocaTela = agora;
    tela = (tela + 1) % 3;
    exibirTela(tela);
  }
}

// ══════════════════════════════════════════════════════════
void lerSensores() {
  float tensao = analogRead(TMP36_PIN) * (5.0 / 1023.0);
  temperatura  = (tensao - 0.5) * 100.0;

  luminosidade = map(analogRead(LDR_PIN),  0, 1023, 0, 1000);
  vibracao     = analogRead(VIBR_PIN);
}

void enviarSerial() {
  Serial.println("=== TELEMETRIA DA CAPSULA ===");
  Serial.print("Temperatura : "); Serial.print(temperatura, 1); Serial.println(" C");
  Serial.print("Luminosidade: "); Serial.print(luminosidade);   Serial.println(" lux");
  Serial.print("Vibracao    : "); Serial.println(vibracao);
  Serial.println("-----------------------------");
}

void atualizarAlertas() {
  bool perigo     = (temperatura >= TEMP_PERIGO) || (vibracao >= VIBR_MAX);
  bool alertaTemp = (temperatura >= TEMP_ALERTA);
  bool alertaLuz  = (luminosidade <= LUZ_MIN);

  digitalWrite(LED_VERDE,    LOW);
  digitalWrite(LED_AMARELO,  LOW);
  digitalWrite(LED_VERMELHO, LOW);
  noTone(BUZZER_PIN);

  if (perigo) {
    digitalWrite(LED_VERMELHO, HIGH);
    tone(BUZZER_PIN, 1000);         
  } else if (alertaTemp || alertaLuz) {
    digitalWrite(LED_AMARELO, HIGH);
    tone(BUZZER_PIN, 500, 300);     // beep curto
  } else {
    digitalWrite(LED_VERDE, HIGH);
  }
}

void exibirTela(int t) {
  lcd.clear();
  switch (t) {
    case 0:
      lcd.setCursor(0, 0);
      lcd.write(byte(0));
      lcd.print(" TEMP: ");
      lcd.print(temperatura, 1);
      lcd.print((char)223);
      lcd.print("C");
      lcd.setCursor(0, 1);
      if      (temperatura >= TEMP_PERIGO)  lcd.print("  >> PERIGO! <<");
      else if (temperatura >= TEMP_ALERTA)  lcd.print("  ** ALERTA **");
      else                                  lcd.print("  STATUS: OK  ");
      break;

    case 1:
      lcd.setCursor(0, 0);
      lcd.write(byte(1));
      lcd.print(" LUZ:");
      lcd.print(luminosidade);
      lcd.print(" lux");
      lcd.setCursor(0, 1);
      lcd.print(luminosidade <= LUZ_MIN ? "  MUITO ESCURO!" : "  ILUMINACAO OK ");
      break;

    case 2:
      lcd.setCursor(0, 0);
      lcd.write(byte(2));
      lcd.print(" VIB: ");
      lcd.print(vibracao);
      lcd.setCursor(0, 1);
      if      (temperatura >= TEMP_PERIGO || vibracao >= VIBR_MAX)           lcd.print("!! PERIGO !!");
      else if (temperatura >= TEMP_ALERTA || luminosidade <= LUZ_MIN)        lcd.print("** ALERTA **");
      else                                                                    lcd.print("  NOMINAL   ");
      break;
  }
}