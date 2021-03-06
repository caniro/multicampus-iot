#include <Led.h>

#define OFF 0
#define ON 1

const int sw_pin = 2;
Led leds[4] = {
    Led(8), Led(9), Led(10), Led(11)
};
int out_no = -1;

void onClick();

void setup()
{
    Serial.begin(115200);
    pinMode(sw_pin, INPUT_PULLUP);
}

void loop()
{
    check();
}

void check()
{
    boolean o_sw, n_sw;
    o_sw = !digitalRead(sw_pin);
    delay(10);
    n_sw = !digitalRead(sw_pin);

    if (o_sw == OFF && n_sw == ON)
    {
        onClick();
    }
}

void onClick()
{
    out_no = (++out_no) % 5;
    Serial.println(out_no);
    for (int n = 0; n < 4; ++n)
    {
        if (out_no == 5)
            leds[n].off();
        else
            leds[n].setValue(n == out_no);
    }
}
