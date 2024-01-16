---
layout: default
title: RetroTINK-4K Experimental Firmware
---

<h1 align="center" style="margin-top: 0px;">RetroTINK-4K Experimental Firmware</h1>

<p style="margin:30px;"></p>

<h2 align="center" style="margin-top: 0px;">⚠️ CAUTION: Read carefully before proceeding ⚠️</h2>

<p style="margin:10px;"></p>

### For the initial update from the launch 1.0 RC26 firmware, it is recommended to update using the reset button method rather than through the menu.

<p style="margin:10px;"></p>

## THE FIRMWARE CONTAINED IN THIS DIRECTORY IS PRE-RELEASE. PROPER FUNCTIONALITY IS NOT GUARANTEED, AND FEATURES MAY STILL BE IN DEVELOPMENT.

<p style="margin:20px;"></p>

## Instructions️

1. Power off your RetroTINK-4K and remove the SD card.
2. Insert the SD card used for your RT4K into the SD card slot on your computer. If your computer doesn't have an SD card slot, you can connect it using the provided USB adaptor.
3. Download the .zip file of the firmware you want from the RetroTINK website.
4. Extract the contents of the .zip file to the SD card's root directory. Be sure to replace the existing "rt4kup.bin" file, as this is used to determine which firmware to install.
  - If you intend to update via the RT4K's menu, do not delete the old \*.rbf firmware file. If you do, you'll be forced to update via the Reset button method (see Step 6 below for how to do this).
5. Remove the SD card and insert it into the SD card slot on the RetroTINK-4K.
6. There are two methods for initiating the firmware installation. The RT4K installs firmware based on the "rt4kup.bin" file.
  - Option 1: Power on the RetroTINK-4K, then go to Advanced Settings > OSD/Firmware. In the Firmware update section, select "Check SD Card" to scan for the firmware file, then confirm that you want to install it.
  - Option 2: Hold down the blue Reset button on the back of the RetroTINK-4K, then power it on. The firmware installation will begin automatically.
  - If the LED blinks red, an install error has occurred. Check the files on the SD card and try again.
7. The RT4K will reboot for about 40 seconds, with the front LED flashing pink and then blue. Once done, it will power on again as normal with a green LED. You're done!

All custom profiles, CSC files, banner images, input modes, mask overlays and modelines will be kept, as those are stored on the SD card instead of on the RT4K itself. 

<p style="margin:41px;"></p>

## Version 1.1.3 (2024-01-14)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_113.zip)
CRC-32: `81CF9156`  
SHA-256: `35d5cde045f8d6013716fde0c9cdd7d15b20b6c88ad408524b93b866618a9d25`

### Changelog:
- Improved auto sampling algorithm

<br/>

## Version 1.1.2 (2024-01-14)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_112.zip)
CRC-32: `EE25E88F`  
SHA-256: `2180d0b8b95ab65eea6d2aabdf5f7f92fe7fbd856080b4c6c1047dc28038a2ba`

### Changelog:
- Saturn mode now uses 427*7 and 455*8 as basis to have unique slots
- Improved 320/640 detection algorithm, may also benefit PS1 (for PS1 use LPF = 35 MHz)

<br/>

## Version 1.1.1 (2024-01-13)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_111.zip)
CRC-32: `C26A7E1E`  
SHA-256: `1e6d6ad5029f2aaf03068f227b3f2e7ceb9bdcba81df31a3d542613e8bf689f2`

### Changelog:
- Added Saturn auto-sampling mode
- Saturn modes only enable 320/640, 352/704 detection
- Fixed possible bug with determining low vs high resolution modes
- Increased threshold to switch between 256/512 and 320/640 modes
- Fixed page number bug in status screens
- Increased delay before IR remote repeat hits
- Left and Right jump 5 spots in the file manager

<br/>

## Version 1.0.9 (2024-01-09)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_109.zip)
CRC-32: `591B36DE`  
SHA-256: `b0f43eec664228ae38ee33244414fa821225244ca949f76779d6a953a7f537b7`

### Changelog:
- Adjusted FPGA timing for HDMI 1.4
- Increased FPGA to HDMI drive strength
- Full shut down of Wide Tolerance mode when not in use to improve loop time
- Reduced SDP output drive strength

<br/>

