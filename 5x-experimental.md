---
layout: default
title: RetroTINK-5X Experimental Firmware
---

<h1 align="center" style="margin-top: 0px;">RetroTINK-5X Experimental Firmware</h1>

<p style="margin:30px;"></p>

<h2 align="center" style="margin-top: 0px;">⚠️ CAUTION: Read carefully before proceeding ⚠️</h2>

<p style="margin:10px;"></p>

### Warning: Only update your device using the tools provided below. Attempts at any other method will result in non-warranty device failure.

<p style="margin:10px;"></p>

## Notice: Firmware updates erase saved profiles and reset the device to default settings.

<p style="margin:15px;"></p>

## THE FIRMWARE CONTAINED IN THIS DIRECTORY IS PRE-RELEASE. PROPER FUNCTIONALITY IS NOT GUARANTEED, AND FEATURES MAY STILL BE IN DEVELOPMENT.

<p style="margin:20px;"></p>

## Instructions️

### Windows

1. Download the [FTDI D2XX Drivers](https://ftdichip.com/wp-content/uploads/2021/08/CDM212364_Setup.zip) and install.
2. Download the [RetroTINK Firmware update tool](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK%20FW%20Tool.zip) and install by unzipping and running RT_FWUP.
3. Download the appropriate HEX file for the desired version from the list below.
4. Plug your device into your computer's USB port while holding down the 'Menu' button. The LED should be RED indicating update mode.
5. Run the RetroTINK Firmware Update tool. The installer will have left a shortcut on your desktop.
6. Hit 'Search'. You should see 'FT232R USB UART' appear in the box.
7. Hit 'Load HEX' and point to the .hex file you downloaded.
8. Hit 'Flash'. The update process should start. If the window freezes, that is okay - the update should complete after a minute or two. Just be patient.
9. Your device should reboot and be ready to use.
10. If you accidentally interrupt the process, just start over from step 4.

### Multiplatform

A talented developer (Ryan Mullen) [ported the firmware update tool to Python.](https://github.com/rmull/tinkup)

This should work on Windows, Mac (including M1) and Linux.

### Video

Big thanks to [RetroRGB](https://www.retrorgb.com/how-to-update-your-retrotinks-firmware.html) who was kind and generous enough to put this video together. **Please do not contact him for technical support.**

<iframe width="560" height="315" src="https://www.youtube.com/embed/Bva0JXLoq7E?si=Eobt-HF3LD1Lo89_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<br/>

## Version 3.93 (2024-03-08)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X SDRAM V393.zip)
CRC-32: `A81280F1`  
SHA-256: `6211a29e6c22e027655c3e55a59b5d9c18168236a251fa4249db4ef0646c5c20`

### Changelog:
- Signifcant improvements in S-video quality
- Improved H-PLL lock for VHS

<br/>

## Version 3.92 (2024-02-24)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X SDRAM V392.zip)
CRC-32: `0915609C`  
SHA-256: `c5cadbfadfa5c394f3b53ebb5d664ee503f8fe86a555332c5b21a640c49b10dd`

### Changelog:
- Hard resolution changes (i.e. 240p <-> 480i) are detected and masked to provide a smoother experience

<br/>


## Version 3.91 (2024-02-20)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X SDRAM V391.zip)
CRC-32: `40993338`  
SHA-256: `64efff77c46703e2a3804f64d39e32ef51e2c6dffd1ae05fc8b5cb71e183327c`

### Changelog:
- Threshold for declaring no signal greatly increased.
- ADC no signal color changed from Blue to Black
- Possibly beneficial for games that switch resolutions and VHS

<br/>

## Version 3.90 (2024-01-30)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X SDRAM V390.zip)
CRC-32: `85FBB9D8`  
SHA-256: `601298ff5ba81646660cbf2ae8a4c3f82d1f9fab5e3448adc1cb740bd3a33f11`

### Changelog:
- Added "MA Smoother" to the Deinterlacer menu. This applies the smoothed-Bob instead of linear-Bob in the motion adaptive deinterlacer.
- Rolled in the new RT4K Inverse 2:2 de-interlacer. Games with frame rate changes (such as FFX) may now be playable.

<br/>

## Version 3.699 (2023-09-09)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X_SDRAM_V3699.zip)
CRC-32: `9EC64D62`  
SHA-256: `5cd7cae666c649d9319c42ed43b08932dc71e77df8285a57a621b17daf8ac06f`

### Changelog:
- Lock to '50 Hz' added
- Improved IVTC 2:2
- Eliminated glitch in image on some units (?)

<br/>

## Version 3.6969 (2023-09-04)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V36969.zip)
CRC-32: `FEBED0EE`  
SHA-256: `bc53da13dbc71b9b94e20be0e896c3d9c7784344c9590032a4cd19a1659542c9`

### Changelog:
- Added 2:2 Inverse Telecine
- Touched up crops in 16:9 1080pOver
- Increased NO SIGNAL threshold to hopefully (?) stop signal drops in PAL triple buffer
- The lightgun border in 2560x1440 is not fixed. Currently do not have time to investigate

<br/>

## Version 3.69 (2023-08-30)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V369.zip)
CRC-32: `41F3A8B3`  
SHA-256: `7e23b8297377acb0cbae0b9a16293c5552704cfbe8cd2d907c976e7d97f2f411`

### Changelog:
- Deinterlace and Vertical Interp. are now separate menus
- Ported RT4K Inverse Telecine Deinterlacer
  - This should be used in conjunction with Frame Lock/Gen Lock/TBC to maintain the correct buffer order
  - Filter setting ranges from Low to Max. Low is for clean sources such as DVDs. Maximum is for noisy sources such as VHS
- Adjusted default ADC clamps to minimize green tint
- Shifted 16:9 SDP modes for 1080pFill to avoid glitch on left hand side
- Added alternate S-Video input on Green/Blue RCA jacks

<br/>

## Version 3.65 (BETA) (2023-07-02)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V365.zip)
CRC-32: `50E2DC52`  
SHA-256: `c9d32670611654ac67d0b1d49c37b6b1e755eb1d7a310777302fbbb86090fe2b`

### Changelog:
- Gen lock converges at a slower rate for less abrupt frequency changes
- Improved TBC control loop algorithm
- Fixed remote control bug for 480i direct selection

<br/>

## Version 3.64 (BETA) (2023-07-02)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V364.zip)
CRC-32: `6311200F`  
SHA-256: `b67526405c1ebfb1c0f9921a62f637c500474a22a2c145b1e0e5c2229dccdd47`

### Changelog:
- Improved algorithm for TBC frame rate filter and locking
- Ported RT4K clock synthesizer control code for GenLock edge cases
- Added support for play/pause on Disney remotes

<br/>

## Version 3.63 (BETA) (2023-06-30)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V363.zip)
CRC-32: `DAD7B657`  
SHA-256: `e84f7120d9ae0912d4f2453b13f8c7ffc7cfccc68b98aa5390ea42879bff8a8d`

### Changelog:
- Uptime counter on the status page. aka Days without a green screen.
- Fixed gain adjustment bug for GBI/1080i/720p
- Added pause (mapped to AUX4 on the new remote)
- Added TBC mode in addition to Frame Lock and Gen Lock. TBC acquires and outputs video using the stable frame rate of the source material while rejecting glitches. Avalible for all units that support Gen Lock (which is the vast majority of RT5Xs in the wild)

<br/>

## Version 3.62 (BETA) (2023-06-22)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V362.zip)
CRC-32: `F7D79C70`  
SHA-256: `7a47433c8986a898e043dfb8ad5ced1e358ca92a82769590856f3cea49c12a1c`

### Changelog:
- For anyone who has had persistent "green screen" or "garbled screen" issues

<br/>

## Version 3.61 (BETA) (2023-06-17)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V361.zip)
CRC-32: `1FDE0017`  
SHA-256: `1a5492373c966e5fddc4a208b7ff34b46094c4b8230d78fa793236d0269b39a7`

### Changelog:
- Horizontal scale/adc sample rate saving fixed.
- SDP chroma gain control fixed
- Further SDRAM controller optimizations
- Added support for next generation remote
- New remote has partial compatibility with the "Disney DVD player" codes. Basic power, menu and quick profile load (numbers) should work.

<br/>

## Version 3.5 (BETA) (2023-06-13)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20V35.zip)
CRC-32: `D0FFC675`  
SHA-256: `7428fd6e1bde9d84f287172a8c7194f342a33f7ec62511509a75a9e2a364cfe9`

### Changelog:
- Fixed horizontal scaler bug
- Improved SDRAM clock stability
- Improved mode detection speed

<br/>

## Version 3.2 (BETA) (2023-06-12)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V32.hex)
CRC-32: `929C828E`  
SHA-256: `e34e15d4abcd8898847b063225d2de130ffc218c27ffe9ce044a8ff75ca61230`

### Changelog:
- Added analog level gain controls for CP modes in the [Video ADC-2] menu
- Gain control focuses on the channel that is being adjusted (Y, Pb or Pr) and dynamically highlights clipped pixels (min = blue, max = purple)
- High light clipping is also shown for SDP brightness/contrast adjustments. Note: clipping for SDP adjustment occurs at 75% intensity for compatibility with SMPTE bars
- LCD Frame blend simulation in the [Interp./Deint Menu].
- Expanded adjustment range for ADC sample rate. This allows you to use the Gen 320 setting to create a 1:1 PAR mode for SNES sources
- Ported over RT4K SDRAM controller to hopefully eliminate glitch out after long periods of no video signal (????)
- MOAR speed on the SDRAM clock

<br/>

## Version 2.99969 (2022-12-13)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V299969.zip)
CRC-32: `48F98CCF`  
SHA-256: `92482034fe93a9a593f3222ba3985470ad0eddec6c7ac0daba1908e5c2b2def1`

### Changelog:
- 720p DS screen tearing fixed
- BMD compatibility

<br/>

## Version 2.999 (2022-12-11)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V2999.zip)
CRC-32: `BE299D89`  
SHA-256: `ae9141570aca05614ce691b7ce658e0414951329a59b05e5b311e981643530e9`

### Changelog:
- All the residual screen tearing... gone... ?

<br/>

## Version 2.99 (2022-12-04)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20V299.zip)
CRC-32: `BD5709B1`  
SHA-256: `fbc81e2b846cf4ecccc7970e731ae47d0f52557db05d16fe7d6db3c8bac09132`

### Changelog:
- Various tearing issues should have been fixed
- Improved latency in 576p -> 1920 x 1440p
- Fixed CVBS auto-gain bug (?)
- Speed of the save/load profile screens improved so you can move on to play the f---ing game

<br/>

## Version 2.98 - Early Thanksgiving and Black Friday Preview Edition (2022-11-21)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V298.zip)
CRC-32: `BB6AAADD`  
SHA-256: `f2100aa180b01d2dbcb22ece3c504edfa74f33ae0d9016b4047f0369c3ce7270`

### Changelog:
- Ported RT4K buffer mode, making all resolutions 'min-lag'.
- Current buffer lag (assuming Frame Lock or converged Gen Lock) can be seen in the [Status] page.
- Ported RT4K Gen Lock, improving overall stability.
- 240p output mode revived (for 240p, 480i, 480p and 720p inputs).
- 480i output mode added (for 240p, 480i, 480p and 720p inputs).
- Downscaler behavior can be controlled in the [Interp./Deint.] menu. Ds Pass-Thru = No, forces all sources to the specified output (i.e. 480i is converted to 240p). DS Pass-Thru = Yes has the output resolution follow the input resolution.
- Please be aware, that downscaling options are considered experimental and unsupported. We cannot provide support or guarantee proper operation with 3rd party HDMI -> analog dongles. You will need a converter that is capable of recognizing and generating the correct sync signals for 480i video.
- 4K24 and 1080p Min-Lag modes removed.
- Profile naming added.

<br/>

## Version 2.72 (2022-05-28)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V272.zip)
CRC-32: `42CE3F99`  
SHA-256: `fb6f9571ee94bce412b27daed263bfe1048aa453c6069c23c12c8662d882eab5`

### Changelog:
- Fixed PAL PS1 Optimal 320 timing
- Optimal timings for hi-resolutions (ADC sample rate > 2048) can have the H. Interpolation size adjusted downward for further tweaks
- Recalibrated RGB/YPbPr inputs to 714 mV peak-to-peak standard
- Increased active picture area for 480p sources by 16 lines

<br/>

## Version 2.7 (2022-04-19)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V27.zip)
CRC-32: `7D9B71F6`  
SHA-256: `ca5af2216de21fa595e9953ff45c2558e90215e197e20a22ef8442996f9d1ed9`

### Changelog:
- Shaved 500 microseconds in Min-Lag mode
- Note: Glitching colors in 1440p

<br/>

## Version 2.69 (2022-04-17)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V269.hex)
CRC-32: `E33FE4BD`  
SHA-256: `96c11d5a1691d3edd222c8b30bf73b69fb084b088e169906242cc045ce39c00d`

### Changelog:
- Press and hold remote control button to keep changing <> values
- Added a 1080p (Min-Lag) mode that should achieve line-doubler latency (~1 ms) while keeping standard timings. available for 240p, 480i and 480p sources.
- Added support for 2048 x 1536p (iPad screen) for 240p, 480i, 480p and 360p sources

<p style="margin:20px;"></p>

Advanced resolutions are enabled by going into [OSD] -> Advanced Res option first to clarify that these modes are experimental and unsupported

<p style="margin:41px;"></p>

## Version 2.60 (2022-02-07)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V260.hex)
CRC-32: `B78A44A3`  
SHA-256: `b52936f356d96eed1824e653a9e80a464b1f9821a4abf1486344f0ffae94c4cf`

### Changelog:
No need to install unless the below items are of interest to you:
- Frame lock now works for 4K
- 288P/576I frame locks to 25 Hz
- 240P/480I/480P frame locks to 30 Hz
- 480P to 4K crop fixed

<p style="margin:20px;"></p>

The success rate here will be spotty since this pushes the clock to 260+ MHz. Triple buffer mode remains at 24 Hz for this mode as a safety fall back.

<p style="margin:41px;"></p>

## Version 2.59 (2022-02-06)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V259.hex)
CRC-32: `470C98B5`  
SHA-256: `2c966de1fc54b2f699591424a23a17f219df1fd9931ae8e6f7797e6460190cd9`

### Changelog:
Usual disclaimers for experimental builds apply.

- 240P/480I, 480P can be scaled to 4K24
- 288P/576I can be scaled to 4K25
- Optimal sampling available for RGB/YPbPr sources
- Leave in triple buffer
- May be best to get stable signal from console before entering 4K

<br/>

## Version 2.58 (2022-02-05)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V258.hex)
CRC-32: `F84DA0E9`  
SHA-256: `db4f7a13a38d0735645570b592cd5b28a005fd6183762d81b560f87fda5ccfdb`

### Changelog:
Same disclaimers as 2.57 apply, not retyping it. No need to apply this firmware unless the items below matter to you:
- 9x Scaling for GBI to 2560 x 1440
- 2560 x 1440 output timings changed slightly to match mClassic and PC
- CSC (Limited Full) bug on startup might (?) be fixed (I have no way of replicating)
- 720p now outputs 59.94 Hz in triple-buffer

<br/>

## Version 2.57 (2022-02-01)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V257.hex)
CRC-32: `9966D808`  
SHA-256: `2916ff999c7a1488647e3a1a64096c621d708c8ffe9b7820bf212428e7ef59e4`

### Changelog:
- 2560x1440 and 1920x1440 are now separate menu items.
- General improvements in FPGA timing closure.
- 2560x1440 now supports 240p/480i, 288p/576i, 480p, 720p, all cropped and centered.
- Optimal timings for 288p/576i now enabled for both 1440p modes.
- Optimal timing for 480P to 2560x1440 has two modes:
  - DTV 858 (3:2) is a square pixel mode ideal for Dreamcast and other games where developers did not account for the 9/10 PAR.
  - DTV 858 (x4) uses a 4x horizontal and 3x vertical scaling. This is slightly wider than 16:9. You can increase the vertical scale by 10% to compensate.

<br/>

## Version 2.55 (2022-01-31)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V255.hex)
CRC-32: `46E34B67`  
SHA-256: `eeac83d64a5975bc5caf6f96583a4a25ea685980da67224b5ed9912712a58cc6`

### Changelog:
- Special 1440p mode for 240p/480i (RGB/YPbPr) and 720p sources
- Note: Cropping/centering is messed up

<br/>

## Version 2.53 (2022-01-30)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V253.hex)
CRC-32: `D93EEC6D`  
SHA-256: `5be61b68e74845554fd6d6c7acb4c3087eee7b77a0babfba854d640b21e19408`

### Changelog:
- Pre-scaler function for down-scaling 720p and 480p sources by 1/2 or 1/3 before re-scaling to output for adding scanline effects to modern sources.
- Fixed screen-tearing when increasing vertical shift
- Lock to 60 Hz function now works for 1200p sources
- Light-gun option in OSD menu, border follows crop
- Fixed a variety of cropping and edge garbage issues
- 720p source can now be scaled to 1080p (Fill) and 1440p
- Composite and S-video source now have optimal sampling
- Hi-resolution optimal sampling modes (512 and 858)
- Option to enable optimal sampling for interfaced sources
- Pre-emph filter now goes down to -5 for extra blur
- Option to select which user profile to load on power up in OSD menu
- Default profile can be loaded by pressing 'Back' on the remote rapidly 6 times
- NOTE: Firmware flashes erase profiles due to significant data structure changes.

<br/>

## Version 2.40 (2022-01-11)
### [Download](https://cdn.jsdelivr.net/gh/retrotink-llc/firmware@main/RetroTINK-5X%20Pro/Experimental/RT5X%20SDRAM%20V240.hex)
CRC-32: `46B585AE`  
SHA-256: `baf223c6c4345553efe76d6223e2e1bf877b735de7b3e59bfb2b5c72e8aca20e`

### Changelog:
- 480p/720p pre-scale function
