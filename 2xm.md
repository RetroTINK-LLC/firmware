---
layout: default
title: RetroTINK Firmware Repository - RetroTINK-2X Pro Multiformat Firmware
---

<h1 align="center" style="margin-top: 0px;">RetroTINK-2X Pro Multiformat Firmware</h1>

<p style="margin:30px;"></p>

<h2 align="center" style="margin-top: 0px;">⚠️ CAUTION: Read carefully before proceeding ⚠️</h2>

<p style="margin:10px;"></p>

### DO NOT EVER ATTEMPT TO FLASH THE HEX FILES DIRECTLY TO THE PCB VIA THE PIC ICSP PINS. THESE FILES ARE ONLY FOR THE 2X-M. NEVER USE THESE FILES ON A NON-MULTIFORMAT PRO/SCART/MINI AND VICE VERSA. YOU MUST USE THE RETROTINK SOFTWARE. THE FIRMWARE CONTAINS AN ANTI-PIRACY MEASURE THAT CAN PERMANENTLY DESTROY THE DEVICE. WE ARE NOT RESPONSIBLE FOR ANY DAMAGES THAT CAN OCCUR IN THIS CASE.

<p style="margin:10px;"></p>

## THE RETROTINK-2X PRO MULTIFORMAT IS INCOMPATIBLE WITH FIRMWARE FOR THE RETROTINK-2X PRO.

<p style="margin:20px;"></p>

## Instructions️

### Windows

1. Download the [FTDI D2XX Drivers](https://ftdichip.com/wp-content/uploads/2021/08/CDM212364_Setup.zip) and install.
2. Download the [RetroTINK Firmware update tool](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK%20FW%20Tool.zip) and install by unzipping and running RT_FWUP.
3. Download the appropriate HEX file for the desired version from the list below.
4. Plug your device into your computer's USB port while holding down the 'INPUT' button. The LED should be RED indicating update mode.
5. Run the RetroTINK Firmware Update tool. The installer will have left a shortcut on your desktop.
6. Hit 'Search'. You should see 'FT232R USB UART' appear in the box.
7. Hit 'Load HEX' and point to the .hex file you downloaded.
8. Hit 'Flash'. The update process should start. If the window freezes, that is okay - the update should complete within a minute or so.
9. Your device should reboot and be ready to use.
10. If you accidentally interrupt the process, just start over from step 4.

### Multiplatform

A talented developer (Ryan Mullen) [ported the firmware update tool to Python.](https://github.com/rmull/tinkup)

This should work on Windows, Mac (including M1) and Linux.

### Video

Big thanks to [RetroRGB](https://www.retrorgb.com/how-to-update-your-retrotinks-firmware.html) who was kind and generous enough to put this video together. **Please do not contact him for technical support.**

<iframe width="560" height="315" src="https://www.youtube.com/embed/Bva0JXLoq7E?si=Eobt-HF3LD1Lo89_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<br/>

## Version 1.8

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro%20Multiformat/RT2XM_V18.hex)
CRC-32: `DF91F410`  
SHA-256: `983ca8531543f0e459ea3743f77b2c8aa83139d16e71a3ee8f582feef037b6e4`

### Changelog:
  - Bug fixes related to sync stability.

<br/>

## Version 1.7

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro%20Multiformat/RT2XM_V17.hex)
CRC-32: `D1A8EE38`  
SHA-256: `d12a0e0ab953694d7ef1e03af49776e9584b147e2f0b466524b8ca771cd1824f`

### Changelog:
  - Minor bug fixes related to 480i sync.

<br/>

## Version 1.6

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro%20Multiformat/RT2XM_V16.hex)
CRC-32: `AE8D1982`  
SHA-256: `2e81aebce14ead92c14222cdf44a180d4aa382241d9f6482d84133110d95c268`

### Changelog:
  - Added 576p Pass-thru. This mode also has an identical 'Hi-Res' 444 variant to the 480p. Switching the 'Mode' switch to 'Line2x' enables 444. Tapping the 'Filter' button once (Blue light turns on) further doubles the horizontal resolution.
  - Added 240p/480i 444 pass-thru. The 'Comb' switch should be set in the 'Retro' position to enable this. I have somewhat mixed feelings as compatibility will be highly hit and miss but I thought it'd be better to see if this is useful for people before deciding to keep/remove it in the future.
  - So far SNES seems to be very intermittent. PS2/PSOne appears to work well, as does Genesis and TG16/PCE.
  - If you're super confused, just set the device to 'Line2x' and 'Auto' and you should have a decent default mode for most use cases.

<br/>

## Version 1.5

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro%20Multiformat/RT2XM_V15c.hex)
CRC-32: `DC3F6C9D`  
SHA-256: `4f4113cd237e0e733f219d110b0452c05c0b9f7771b335b6d6f29d77a8e6649e`

### Changelog:
  - Improved sync stability and tolerance.
  - Fixed clock polarity (wasn't causing a problem but why not).
  - Hi-res 480p 444 mode indicated by blue light after tapping the 'Filter' button once.

<br/>

## Version 1.4 (BETA)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro%20Multiformat/RT2XM_V14_BETA.hex)
CRC-32: `6E1EDD14`  
SHA-256: `dfc5eb09b4f91cbd74451a815e6fe03fd8df52cff9e363e32fa127538b5d8b36`

### Changelog:
  - Added 1788 x 1080i. Unfortunately the video ADC cannot sample the full 1920 pixels/line. As with the 720p support, this should be considered a bonus and never a selling point.

<br/>

## Version 1.3 (BETA)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro%20Multiformat/RT2XM_V13BETA_HIRES.hex)
CRC-32: `C44AF7C0`  
SHA-256: `02640b7bb7b41f0a64cb1c6cfb92fd9cb05d53d2acab7adac3acdb3d9674e0e5`

### Changelog:
  - Added 720p pass-thru support. Note: this feature should be considered a bonus and never a selling point. While the "pseudo-444" RGB mode may become a "stable" feature in the future, the 720p support relies on overclocking the system. While there is virtually no risk of damage, there can be no guarantee that the it will work on every unit. The audio timing is also slightly off standard.
  - Added 480p "Hi-Res" mode. Click the 'Filter' button when in 444 480p to activate. This sends twice the horizontal resolution. Since this is not going to be compatible with every display, this setting is not remembered across power cycles.
  - Further improvements in stability for 480p modes and sync detection.

<br/>

## Version 1.2

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro%20Multiformat/RT2XM_V12.hex)
CRC-32: `9D2B3DF1`  
SHA-256: `2e46adc3ba54f89e50498ff0a62e979c4ad080b174c3423fc0e3aa67728937e9`

### Changelog:
  - Pseudo-444 sampling mode for 480p inputs only. Set the 'Mode' switch to 'Line2x' to activate. 'Pass' operates with the exact same 422 output as before.
  - Pseduo-444 mode outputs a standard CEA-861 720 x 480p resolution but should be considered experimental until further notice.
  - Improved sync detection and stability.

<br/>

## Version 1.1

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro%20Multiformat/RT2XM%20v11.hex)
CRC-32: `AD22BDA1`  
SHA-256: `f6267a3d5990e2660b7fcf330d78827cbcfa6eb4b9a1681087d4263ccca66c7e`

### Changelog:
  - Fixed image shift glitch for component video mode on PS2 and other consoles with jitter/noisy sync pulses.
  - Enabled field offset for 480i deinterlacing (see manual).
  - Enabled chroma phase control for 480p sampling (see manual).
