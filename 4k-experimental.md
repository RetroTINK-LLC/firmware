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
  - Option 2: Hold down the blue Reset button on the back of the RetroTINK-4K, then power it on. The firmware installation will begin automatically. **NOTE: As of experimental firmware 1.6.0, if you wish to use the reset button method, you must unplug the RT4K from power, hold the reset button, and plug the power back in.**
  - If the LED blinks red, an install error has occurred. Check the files on the SD card and try again.
7. The RT4K will reboot for about 40 seconds, with the front LED flashing pink and then blue. Once done, it will power on again as normal with a green LED. You're done!

All custom profiles, CSC files, banner images, input modes, mask overlays and modelines will be kept, as those are stored on the SD card instead of on the RT4K itself.

<p style="margin:41px;"></p>

## Version 1.8.6 (2025-06-07)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_186.zip)
CRC-32: `1AF32B66`  
SHA-256: `5450073d9a0d983214d292cbdec6d7e2bac80b0ea0498ee843ff3589254569ce`

### Changelog:
- Fixed audio balance min/max bug
- Fixed Decimation control GUI display bug for the RT4KCE when auto sampling is enabled
- New analog pixel edge detection algorithm to align decimation phase selection, minimizing annoying horizontal shifts when auto-phase selects a new phase position

<br/>



## Version 1.8.5 (2025-06-05)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_185.zip)
CRC-32: `1564376C`  
SHA-256: `0101f1612eaddbeb509c689846ac2ef501d1d71f847a759aaa0ae4a4298227fa`

### Changelog:
- Added audio right/left balance control for analog sources

<br/>


## Version 1.8.4 (2025-06-04)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_184.zip)
CRC-32: `428D1FFA`  
SHA-256: `4860b93ac6adac84f29bbfbcf8456dbbcfad850e3ecc31263fc58b681813860c`

### Changelog:
- Added audio VU (peak) meter to the audio input menu
- Real time display of audio levels for analog audio inputs to help identify clipping
- RT4KCE looks for 'default_ce_fbx.bmp' (thank you FirebrandX for cleaning up the banner)
- Banner supports 1 layer of subfolders

<br/>



## Version 1.8.3 (2025-05-30)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_183.zip)
CRC-32: `AC5053C3`  
SHA-256: `d5d046438492397a2c14684af5d17504f7fba982905f9451eb7332270e019e07`

### Changelog:
- Added de-blur function for Decimation Factors 8/4
- Enabled in Sample Date Detection Menu -> De-blur Dec. 8/4
- Analyzes image to see if Decimation Factor 4 (e.g., N64 640 wide) is the result of simple bilinear upscaling
- If bilinear upscaling is found, Decimation Factor 8 will be used (e.g., de-blurring N64 640 -> 320)

<br/>

## Version 1.8.2 (2025-05-24)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_182.zip)
CRC-32: `4628B522`  
SHA-256: `4bf2a7b005b7b245d2ded9a2af9a13db2ef350b03ea7c38a67de4b5606d7284b`

### Changelog:
- Added 192 kHz and 384 kHz analog audio sample rates
- 384 kHz may be out of spec
- Audio gain levels now equalized between 48 kHz, 96 kHz and 192 kHz
- Fixed bug where changing the audio sample rate resets the gain

<br/>

## Version 1.8.1 (2025-05-19)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_181.zip)
CRC-32: `A90953B5`  
SHA-256: `aa5d0cc2f08f298cd875b3310ae1ffd1f01445f6f51e20dca83c7926956b973d`

### Changelog:
- Expanded CRT beam sim from 1:4 to 1:8 (output frame rate can be 8x input)
- Clean up of auto phase algorithm to reject false positives
- On demand autophase and continuous autophase use identical methods

<br/>

## Version 1.8.0 (2025-04-19)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_180.zip)
CRC-32: `749BA614`  
SHA-256: `96749cd92dc56f36e0b8da89fa0077fc46409bae9dfd091463dbe7edc728bbc7`

### Changelog:
- Internal bug fixes
- Addressed issue with green lines in SDP mode (found in a small number of units)

<br/>

## Version 1.7.9 (2025-03-30)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_179b.zip)
CRC-32: `45052FFE`  
SHA-256: `15559087d48504e01af83dc7e05e27b5b5c6b6333cc6eb79be3435a4fbe7ee77`

### Changelog:
- Further internal optimizations

<br/>

