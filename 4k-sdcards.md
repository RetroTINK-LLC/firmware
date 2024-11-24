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

## Version 1.6.9 (2024-11-24)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/SD%20card%20images/Rt4k_169_sdcard.zip)
CRC-32: `F9FBD428`  
SHA-256: `dbb7b111dd1e6e1b41bf997774cca5ed31f93da3ce0904e804a08418a9ca44f8`

### Changelog:
- Added interlaced support for RGBHV sources
- Added auto-sleep timer support (in OSD/Firmware menu, global setting saved indepedent of profile)
- Improved auto-phase algorithm that rejects the phase with ringing artifacts in favor of a phase with maximum flatness for both on-demand and continuous modes
- Added support for serial communications over HD15 and USB (virtual serial ports)
- Added commands for SVS switch profile auto-loading on new input
- Added commands to simulate remote control actions over serial port
- Fixed issues that caused glitches with S/PDIF audio inputs
- Fixed edge cases related to 240p/480i mode detection 
- Fixed issue that result in cut off pixels in 640x480 PC modes 
<br/>



## Version 1.5.4 (2024-07-21)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/SD%20card%20images/Rt4k_154_sdcardd.zip)
CRC-32: `1B098F3B`  
SHA-256: `75686dda487b0fe9cf9cfeb56e124109e71d8c58e94d60c0ce151b57a151e1f6`

### Changelog:
- Improved RGBHV mode detection
- Improved Gen Lock capture range
- Improved detection of 1080p YPbPr sources
- Fixed default trims for 720p, 1080i and 1080p analog sources
- Fixed various issues causing random glitching of HDMI output pixel order
- Added ability to pass-through HDR10 and HLG content from HDMI sources
- Added ability to auto-load DV1 profiles based on reported core name
- Added ability to alpha key masks to specify direct draw of mask color without blending
- Added ability to produce interlaced outputs (e.g. 480i, 1080i)
- Low resolution OSD rendering support to display menu when output modeline is 240p or 480i
- Fixed minor issues with analog LPF for RGBHV sources
- File selection menu remembers the sub-directory and cursor position when recalled again


<br/>



## Version 1.4.2 (2024-04-27)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/SD%20card%20images/Rt4k_142_sdcard.zip)
CRC-32: `60728C8D`  
SHA-256: `01b541e1a688548c63e6f7e86925de485dbc6c061334db22f1c201cac765fe25`

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
