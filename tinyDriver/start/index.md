---
layout: page
title: Getting Started with tinyDriver
tags: [tinyDriver, tinyAVR, ATtiny84, Arduino]
modified: 2016-04-01
comments: false
image:
  feature: header.jpg
---

This is a guide for getting started with your [tinyDriver][1] board.

## Programming Setup

To get *tinyDriver* going, you need some hardware and some software.

### Hardware 

To program 

![USB ASP]()

- USB ASP

![Tiny AVR]()

- Sparkfun USBTiny


![Atmel ICE]()


- Atmel ICE

### Software

- Atmel Studio
- avrdude
- avr-gcc
- WinAVR
- CrossPack

uploading code

## Your First *tinyDriver* Program 

For using the *tinyDriver*, you need to learn some AVR programming. 
This may sound intimidating, but it's really not that hard. 
If you learn a bit of C (pun alert) and a smattering of microcontroller 
jargon, you know enough to get started. I have nice resources at the end 
of the article to help you get you started.

If you have used an Arduino before, you know that 
the code is usually structured as follows:

{% highlight C++ %}
{% raw %}
// hello.ino

// initial setup
void setup()
{
   
}

// main loop 
void loop()
{

}
{% endraw %}
{% endhighlight %}

AVR programming is not so different:

{% highlight C %}
{% raw %}
// main.c

// main program
int main(void)
{
   // set up code here

   // being main loop
   while (1) {

     // do your stuff here
   }
}
{% endraw %}
{% endhighlight %}

Folks suffering from AWS (Arduino Withdrawal Syndrome) may resort to this:

{% highlight C %}
{% raw %}
// main.c

// initial setup
void setup()
{
   
}

// main loop 
void loop()
{

}

// main program
int main(void)
{
   // set up code here
   setup();

   // being main loop
   while (1) {   
     // do your stuff here
     loop();
   }
}
{% endraw %}
{% endhighlight %}

### Blinking the RGB LED

Our goal for the first program is to make the built-in RGB LED of 
*tinyDriver* to pulse as follows: 

*Flash Red, Green, Blue. Repeat.*

For this, first let's grab the ATtiny84A datasheet. ([PDF link][3] from 
Atmel site.)

Here's the pinout diagram for the ATtiny84:

![Attiny84A pinout]()


Now let's take a peek at the *tinyDriver* schematic:

![tinyDriver Schematic]()

So, the RGB LED is connected to pins *PA0* (Red), *PA1* (Green) and 
*PA2* (Blue). So all we need to do is turn each of these pins *HIGH*.

Here is the full code listing:

{% highlight C %}
{% raw %}
#include <avr/io.h>
#include <util/delay.h>
 
#define F_CPU 8000000

int main (void)
{
    // set PA0, PA1, PA2 as output
    DDRA = (1 << PA0) | (1 << PA1) | (1 << PA2);

    // loop
    while (1) {

        // flash red
        PORTA = (1 << PA0);
        _delay_ms(500);
        PORTA = 0;
        _delay_ms(500);

        // flash green
        PORTA = (1 << PA1);
        _delay_ms(500);
        PORTA = 0;
        _delay_ms(500);

        // flash blue
        PORTA = (1 << PA2);
        _delay_ms(500);
        PORTA = 0;
        _delay_ms(500);

    }
}
{% endraw %}
{% endhighlight %}

We start by including a few header files. *avr/io.h* contains the 
apropriate IO definitions for the selected chip, which in this case 
is ATtiny84A. The *util/delay.h* is included so that can use the *_delay_ms()* 
function in our program.

Next, you will see that *F_CPU* is set to the value of *8000000*, or 
8 MHz.


### Uploading the Code



## Your Second *tinyDriver* Program 


- hardware PWM.

## Downloads

You can find the complete source code for both the above projects here:

[https://github.com/electronut/tinyDriver][2]


## What Next? Adventure is out there!

- Books on C
- Books on AVR programming
- electronics


[1]: http://electronut.in/tinyDriver/
[2]: https://github.com/electronut/tinyDriver
[3]: http://www.atmel.com/Images/doc8183.pdf