## Version 1.7.8 (2025-03-26)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_178.zip)
CRC-32: `4464E165`  
SHA-256: `595a500ce0818fd2394153c06a7b476cf15ccce4696a0020226a983fdf124679`

### Changelog:
- Modified sync thresholds further

<br/>

## Version 1.7.7 (2025-03-21)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_177.zip)
CRC-32: `BE9653A4`  
SHA-256: `57a3b0f3ca864bb829c26404fa47fda2648f0327313f518d2ca24d7c42b3bced`

### Changelog:
- Modified sync processor settings

<br/>

## Version 1.7.6 (2025-03-01)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_176.zip)
CRC-32: `A4CB5124`  
SHA-256: `9b5cbbda68877334233603b7ea5f3b215c56676c4d020aec228dbd01f4752273`

### Changelog:
- Fixed some issues related to audio and HDR glitching through HDMI switches

<br/>

## Version 1.7.5 (2025-02-27)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_175.zip)
CRC-32: `C4F55C29`  
SHA-256: `d1db97f67d1b094b2f87218c876e46d89d96a3c8ec02a70fbd4e9c3c4f06b5fb`

### Changelog:
- Fixed line bug in RT4KCE
- More internal optimizations
- Tuned inverse 2:2 to reduce false unlocks.

<br/>

## Version 1.7.4 (2025-02-17)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_174.zip)
CRC-32: `A7C07F7A`  
SHA-256: `9ad552b6880d686d513b764d8ce7ffcdf464491ec42a3bb981c67ff688696ae2`

### Changelog:
- Internal fixes and optimizations
- Added RT4KCE image to this package

<br/>

## Version 1.7.2 (2025-01-11)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_172.zip)
CRC-32: `2EA850F2`  
SHA-256: `bb2c56f963379e02e723b7b9d8d54284779c7efce380cd9aebe0da1a5e8cc1e9`

### Changelog:
- Added Beam Steepness and Phospher Glow controls to Rolling BFI
- Higher Beam Steepness results in less blending between each phase for increased motion clarity but more tearing
- Phospher Glow implements a version of Timothy Lottes MPRT to simulate phospher decay and restore lost brightness but higher levels reduce motion clarity
- Added explicit phase resynchronizer to unify the inverse 3:2 and 2:2 counters
- Fixed edge crop shift due to new pipeline additions

<br/>

## Version 1.7.1 (2025-01-06)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_171.zip)
CRC-32: `EF416BB1`  
SHA-256: `48a9f11a84a5a3cdb1d446fd1ce79dac2a245d5099c2d928fac23116c10fe28f`

### Changelog:
- Added CRT Beam function to the list of BFI Blending modes to generate a rolling BFI
- CRT Beam requires pipeline to have the correct input gamma and output gamma to be set (usually 2.2 - 2.4) or in HDR mode
- Fixed null pointer bug when decoding 'remote' serial commands with no argument
- Added cop to disable previous field reads when Bob deinterlacer is used

<br/>

## Version 1.7.0 (2024-11-27)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_170b.zip)
CRC-32: `4D8EC4B6`  
SHA-256: `61a986f27ced4556250c726d8e6d1cadd2adbc6c96e58ae65e74e028325a9137`

### Changelog:
- Modifed S/PDIF sample rate detection

<br/>

## Version 1.6.9 (2024-11-09)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_169.zip)
CRC-32: `40B12EFC`  
SHA-256: `10edb752f03b22624fc2e2e6782752711865dcc83ca9f554028940489e7cfce7`

### Changelog:
- Re-ordered SVS IR code command
- Enabled BFI strobe factors that are not power of 2
- Clean up of string code

<br/>

## Version 1.6.8 (2024-11-03)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_168.zip)
CRC-32: `66248CB5`  
SHA-256: `ce239e4c9adf2d3cfb179e67c07ba5aae41de5111929bfbffe69c620380c44d8`

### Changelog:
- Cleaned up IR remote control codes to conform with NEC standard
- Diagnostic screen now reports IR address and command instead of raw bit pattern
- Custom IR command set can be loaded from the SD card by putting the file 'ir_command.txt' on the SD card root
- Fixed profile menu bug where power on profile was cut off
- Fixed minor bug in SVS auto load profile name
- Added ability for SVS switch to emulate IR commands over serial

<br/>

## Version 1.6.7 (2024-11-02)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_167.zip)
CRC-32: `47AF742A`  
SHA-256: `d2fd46f04495992fad8cb1787ef1e3e0ab53e34fbcf04220d7fc40023ceb0f4b`

