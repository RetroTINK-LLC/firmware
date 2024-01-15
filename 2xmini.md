---
layout: default
title: RetroTINK-2X MINI Firmware
---

<h1 align="center" style="margin-top: 0px;">RetroTINK-2X MINI Firmware</h1>

<p style="margin:30px;"></p>

<h2 align="center" style="margin-top: 0px;">⚠️ CAUTION: Read carefully before proceeding ⚠️</h2>

<p style="margin:10px;"></p>

### DO NOT EVER ATTEMPT TO FLASH THE HEX FILES DIRECTLY TO THE PCB VIA THE PIC ICSP PINS. THESE FILES ARE ONLY FOR THE 2X-MINI. NEVER USE THESE FILES ON A PRO/SCART/PRO MULTIFORMAT AND VICE VERSA. YOU MUST USE THE RETROTINK SOFTWARE. THE FIRMWARE CONTAINS AN ANTI-PIRACY MEASURE THAT CAN PERMANENTLY DESTROY THE DEVICE. WE ARE NOT RESPONSIBLE FOR ANY DAMAGES THAT CAN OCCUR IN THIS CASE.

<p style="margin:20px;"></p>

## Instructions️

### Windows

1. Download the [FTDI D2XX Drivers](https://ftdichip.com/wp-content/uploads/2021/08/CDM212364_Setup.zip) and install.
2. Download the [RetroTINK Firmware update tool](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK%20FW%20Tool.zip) and install by unzipping and running RT_FWUP.
3. Download the appropriate HEX file for the desired version from the list below.
4. Plug your device into your computer's USB port while holding down the 'FILTER' button. The LED should be RED indicating update mode.
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

## Version 1.2

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Mini/RT2X_MINI_V12.hex)  
CRC-32: `33D5A43C`  
SHA-256: `450348a476dafb389c5a8dc11aee55e20a3d07c45d0b79e4f1d5a440d5a0b3af`

### Changelog:
- Press and hold the filter button for more than 1 second and release to toggle between pass-thru and Line2x.
- Pass-thru is only useful for transcoding and capturing with professional cards. It will not work with many TVs. If you do not specifically need this functionality, please do not attempt to use it.

<br/>

## Version 1.1

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Mini/RT2X_MINO_V11b.hex)  
CRC-32: `FD028CD1`  
SHA-256: `04f5eda53063ad22e60a11ef2536390e50da7d17a33e9283827d213139428b50`

### Changelog:
- Made LEDs dimmer.
- Improved detection stability.
- Mutes video output after 30 seconds of no valid input detected.
- Idle state (no input) is now solid green instead of cycling between yellow and white.
  