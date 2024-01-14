---
layout: default
title: {{[{{site.title}}]({{site.url}}) | markdownify}}
---

<h1 align="center" style="margin-top: 0px;">RetroTINK-2X Pro firmware</h1>

<br />

<h2 align="center" style="margin-top: 0px;">⚠️ CAUTION: Read carefully before proceeding ⚠️</h2>

### DO NOT ATTEMPT TO FLASH THE HEX FILE DIRECTLY TO THE PCB VIA THE ICD PINS. THESE FILES ARE ONLY FOR THE 2X-PRO. NEVER USE THESE FILES ON A SCART/MINI/PRO MULTIFORMAT AND VICE VERSA. YOU MUST USE THE RETROTINK SOFTWARE. THE FIRMWARE CONTAINS AN ANTI-PIRACY MEASURE THAT CAN PERMANENTLY DESTROY THE DEVICE. WE ARE NOT RESPONSIBLE FOR ANY DAMAGES THAT CAN OCCUR IN THIS CASE.

## THE RETROTINK-2X PRO IS INCOMPATIBLE WITH FIRMWARE FOR THE RETROTINK-2X PRO MULTIFORMAT.

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

## Version 1.7

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro/RT2XPro%20v17.hex)
CRC-32: `B8267F90`  
SHA-256: `5a1d6cab8a03e07ff0c5cf4070b78ddc48ed864769f84d4d6e5854e6a74aa617`

### Changelog:
  - Retro mode now calibrated to 0.7 V video
  - Auto mode now uses an auto gain function to adapt to different video sources
  - Generally much brighter and vivid image output

<br/>

## Version 1.6

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro/RT2XPro_V16.hex)
CRC-32: `50572D2B`  
SHA-256: `e681d397262cc3ba05a22551bc9285e61387e1a0948dfeb068edf7aa36d434c5`

### Changelog:
  - Minor bug fixes related to "low-res" filter.

<br/>

## Version 1.5

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro/RT2XPro%20v15.hex)
CRC-32: `299227C8`  
SHA-256: `c121d7516f91519c6e1d3a1e661fb0578a4836404a223bab21383c336c45f86d`

### Changelog:
  - Fixed problem with booting up in pass-thru
  - Tweaked low-res YPbPr
  - Modified automatic HDMI disable on no input to recover without losing audio output.

<br/>

## Version 1.4

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro/RT2XPro%20v14.hex)
CRC-32: `76989026`  
SHA-256: `976f37dee577116892440e03c38cb1cb79743ce167fbc30925b8717e1b1f34f0`

### Changelog:
  - Full EDID readout to detect DVI devices every time the video output port is cycled.
  - Added "Low Res YPbPr" plus scanline filter mode.
  - By popular request, added "sleep/off" mode. Press and hold the "Filter" button for 3 seconds to turn the device off. Short tap on the "Filter" button to turn the device back on.
  - Auto shut off of video output if no input is detected for 30 seconds. Red LED flashes 3 times to indicate video output power-down. Output is automatically resumed when a valid input is detected again.
  - Yet more tweaks to audio output in a futile attempt to maximize compatibility.

<br/>

## Version 1.3

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro/RT2X-Pro%20v13.hex)
CRC-32: `44179261`  
SHA-256: `8588543b0bb02ff2a046cf83a022f8a1c3dd63f781914f70091e50a5d0ade5a3`

### Changelog:
  - FBX calibrated luma gain for perfect NES output
  - Tweaked audio output for (hopefully) better audio compatibility
  - Tweaked sync, porch and active timing to comply with CEA-861 standards except for the number of vertical lines when doubling 240p/288p.
  - Tweaked low-res YPbPr mode
  - 480i scanline mode: The scanline generator cycles between blanking odd and even lines every frame to simulate an interlaced CRT. The image is darker but does restore some lost vertical resolution using your eye as a sort of weave de-interlacer.

<br/>

## Version 1.2

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro/RT2X-Pro%20v12.hex)
CRC-32: `62DDD244`  
SHA-256: `a86c1570a3a2855a02ee190c37b2ae56d2929fcc024e15f0d8f959b1b2496545`

### Changelog:
  - Improved DVI-only detection
  - CVBS Luma gain in 'Auto' mode now works more like a modern LCD versus a CRT if you prefer that look instead.
  - Low-res YPbPr mode for mimicking pixel dithering effects. Filter button cycle is now: regular, smoothed, scan-lined, low-resolution, low-resolution/smoothed. Warning: low-resolution mode is for experimental purposes only and degrades the sharpness (and adds minor ringing artifacts) since it applies CVBS type filtering to the Luma channel. Added only due to popular request :-)

<br/>

## Version 1.1

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-2X%20Pro/RT2X-Pro_v11.hex)
CRC-32: `7D1B7F18`  
SHA-256: `35e2c9068ac7572913de3ff88ae814156a25ed6958d300ab885aa73e17362d02`

### Changelog:
  - Improved sharpness on all input modes via tweaked filters.
  - Improved format detection and switching for PAL60, PAL-M, NTSC4.43 (modified consoles).
  - Smooth mode is SMOOTHER.
  - Blocky mode is slightly sharper.
  - Added LED flicker to indicate new format detection.
  - Tweaked Composite Luma sharpness per format color subcarrier.
  - Tweaked Composite PAL Chroma comb filter to remove interleaved chroma lines.
  - Added Composite high resolution Chroma mode (manually enabled, not saved after power down, see manual).
  - Improved Color Bars displaying stability in free run.
  - Auto-detection of DVI only monitors at power up via EDID, indicated by Blue LED at power up.
  - Manual DVI mode (see manual).
  - Re-centered image vertically by 1 pixel.
  - Output mode changed to RGB444 from YCbCr 422, which had previously caused color fidelity issues on some TVs with respect to the Classic.
  