### Changelog:
- Added support for SVS switch auto-loading
- Similar function to DV1 (auto-loading enabled in the 'Profile' menu)
- When SVS signals new input, RT4K checks the /profile/SVS subfolder for a matching profile
- Profiles need to be named: 'S\<input number\>_\<user defined\>.rt4'
- For example, SVS input 2 would looke for a profile that is named S2_SNES...rt4
- If there's more than one profile that fits the pattern, the first match is used
- Other devices may also use this system by sending SVS commands through either serial port
- SVS NEW INPUT=\<input number\> triggers an auto profile load
- SVS CURRENT INPUT=\<input number\> is a keep alive signal that tells the RT4K a switch is connected. This should be sent ~1-2 seconds

<br/>

## Version 1.6.6 (2024-11-01)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_166.zip)
CRC-32: `E65DEB58`  
SHA-256: `92C9397A6921EEED05C9A9C8FDA1BD31E01367131F1F7F9E5EA056F3308AB0B9`

### Changelog:
- Added serial command infrastructure over HD15 and USB
- HD15: RT4K TX on Pin 12, RT4K RX on Pin 15, 9600 bps 8-N-1, open drain
- USB: FTDI RT232R, 115200 bps 8-N-1

<br/>

## Version 1.6.5 (2024-10-20)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_165.zip)
CRC-32: `F76A00A3`  
SHA-256: `9cd7cc27c2fe9a307c30b81750037ae451ead590acb3b67009e6b7ef87da6c73`

### Changelog:
- Slight modification to 240p and 288p sync processing
- Auto auto-phase (the one used for auto decimation/auto sampling) now uses the same dynamic gradient flow optimization as the manual auto phase from 1.6.3 to minimize ringing

<br/>

## Version 1.6.4 (2024-10-19)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_164.zip)
CRC-32: `E66A5BD2`  
SHA-256: `6e73acf54b4ed616dca909f827cbd4c21296cc8c38d4b82b6ce521bef4b5941c`

### Changelog:
- Gen-Lock now uses new algorithm with enhnaced frequency locking and glitch minimization
- May help prevent further video/audio drops during frame rate changes on picky equipment such as Avermedia capture cards

<br/>

## Version 1.6.3 (2024-10-17)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_163.zip)
CRC-32: `D5312BE2`  
SHA-256: `2ACA22CB2AF1FE75D6255E59AE19ACAC0DBE2B670FFFD3CF1D1C13EF2F8BFF0C`

### Changelog:
- Adjusted *manual* auto-phase algorithm to look for valid phases that do not have ringing artifacts
- Fixed cut right pixels in 640x480p60 PC mode

<br/>

## Version 1.6.2 (2024-10-11)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_162.zip)
CRC-32: `D2B55610`  
SHA-256: `691B47BAB39ECB6743D6C7F6D9FFBB12F8C9C2C512B3EA3ADE2F3D514F5481DA`

### Changelog:
- Discovered and fixed some cases where 240p -> 480i was not being detected correctly
- Auto sleep now has a warning and can be cancelled with a button press

<br/>

## Version 1.6.1 (2024-10-03)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_161.zip)
CRC-32: `A67E183E`  
SHA-256: `30AEDA50A5805709B2AF72C416BF085B5AB353B0FAB51A24F0512BABCD523DE4`

### Changelog:
- Possible fixes to various sleep/auto power glitches
- Fixed some bugs that was causing S/PDIF sample rate to be detected incorrectly possibly leading to audio glitches

<br/>

## Version 1.6.0 (2024-09-28)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_160.zip)
CRC-32: `0335A147`  
SHA-256: `1f5fdd17317eef0129a2d85a3be5ff6d948da68c509e5c8772e426d2b84a35ce`

### Changelog:
- Added auto-sleep timer if no signal is detected for a specified length of time
- Added the ability to default to sleep on cold boots (inserting USB power)
- Settings are in the OSD/Firmware menu
- Settings are saved on the SD card and are global, not profile specific

<br/>

## Version 1.5.9 (2024-09-27)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_159.zip)
CRC-32: `31852AC7`  
SHA-256: `B9A49541FC93C654C6D07231B3297A02832387B12B7B7206FDF38A48FEED7891`

