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
