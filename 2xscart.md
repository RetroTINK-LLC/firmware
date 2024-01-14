---
layout: default
---

<h1 align="center" style="margin-top: 0px;">RetroTINK-2X SCART Firmware</h1>

<p style="margin:30px;"></p>

<h2 align="center" style="margin-top: 0px;">⚠️ CAUTION: Read carefully before proceeding ⚠️</h2>

<p style="margin:10px;"></p>

### DO NOT ATTEMPT TO FLASH THE HEX FILE DIRECTLY TO THE PCB VIA THE ICD PINS. THESE FILES ARE ONLY FOR THE 2X-SCART. NEVER USE THESE FILES ON A PRO/MINI/PRO MULTIFORMAT AND VICE VERSA. YOU MUST USE THE RETROTINK SOFTWARE. THE FIRMWARE CONTAINS AN ANTI-PIRACY MEASURE THAT CAN PERMANENTLY DESTROY THE DEVICE. WE ARE NOT RESPONSIBLE FOR ANY DAMAGES THAT CAN OCCUR IN THIS CASE.

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

## Version 1.6

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20SCART/RT2XSCART_v16.hex)
CRC-32: `5E57DA40`  
SHA-256: `0ed6b98b6d6849f6fffa950ea9048983ae2f58ae5ba80b099d0673c25d930936`

### Changelog:
  - Minor bug fixes related to "low-res" filter.

<br/>

## Version 1.5

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20SCART/RT2X_SCART%20v15.hex)
CRC-32: `1FDF4A7F`  
SHA-256: `06b372347571b114d30a5882b2b85a75255179bd048859c3fec16111e69f8941`

### Changelog:
  - Fixed problem with booting up in pass-thru
  - Tweaked low-res YPbPr
  - Modified automatic HDMI disable on no input to recover without losing audio output.

<br/>

## Version 1.4

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20SCART/RT2XSCART%20v14.hex)
CRC-32: `D0F5025C`  
SHA-256: `be049475d4fb62fe276313609d9cc1a3ab56bf5056f9928b71b09b8695f8b4ab`

### Changelog:
  - Full EDID readout to detect DVI devices every time the video output port is cycled.
  - Added "Low Res YPbPr" plus scanline filter mode.
  - By popular request, added "sleep/off" mode. Press and hold the "Filter" button for 3 seconds to turn the device off. Short tap on the "Filter" button to turn the device back on.
  - Auto shut off of video output if no input is detected for 30 seconds. Red LED flashes 3 times to indicate video output power-down. Output is automatically resumed when a valid input is detected again.
  - Yet more tweaks to audio output in a futile attempt to maximize compatibility.

<br/>

## Version 1.3

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20SCART/RT2X_SCART%20v13.hex)
CRC-32: `4A3BB110`  
SHA-256: `4063cd65c4d6ca3d83f87db27dd38129d0aa563eb4091203525a3f6e23cfe975`

### Changelog:
  - FBX calibrated luma gain for perfect NES output
  - Tweaked audio output for (hopefully) better audio compatibility
  - Tweaked sync, porch and active timing to comply with CEA-861 standards except for the number of vertical lines when doubling 240p/288p.
  - Tweaked low-res YPbPr mode
  - 480i scanline mode: The scanline generator cycles between blanking odd and even lines every frame to simulate an interlaced CRT. The image is darker but does restore some lost vertical resolution using your eye as a sort of weave de-interlacer.

<br/>

## Version 1.2

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20SCART/RT2X_SCART%20v12.hex)
CRC-32: `57C01E46`  
SHA-256: `bf12ec37b94d49779ff2b5a289e318d9bf82672aedccd04a03bf8eea2d7e5ab4`

### Changelog:
  - Improved DVI-only detection
  - CVBS Luma gain in 'Auto' mode now works more like a modern LCD versus a CRT if you prefer that look instead.
  - Low-res YPbPr mode for mimicking pixel dithering effects. Filter button cycle is now: regular, smoothed, scan-lined, low-resolution, low-resolution/smoothed. Warning: low-resolution mode is for experimental purposes only and degrades the sharpness (and adds minor ringing artifacts) since it applies CVBS type filtering to the Luma channel. Added only due to popular request :-)