### Changelog:
- Reconcilled various sync adjustments for 480i, 576i and 1080i on RGBHV
- Fixed various collateral damage due to accomodating interlaced video in RGBHV

<br/>

## Version 1.5.8 (2024-09-24)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_158.zip)
CRC-32: `CDE56C85`  
SHA-256: `FC1196709343B7CEB5945EF511D1CDB301A6E268440174B09544CC15C99704DB`

### Changelog:
- Fixed 576i detection in RGBHV mode
- Added placeholder for Legal/Regulatory notices

<br/>

## Version 1.5.7 (2024-09-23)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_157.zip)
CRC-32: `B3FE25CC`  
SHA-256: `B292BFC8D976181603795365618AD546B0EB8FF376D6606AB0B0D898B3D0C823`

### Changelog:
- Fixed quirks that stopped interlaced video from RGBHV sources

<br/>

## Version 1.5.6 (2024-07-24)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_156.zip)
CRC-32: `6A5F1615`  
SHA-256: `80107dca81fb5bc1f73226f72da097f14885bc4e6adc1a28a58c43ae3608168f`

### Changelog:
- Audio auto-mute only active when HDMI IN is the active audio source
- Fixed bug where saving new profiles not not refresh the file load selection menu
- Added built in support for detecting 1366x768 PC resolution

<br/>

## Version 1.5.5 (2024-08-04)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_155.zip)
CRC-32: `00C24B25`  
SHA-256: `b4a4fe2306d2b639978652eedde22a741d78d2c21df538df3b53bea9f6209680`

### Changelog:
- Auto mutes audio output when there is no video signal to prevent garbage being injected into the sound
- Fixed inverse 2:2 cadence break

<br/>

## Version 1.5.4 (2024-07-20)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_154d.zip)
CRC-32: `D246896D`  
SHA-256: `648de38e6678bbd523212ca057f58683d383dbaa209fa570159888aea1f80ad6`

### Changelog:
- File selection box remembers previous sub-directory and cursor position when recalled again

<br/>

## Version 1.5.3 (2024-07-17)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_153.zip)
CRC-32: `CB28EB9D`  
SHA-256: `B20E8A3E520FC631BDF34394AE06EB510F27BE7E6E0C37154ECD8186C5097299`

### Changelog:
- Minor change to VGAHV input mode to optimize LPF performance at high input resolutions
- May become official release if no problems observed

<br/>

## Version 1.5.2 (2024-07-14)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_152.zip)
CRC-32: `B78FB41F`  
SHA-256: `60841e9f6309f0638348a244c9073af44c17a2be7868cfd411988513ef8e30ef`

### Changelog:
- Added logic to properly handle Gen-Lock and Frame-Lock so that sync happens on the correct field
- Deinterlacer controls have no effect when the output is also interlaced
- Shifted mask by one pipeline clock

<br/>

## Version 1.5.1 (2024-07-12)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_151.zip)
CRC-32: `E63E310C`  
SHA-256: `b95462b4c6af74b6b9284cc67b311a8cfcc55428d44344ccaa1655c9b88769a6`

### Changelog:
- Added ability to generate interlaced output timings (see modeline examples below)
- Note the vertical active size is defined as the total of both fields, whereas the porch and sync are defined by f0
- Menu now works in 240p output using temporal downscaling
- HDMI output automatically enables pixel repeat for low clock rates
- Example modelines below:
- 1920, 88, 44, 280, 1, 1080, 2, 5, 22, 1, 59.94, "1920x1080i59.94", 1
- 720, 16, 62, 138, 0, 480, 4, 3, 22, 0, 59.94, "720x480i59.94", 1
- 720, 16, 62, 138, 0, 240, 4, 3, 22, 0, 60, "720x240p60"

<br/>

## Version 1.5.0 (2024-06-30)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_150.zip)
CRC-32: `D694AB62`  
SHA-256: `07c257ee52fef2677aff8a70218e36cba67990a9a0e95447f339b434e8e49c8c`

### Changelog:
- Replaces 1.4.9
- Fixes error in .bmp importer

<br/>

## Version 1.4.9 (2024-06-30)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_149.zip)
CRC-32: `A63568F3`  
SHA-256: `39bb2edfa67585cd6c8062095cc1b09dd5f1f2f6e0695dc71eaab8c66e80581d`

### Changelog:
- Added alpha keying for masks
- Masks must be saved as 32-bit .bmp files
- Any pixels with the alpha layer having an intensity of 105 (0x69) will be drawn exactly as-is with no blending
- All other codes or absence thereof will be treated as before (full backwards compatibility)
- See 'DMG-115x_alpha.bmp' as an example (credit to billgonzo for original)

