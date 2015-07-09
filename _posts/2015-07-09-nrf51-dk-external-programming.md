---
layout: post
title: External nRF51822 SWD Programming using the nRF51-DK
excerpt: "Using the Nordic nRF51-DK SWD pins to program external nRF51822 boards."
tags: [nRF51822, nRF-DK, BLE, SWD, JTAG, ADC]
categories: [Electronics]
comments: true
modified: 2015-07-09
image:
  feature: header.jpg
---

![RBL Nano ADC](/images/2015/07/rbl-nano-adc.jpg "RBL Nano ADC")

## Introduction

This is a short note on using the nRF51-DK to program an nRF51822 chip
on an external board. I've started with the RedbearLab Nano, but will add
to this article as I try other boards.

## Prerequisite

Before you read further, please take a look at my [previous article on
nRF51-DK programming using GCC][1], since we're going to use the same
setup here.

## nRF51-DK SWD Interface

One of the major advantages of getting the nRF5-DK1 is that it has a
built-in JTAG adapter and hence can be used to program external
chips. The standard 10-pin adapter is shown below in red. But there's
also a more convenient way to get the debug output using the *P20* pin
headers to the right of it. The *P20* uses standard pin spacing of
2.54 mm which makes it easy to hook up some wires to a breadboard.

![nRF51-DK-P20-SWD](/images/2015/07/nRF51-DK-P20-SWD.jpg "nRF51-DK-P20-SWD")

The complete hardware files for the nRF51-DK are [available from Nordic][5], and the schematic has the P20 connections used above. (Look for *nRF51-DK-HW* in the *Downloads* section.)

## Programming the RedBearLab Nano

Let's first look at how to program the [RedBearLab Nano][4], which seems to be a popular BLE board.

### Software 

To program the RedBearLab Nano, you need to make a couple of changes in the toolchain. The Nano has less memory compared to the chip on the nRF51-DK, so you need to make a corresponding change in *ble_app_uart_gcc_nrf51.ld*. (The RAM LENGTH below is decreased to 0x2000.)

{% highlight sh %}
{% raw %}
/* Linker script to configure memory regions. */

SEARCH_DIR(.)
GROUP(-lgcc -lc -lnosys)

MEMORY
{
  FLASH (rx) : ORIGIN = 0x18000, LENGTH = 0x28000
  RAM (rwx) :  ORIGIN = 0x20002000, LENGTH = 0x2000
}

INCLUDE "gcc_nrf51_common.ld"
{% endraw %}
{% endhighlight %}

The second change is really not necessary unless you want to use Nordic's BSP (Board Support Package) but I am including it in this project since you are likely to encounter it. Save the contents below to a file named *custom_board.h* in the *examples/bsp* folder in the SDK. 

{% highlight sh %}
{% raw %}
/* Copyright (c) 2012 Nordic Semiconductor. All Rights Reserved.
 *
 * The information contained herein is property of Nordic Semiconductor ASA.
 * Terms and conditions of usage are described in detail in NORDIC
 * SEMICONDUCTOR STANDARD SOFTWARE LICENSE AGREEMENT.
 *
 * Licensees are granted free, non-transferable use of the information. NO
 * WARRANTY of ANY KIND is provided. This heading must NOT be removed from
 * the file.
 *
 */
#ifndef REDBEAR_NANO_H__
#define REDBEAR_NANO_H__

#define LEDS_NUMBER    1

#define LED_START  19
#define BSP_LED_0  19
#define LED_STOP   19

#define BUTTONS_LIST {}
#define LEDS_LIST { BSP_LED_0 }

#define BSP_LED_0_MASK    (1<<BSP_LED_0)

// bsp.c assumes BSP_LED_1_MASK always exists
#define BSP_LED_1_MASK    (1<<BSP_LED_0)

#define LEDS_MASK      (BSP_LED_0_MASK)
#define LEDS_INV_MASK  LEDS_MASK

// there are no buttons on this board
#define BUTTONS_NUMBER 0
#define BUTTONS_MASK   0x00000000

// UART pins connected to J-Link
#define RX_PIN_NUMBER  11
#define TX_PIN_NUMBER  9
#define CTS_PIN_NUMBER 10
#define RTS_PIN_NUMBER 8
#define HWFC           true

#endif /* REDBEAR_NANO_H__ */

{% endraw %}
{% endhighlight %}

You can read more about *custom_board.h* at the [nRF51 SDK documentation on this topic][6].

### Hardware

Here are the pin connections for the Nano:

![RedBearLab Nano](/images/2015/07/rbl-nano.png "RedBearLab Nano")


Hook up the SWD interface as follows (Thanks to [Lijun's write-up][2] on this topic.):

| nRF51-DK | RBL Nano |
|:--------:|:--------:|
| SH_VTG  | VDD |
| SH_SWDIO | SWDIO |
| SH_SWDCLK | SWCLK |
| SH GND DETECT | GND |
| GND | GND |

If you are powering the Nano externally, connect VDD to the power supply - it has to be less than 3.3 V. Or you can power it from the VDD of nRF51-DK itself.

Here is a photo of how I hooked it up:

![RBL Nano SWD](/images/2015/07/rbl-nano-swd.jpg "RBL Nano SWD")

To program the board, just go into the *rbl_nano/s110/armgcc* and
build [like before][1]. The nRF51-DK will automatically detect the
external target and upload the code.

There are some slight changes I made for the Nano compared to my
previous project, and I use the same *main.c* for both projects by
using an *#ifdef BOARD_CUSTOM*:

1. The Nano has its built in LED on pin 19, so I used that instead of 22.
2. For some reason I could not get ADC input 2 to work, hence I
am using ADC input 5 for the Nano. So the LDR resistor divider output need to go into pin *P0_4* (RedBearLab calls it *A3* which is inconsistent with Nordic's numbering of the same pin as *Analog input 5*.)

RebBearLabs has brilliantly placed the LED *under* the Nano board, so you
just need to turn off all the lights in the room to check if it's
blinking. (Or ask your pet ant to check under the board.)

Once you have everything hooked up, the board will appear as
"ADC-UART-Nano" on your BLE app and you can get the LDR light values
over NUS (Nordic UART Service) [as before][1].

## Downloads

You can find files for this project at the github link below. Do your
builds in the *rbl_nano/s110/armgcc* folder.

[https://github.com/electronut/nRF51-adc-test][3]

## References

1. [Lijun's article][2] on using *P20* of the nRF51-DK.


[1]: http://electronut.in/nrf51-adc-test/
[2]: http://wiki.lijun.xyz/misc-use-nrf51-dk-debug-out.html
[3]: https://github.com/electronut/nRF51-adc-test
[4]: http://redbearlab.com/blenano/
[5]: https://www.nordicsemi.com/eng/Products/nRF51-DK
[6]: https://developer.nordicsemi.com/nRF51_SDK/nRF51_SDK_v8.x.x/doc/8.1.0/s110/html/a00033.html