## Version 1.0.8 (2024-01-08)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_108.zip)
CRC-32: `E07A9083`  
SHA-256: `2b0acf9ffef00cacca9d20ee4563302cac7a983f3612a9edfe0e899d9ec71b50`

### Changelog:
- "Wide Tolerance" added to Video ADC Menu
  - Replaces older Slow Lock Function
  - Helps lock on to badly behaved sources like NEOGEO and Atari 2600/7800
  - Should be left off unless needed. May have unintended side effects for normal sources  
- Fixed cop for new LCD modes to lock out H. Interp options
- Fixed proper half-phase offset in rotational modes since H and V kernel controls are swapped in RoTaTE
- MiSTer DV1 controls broken out
  - Auto decimation can be turned off
  - Auto crop can be turned off  
- MiSTer DV1 core name now displayed as part of mode name
- HDCP only activates after a few seconds of continous raw HDCP frames detected

<br/>

## Version 1.0.6 (2024-01-06)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_106.zip)
CRC-32: `37239B54`  
SHA-256: `101f04d990ed526e213dbdcc4e69219213db1033513afee79062b58da8721c25`

### Changelog:
- Interpolation, Scanline, LCD and Mask effects automatically rotate CW or CCW when RoTaTe is on
- Forced PAR and allow DAR to OFF for MiSTer Generic DV1
- Compensated for decimation change when MiSTer menu is open in 1:1 PAR mode
- Unlocked Auto-crop controls in menu for HDMI sources
- New LCD effects
  - Second mono LCD pattern with adjustable horizontal size
  - GBR and RGB patterns
- Fixed RoTaTe CW crop bug
- 1440p120 changed to CVT-rb timing
- 4K50 and 1080p50 changed to CEA-861 with extra blanks instead of using their 60 Hz versions
- Changed HDCP Alert

<br/>

## Version 1.0.5 (2024-01-06)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_105.zip)
CRC-32: `00120576`  
SHA-256: `ebfcf42ea3235912dc09320717ece0d3ca159274de2d11474ed3f858599973c8`

### Changelog:
- Enabled auto-crop for HDMI sources
&ensp;- AUX1 - vertical trim only
&ensp;- AUX2 - crop active and stretch to 4:3
&ensp;- AUX3 - crop active and stretch to 16:9
- Adjusted auto-crop algorithm
- 1080p -> 1440p120 CVT-rb works now

<br/>

## Version 1.0.4 (2024-01-03)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_104.zip)
CRC-32: `54E2FFA3`  
SHA-256: `217c6727827540a60098d00905667ba5df95c8d5a9141700f31ed5478ab6e941`

### Changelog:
- Fixed hidden '.' file bug introduced when using the SD card with Mac OS X.
- MiSTer DV1 detected and parsed
  - Can be disabled in HDMI RX menu, default on
  - Automatically tunes the crops (if core provides info) and takes control of the decimation factor
  - New HDMI modes entries added for MiSTer DVI (240p, 288p, 480i, 576i and unknown/generic)
  - https://github.com/MiSTer-devel/Main_MiSTer/issues
- Added 32 kHz audio sample rate detection (diagnostics page needs to be fixed, since it still displays 44.1 kHz)
- Various FPGA optimizations and added the ability to override DE with DV1 info

<br/>

## Version 1.0.2 (2023-12-15)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_102.zip)
CRC-32: `922ADAA0`  
SHA-256: `2696b2541358e536debf4108c7336a040f690b4fc833fa7afa89282a7311301e`

### Changelog:
- Fixed file handler to ignore files/directories that start with '.'
- Added warning when disabling BFI minimum frame rate limit
- Fixed auto-decimation bug with PS1 MiSTer core
  - NOTE: Because MiSTer does not send the correct de-repetition (along with crop) meta data, you will need to manually set it in the HDMI receiver menu.
  - Usually Input Pixels = 4/Output Pixels = 1 is sufficent unless you need 1:1 PAR modes (i.e. emulating LCD) in which case, you will need to figure out the exact number

<br/>

## Version 1.0.1 (2023-12-12)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_101.zip)
CRC-32: `776145AB`  
SHA-256: `e9a297cc1a811949b86ff1a7a57a6b8bbbd6a94980779921c899f600fe478380`

### Changelog:
- Fixed SD card read freeze bug due to unexpected read latency/timeouts
- blizzz's name fixed
- Option to disable min. BFI rate cop`