<br/>

## Version 1.4.8 (2024-06-23)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_148.zip)
CRC-32: `C91F07DD`  
SHA-256: `88cd08726be5a096a5ce959279e6b7cffd88930f4a8e1d17127c9fff552319fb`

### Changelog:
- Fixed EDID issues related to HDR and causing DVI only operation
- Disabled 3D comb when S-Video is used

<br/>

## Version 1.4.7 (2024-06-05)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_147.zip)
CRC-32: `6262C9FE`  
SHA-256: `D7FCAA51191271BCE7CC6FC07027F95BC49976C81C27B76E6C2533AA3039C561`

### Changelog:
- Added the ability to pass HDR10 and HLG from input to output
- RT4K EDID modified to allow for HDR sources
- When HDR sources are applied, all color correction controls are disabled
- Added the ability to auto-load DV1 profiles
- If enabled, will check for a profile with the name that matches the core name in the DV1 sub-folder (for example SNES Core = /profile/DV1/SNES.rt4)
- More multi-fpga internal optimization

<br/>

## Version 1.4.5 (2024-05-11)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_145.zip)
CRC-32: `2D22BA6B`  
SHA-256: `62db970b9608e93c266925346e62d7ed9ac5a90b28ff92ba43862a4f0ea355d8`

### Changelog:
- Minor update
- Added groundwork for multi-FPGA image support
- Automatic detection of out-of-order HDMI output and reset

<br/>

## Version 1.4.4 (2024-05-09)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_144.zip)
CRC-32: `7A415229`  
SHA-256: `7dfae4c388e44b8af86392ca3b831f3567af9a4f5facd2b5356817525d9c54c9`

### Changelog:
- Fixed bug preventing 1080p YPbPr detection
- Improved overall analog sync processing reliability
- Adjusted default trims for 720p, 1080i and 1080p to eliminate left hand black edge

<br/>

## Version 1.4.3 (2024-05-06)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_143.zip)
CRC-32: `DA2A24C7`  
SHA-256: `b42db528b24b9872fd4089e8243545baf259ca640046268cad9b96ec2d277bae`

### Changelog:
- Improved detection of PC/RGBHV sources to reduce false "Unknown" mode states
- Increased GENLOCK capture range to +19% to capture 70 Hz DOS sources with a 60 Hz modeline (reminder 4K70 is not supported)

<br/>

## Version 1.4.2 (2024-04-27)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_142.zip)
CRC-32: `60728C8D`  
SHA-256: `0be711173c5b22b82d9b1643f01f7518bf07e22ce9bc2c7a9e24ab936aecbcc2`

### Changelog:
- High precision IIR filter to minimize ghosting
- Fixed 3D comb bug in 240p modes
- Candidate for next "Official" release (again)

<br/>

## Version 1.4.1 (2024-04-13)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_141.zip)
CRC-32: `03D8232C`  
SHA-256: `c1ed61c62699dbf7b9959cce9a340b8016ff3a3e25beb2e1346669ba853a8e42`

### Changelog:
- Improved low angle detection
- Candidate for next "Official" release 

<br/>

## Version 1.4.0 (2024-04-12)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_140.zip)
CRC-32: `7656C43A`  
SHA-256: `69cd773e749c3e634e76a78ec19bd913158e58e50a0970e6a6e6bd5bbe5b64ba`

### Changelog:
- Edge Adaptive deinterlacing status moved to "no longer disapproved by Extrems"
- Fixed various edge case failures of the new MADI related to MiSTer DV1 and high output frame rates
- Modified Freesync VRR metadata
- Added VESA VRR injection
- Improved output Gamma/PQ quantization (thanks Extrems for contributing the code)
- Candidate for next "Official" release 

<br/>

## Version 1.3.9 (2024-04-10)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_139.zip)
CRC-32: `A9629C97`  
SHA-256: `b1b61de04f32c8d8faa7e5331ebc688941ab51fb53db4f20e72eb42dcb17b284`

### Changelog:
- Further improvements in Edge Adaptive deinterlacing
- Reduction in artifacts and wrong edge selections
- This feature is still not Extrems Approved (tm), pls no troll

<br/>

