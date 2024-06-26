---
layout: default
title: RetroTINK-4K SD Card Images
---

<h1 align="center" style="margin-top: 0px;">RetroTINK-4K SD Card Images</h1>

<p style="margin:30px;"></p>

<h2 align="center" style="margin-top: 0px;">⚠️ CAUTION: Read carefully before proceeding ⚠️</h2>

<p style="margin:30px;"></p>

## Instructions️

1. Download the appropriate zip file for the desired SD card image (this should contain all data normally on the SD card: firmware, profiles, banners and other data).
2. Unzip onto a [freshly formatted FAT32 SD card](http://ridgecrop.co.uk/index.htm?guiformat.htm).
3. If needed, download and copy the latest firmware from the [Release Firmware section](4k.md), and perform a firmware update on your RT4K as instructed.

<p style="margin:41px;"></p>

## Version 1.4.2 (2024-04-27)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/SD%20card%20images/Rt4k_142_sdcard.zip)
CRC-32: `60728C8D`  
SHA-256: `0be711173c5b22b82d9b1643f01f7518bf07e22ce9bc2c7a9e24ab936aecbcc2`

### Changelog:
- Next generation Motion Adaptive Deinterlacer
- Improved multi-field motion analysis to minimize false combing
- Improved spatio-temporal smoothing of motion vectors
- Edge-adaptive interpolation to minimize "jaggies" when Bob is used
- Improved Freesync VRR compatibility
- Added VESA VRR
- Added HLG HDR mode with proper color conversion and PQ
- For HLG, the Input Gain control under the "Color Correction" menu should be used to tune the intensity

<br/>


## Version 1.3.4 (2024-03-15)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/SD%20card%20images/Rt4k_134_sdcard.zip)
CRC-32: `6EA7BEB3`  
SHA-256: `9b94a06b5ae6c26959f6d25996bee662745a242cd7919ce4a539d10925d2d1df`

### Changelog:
- Added XBR Smoothing
- Added Enhanced S-video
- Improved chroma response/sharpness for regular S-video
- Added 3D Comb filter for NTSC composite video
- Improved PAL composite and S-video
- Improved ability to track and hold poor VHS signals
- Improved MiSTer DV/Analogue decimation detection
- Minimized glitching during horizontal resolution changes
- Added option to blank video during major resolution chanes to minimize visual glitches
- Improved S/PDIF detection
- Various bug fixes
- SD Card Image adds Wobbling Pixels profiles for Enhanced S-video plus 3D comb optimized composite profiles

<br/>


## Version 1.2.1 (2024-02-02)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/SD%20card%20images/Rt4k_121_sdcard.zip)
CRC-32: `A5021E4A`  
SHA-256: `74128161f3164c831b82f87a119b70bb657c4b6157d94b5f35600691dd870f1e`

### Changelog:
- Added special Sega Saturn auto-sampling support.
- Complete rewrite of the auto-sampling/auto-phase algorithm for improved stability for all systems.
- Complete rewrite of the inverse 3:2 and 2:2 telecine deinterlacers for improved stability and response time. Games that have moderate pace changes such as FFX should now be playable.
- Added the ability to generate pseudo-interlaced scanline (i.e. 480i style scanlines from 480p inputs, 1080i style scanlines from 1080p inputs).
- Improved Analogue DAC support including auto-calculating the decimation factor
- Fixed various HDMI audio compatibility issues including audio glitches for Atomos recorders and missing HDR infoframes when run through AVRs.

<br/>

## Version 1.1.0 (2024-01-15)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/SD%20card%20images/Rt4k_110_sdcard.zip)
CRC-32: `3338FFB0`  
SHA-256: `24fb1e3320b708df933831212032b6a5a47511f789f19c328f12f046b9e0be90`

### Changelog:
- Added MiSTer DV1 support for auto-decimating and auto-cropping video output from cores
- Enabled Auto-Cropping for HDMI® input sources
- Scanlines and masks are automatically rotated correctly when the video is rotated
- Added additional LCD effects including RGB and BGR subpixel layouts
- 'Wide Tolerance' sync mode added for sources with poor sync signals such as NEOGEO and Atari 2600/7800
- 1080p60 -> 1440p120 CVT-rb fixed
- Fixed file handling to ignore '.' files introduced by Mac OS X
- Improved audio compatibility with some displays and Atomos capture devices
- Various bug and stability fixes

<br/>

## Version 1.0 RC26 (2023-12-09)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/SD%20card%20images/Rt4k_10rc26_sdcard.zip)
CRC-32: `4D571806`  
SHA-256: `f4c7cc7334f1968e83d050dd455d85ee55e37bd0b00a03dc37634a26d9495099`

### Changelog:
- Original launch SD card image