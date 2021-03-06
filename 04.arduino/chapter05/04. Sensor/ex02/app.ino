// LM35 μ¨λ μΌμ
#include <MiniCom.h>

MiniCom com;
const int lm35_pin = A0;

void check()
{
    int value = analogRead(lm35_pin);
    float ftp = value / 1024.0 * 5;
    ftp = ftp * 100.0 + 0.5;
    com.print(1, "T: ", ftp);
}

void setup()
{
    com.init();
    com.setInterval(2000, check);
    com.print(0, "[[LM35]]");
    com.print(1, "Preparing LM35");
}

void loop()
{
    com.run();
}