## Version 1.3.8 (2024-04-09)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_138.zip)
CRC-32: `29B7D33B`  
SHA-256: `53fbad0ce852709ed8100825dded823c479b4789f5c15b1974866cef94d1a308`

### Changelog:
- Improved Edge Adaptive deinterlacing
- This feature is not Extrems Approved (tm), pls no troll

<br/>

## Version 1.3.7 (2024-04-02)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_137.zip)
CRC-32: `748AB716`  
SHA-256: `bc343aaba8b1e818292e39020d80ad49e9bcff11b5679a12182c64b39f27e9f2`

### Changelog:
- Added Edge Adaptive (WIP) interpolation for Motion Adaptive Deinterlacer
- "Interpolator" options are now: Linear (Bob) and Edge Adaptive (Smoothed Bob)
- Edge Adaptive interpolation can signficantly improve image quality, especially for 3D games and eliminate the "jaggy" effect during motion
- Max threshold added back in

<br/>

## Version 1.3.6 (2024-04-01)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_136.zip)
CRC-32: `A0337A45`  
SHA-256: `4fe67d58280d160c24ef8aeb1ed1bd1d8c1a70e573dd52a5de74931b40b1e6a7`

### Changelog:
- Early build of next-generation Motion Adaptive Deinterlacer
- Enhanced motion-vector estimation
- False combing nearly eliminated
- Tuned thresholds per the Intel VIP Suite documentation
- "Max" sensitivity for MA removed
- Default "Noise Threshold" now 0

<br/>

## Version 1.3.5 (2024-03-25)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_135.zip)
CRC-32: `8413FD44`  
SHA-256: `e41ee680f9958812126bf88ee89e1cad540b4a360df6ed272953d02d8593edf9`

### Changelog:
- Added HLG HDR implemention with proper color conversion and perceptual quantization
- For HLG, the Input Gain control under the "Color Correction" menu should be used to tune the intensity

<br/>

## Version 1.3.4 (2024-03-15)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_134.zip)
CRC-32: `8ED35E79`  
SHA-256: `e07f92bcbe02cde0769add99b18b59d7acc4d74c1f9b712d0460bf31aae0d3f4`

### Changelog:
- Fixed small OSD bug in 1080p

<br/>

## Version 1.3.3 (2024-03-13)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_133.zip)
CRC-32: `A7F56A75`  
SHA-256: `b811621c6fba8e6729c0acca6b658593192ef4421cfd7b48efa309cf931db46e`

### Changelog:
- PAL Line Averaging automatically disabled for non-PAL sources
- Enc. -> Enh. S-video
- Fixed repeated line at the top of the screen when scanlines are on

<br/>

## Version 1.3.2 (2024-03-09)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_132.zip)
CRC-32: `18A6D047`  
SHA-256: `ecf965ad42f3d43ef13f1c4dd51269d45633d2589566c81e3ff8c0b027ca5a98`

### Changelog:
- Fixed bug that broke enhanced S-video luma/chroma registration for NTSC-type sources

<br/>

## Version 1.3.1 (2024-03-08)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_131.zip)
CRC-32: `94376E67`  
SHA-256: `7932a3e5603eef581c72721edefa4fb6847e52c50e6c1cacfb65d27eab036a0a`

### Changelog:
- 3D comb and 2D Y/C modes are separate options to allow the user to select which 2D mode is used as a fall back during motion
- 3D comb enabled for 240p sources to improve image quality for systems like the NES and TG16 and eliminate composite jitter in captures/triple buffer
- It may be useful to increase the 3D Noise Threshold for game consoles vs regular video
- Fixed bug where SDP standard was not reported in enhanced S-video
- Recalibrated enhanced S-Video for both NTSC and PAL
- Default Chroma Bandwidth changed to 'High'
- Massively improved chroma response for both regular S-video and enhanced S-video
- Blank change res default off (can interefere with wonky sources like atari or VHS). Turn it on only if you NEED it
- Added option to disable PAL delay line

<br/>

## Version 1.3.0 (2024-03-02)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_130.zip)
CRC-32: `49D64C8E`  
SHA-256: `41c898130cb88fa46431ef64ebd9492eeecd2a4ef6e4a34f6f97c83650c5febf`

### Changelog:
- Cleaned up thresholding controls for the 3D Comb
- Low setting quickly falls back to 2D mode, while the Medium and High settings favor the 3D mode
- The default setting for the 3D comb is somewhere between Low and Medium
- Fixed bugs that prevented 3D comb and Inverse Telecine from working together
- Inverse 3:2 Telecine might need the 3D comb to be set to Low or Default to prevent artifacts
- Normal video can use a higher threshold to aggressively remove composite video artifacts
- Further optimizations in Inverse 2:2 Telecine to minimize glitches during cadence changes
- Calibrated Enhanced S-Video for PAL
- Automatic detection of S/PDIF signal loss and auto-reset 

<br/>

## Version 1.2.9 (2024-02-29)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_129.zip)
CRC-32: `9142EEC1`  
SHA-256: `3d9f6f339f639f56e0d27b0ad27255cfd5c5029b554e348e5e244f9819ee3214`

### Changelog:
- Complete re-write of the 3D comb filter algorithm
- 3D comb now searches multiple fields for motion and across both luma and chroma
- Improved analog noise rejection for XBR smoothing filter
- Overall optimization of FPGA to free up multipliers and RAM

<br/>

## Version 1.2.8 (2024-02-26)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_128.zip)
CRC-32: `B8FA90A5`  
SHA-256: `9f50948668214246fb2ae3d641a1b096e215005b1d08f3003881c6744e7b99fc`

### Changelog:
- Reverted Gen Lock optimization code to 1.2.4
- Fixed incorrect field ordering in the Inverse 2:2

<br/>

## Version 1.2.7 (2024-02-24)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_127.zip)
CRC-32: `9C477D57`  
SHA-256: `e7e60c51e074f88f14951cd833c1268719a111cd3a159aa822308c5195c950d4`

### Changelog:
- Hard resolution changes (i.e. 240p <-> 480i) are detected and masked to provide a smoother experience
- Default on, this can be disabled in the scaling menu (Blank Res. Change)

<br/>

## Version 1.2.6 (2024-02-20)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_126.zip)
CRC-32: `B8FA90A5`  
SHA-256: `9f50948668214246fb2ae3d641a1b096e215005b1d08f3003881c6744e7b99fc`

### Changelog:
- No signal threshold for SDP sources increased
- Default color for the SDP decoder and HDMI RX now black (this is seperate from the RT4K blanking/crop color)
- Fixed bug that stopped inverse telecine from working for certain lower resolution sources
- Chroma offset control for Enhanced S-video is back

<br/>

## Version 1.2.5 (2024-02-18)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_125.zip)
CRC-32: `1CCC365F`  
SHA-256: `de914a94ab740515ae65d45400709debf13a155a4941e49cba16be069b86aeae`

### Changelog:
- Cleaned up XBR smoothing filter
- XBR now has two modes: Level 1 (45 degree angles only) and Level 2 (30 and 60 degree angles).
- XBR now has multiple options for analog noise control

<br/>

## Version 1.2.4 (2024-02-14)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_124.zip)
CRC-32: `E33EC9FB`  
SHA-256: `fcd9a1a7a44f02807585bc0b10c7b5ee564932133f3cd3a61b0d92529887941f`

### Changelog:
- Fixed MiSTer Decimation  Control locking out when Decimation Mode is set to manual
- Fixed CRT Sim mode
- Very rough draft of XBR smoothing filter (in the Image Proc. Menu)

<br/>

## Version 1.2.3 (2024-02-11)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_123.zip)
CRC-32: `E1751263`  
SHA-256: `6dc61b8c91f86898dfea3d55c36134ccaa345657e70c20ad5577fc000166e858`

### Changelog:
- Enhanced S-video detects and auto-aligns the luma and chroma offsets
- Enhanced S-video default chroma offset tuned across multiple sample rates
- Scaler changes are now fully buffered and synced
- Auto-sample/decimation changes for analog signals should now be smooth
- MiSTer/Analogue direct video decimation changes (i.e. when the Menu OSD opens) should now be smooth

<br/>

## Version 1.2.2 (2024-02-06)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_122.zip)
CRC-32: `7FAADF53`  
SHA-256: `e3eda87357be35996ea0060cfbbffcc598c744b97eb75837cbf5586d23964f46`

### Changelog:
- [NEW FEATURE] Enhanced S-Video with far higher luma resolution than standard decoders
- Avalible for S-video connections on the HD-15 port ONLY
- Added full interpolation of Cb and Cr channels compared to the version in the beta firmware
- Consider it highly experimental
- Improved Analogue auto-decimation
- MiSTer menu core auto disables decimation
- MiSTer DV1 auto-decimation now has two modes: Infoframe uses the DV1 infoframe sent by the core. Measure dynamically analyzes the image and calculates the decimation without relying on metadata.
- Automatically falls back to Measured value in case core provided information is not avalible

<br/>

## Version 1.2.1 (2024-01-28)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_121.zip)
CRC-32: `2A552631`  
SHA-256: `63ab8f92aee6689733711a7547bbeb1cbde1e6a5e256174cb814851960220cba`

### Changelog:
- Complete re-write of Inverse 3:2 algorithm
- Inverse 3:2 deinterlacer far more responsive and stable for 480i sources
- Futher optimization of Inverse 2:2 deinterlacer (FFX playable?)
- Added ability to turn off auto decimate for A/DAC mode

<br/>

## Version 1.2.0 (2024-01-26)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_120.zip)
CRC-32: `A61D5BD2`  
SHA-256: `b0665343c644453b0e4927f54b6da25de24f85a2f23e1b61b4248c9936124659`

### Changelog:
- Further complete overhaul of the inverse 2:2 telecine deinterlacer
- Lowered minimum frequency range for Gen Lock / Frame Lock

<br/>

## Version 1.1.9 (2024-01-26)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_119.zip)
CRC-32: `6C7AABCC`  
SHA-256: `e7960afbe0c9f9e099bbc3f1716ae1f2c27d0afdfe6087b5a05eec91fb576df2`

### Changelog:
- Fixed A/DAC detection bug
- Fixed GenLock introduced in 1.1.8
- Added additional reset logic to the HDMI TX control
- CSC block buffers input signals to improve timing
- Inverse 2:2 re-written to avoid memory collisions, should improve detection
- Added cop to disable inverse 2:2 telecine for progressive modes

<br/>

## Version 1.1.8 (2024-01-21)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@05b0e1a/RetroTINK-4K/Experimental/rt4k_118.zip)
CRC-32: `2FCC1715`  
SHA-256: `3c0865755d6979234f258c33cdfe3914b5d1084c35154d4df0c9488cc493f383`

### Changelog:
- Analogue consoles, when used in DAC mode are automatically decimated
- Replaces older method which only guessed at the decimation factor
- Name of the Analogue console is now displayed in the A/DAC menu

<br/>

## Version 1.1.7 (2024-01-20)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_117.zip)
CRC-32: `1EAEAF51`  
SHA-256: `6220de053a6c72e203b9ddc79e1ab8fc6a8cc175974fdf9f4f79a96dd8da2141`

### Changelog:
- Fixed pseudo-interlace menu display bug
- Added Limited Range option to the HDMI Output Menu
- Added Dithering option to color correction menu
- Fixed Saturn cop for 455 and 910

<br/>

## Version 1.1.6 (2024-01-20)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_116.zip)
CRC-32: `7E14704E`  
SHA-256: `57b10fd1c8e6c34785db8460b6614ddf9ca12bb3e0b9d405ec50ffbc8b50c9f8`

### Changelog:
- [NEW FEATURE] Pseudo Interlaced Scanlines to the Image Processing menu
- Presents progressive sources with interlacing (i.e. 720p -> 1440i or 720p -> 720i)
- Saturn detection thresholds tuned
- Fixed vertical pre-scale control cop for CRT simulation deinterlacing mode
- Fixed SPD infoframe bug when VRR is off
- Possible cleanup of the HDR infoframe

<br/>

## Version 1.1.5 (2024-01-19)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_115.zip)
CRC-32: `8AFB382E`  
SHA-256: `3511e8a141504afea7ee843048cd6b2918bb243a5b33fce3c0cb62b165685203`

### Changelog:
- Complete re-write of the auto-decimation phase algorithm (for auto sampling)
- Fixed issues with auto-phase detection in Saturn hi-res
- Overall improved stability of the auto-phase

<br/>

## Version 1.1.4 (2024-01-17)

### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-4K/Experimental/rt4k_114.zip)
CRC-32: `E9E3769B`  
SHA-256: `5d874dd82f6942e2a1bdc71359fc6cb8075909f9cc2426a96906551354f9a3b4`

### Changelog:
- Complete re-write of the auto-sample rate detection algorithm
- Cleaned up Saturn auto-sampling mode
- Tuned auto-phase to reject data unless there is sufficent detail in the scene
- Fixed bugs in HDMI TX control

<br/>

## Version 1.1.3 (2024-01-15)

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
- Option to disable min. BFI rate cop
