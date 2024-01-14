---
layout: default
---

<h1 align="center" style="margin-top: 0px;">⚠️ CURRENTLY UNDER CONSTRUCTION ⚠️</h1>

<br/>

<h1 align="center" style="margin-top: 0px;">RetroTINK-5X experimental firmware</h1>

<p style="margin:20px;"></p>

<h2 align="center" style="margin-top: 0px;">⚠️ CAUTION: Read carefully before proceeding ⚠️</h2>

### Warning: Only update your device using the tools provided below. Attempts at any other method will result in non-warranty device failure.

## Notice: Firmware updates erase saved profiles and reset the device to default settings.

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

## Version 3.699 (2023-09-09)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- Lock to '50 Hz' added
- Improved IVTC 2:2
- Eliminated glitch in image on some units (?)

<br/>

## Version 3.6969 (2023-09-04)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- Added 2:2 Inverse Telecine
- Touched up crops in 16:9 1080pOver
- Increased NO SIGNAL threshold to hopefully (?) stop signal drops in PAL triple buffer
- The lightgun border in 2560x1440 is not fixed. Currently do not have time to investigate

<br/>

## Version 3.69 (2023-08-30)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

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
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- Gen lock converges at a slower rate for less abrupt frequency changes
- Improved TBC control loop algorithm
- Fixed remote control bug for 480i direct selection

<br/>

## Version 3.64 (BETA) (2023-07-02)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- Improved algorithm for TBC frame rate filter and locking
- Ported RT4K clock synthesizer control code for GenLock edge cases
- Added support for play/pause on Disney remotes

<br/>

## Version 3.63 (BETA) (2023-06-30)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- Uptime counter on the status page. aka Days without a green screen.
- Fixed gain adjustment bug for GBI/1080i/720p
- Added pause (mapped to AUX4 on the new remote)
- Added TBC mode in addition to Frame Lock and Gen Lock. TBC acquires and outputs video using the stable frame rate of the source material while rejecting glitches. Avalible for all units that support Gen Lock (which is the vast majority of RT5Xs in the wild)

<br/>

## Version 3.62 (BETA) (2023-06-22)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- For anyone who has had persistent "green screen" or "garbled screen" issues

<br/>

## Version 3.61 (BETA) (2023-06-17)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- Horizontal scale/adc sample rate saving fixed.
- SDP chroma gain control fixed
- Further SDRAM controller optimizations
- Added support for next generation remote
- New remote has partial compatibility with the "Disney DVD player" codes. Basic power, menu and quick profile load (numbers) should work.

<br/>

## Version 3.5 (BETA) (2023-06-13)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- Fixed horizontal scaler bug
- Improved SDRAM clock stability
- Improved mode detection speed

<br/>

## Version 3.2 (BETA) (2023-06-12)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

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
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- 720p DS screen tearing fixed
- BMD compatibility

<br/>

## Version 2.999 (2022-12-11)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- All the residual screen tearing... gone... ?

<br/>

## Version 2.99 (2022-12-04)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- Various tearing issues should have been fixed
- Improved latency in 576p -> 1920 x 1440p
- Fixed CVBS auto-gain bug (?)
- Speed of the save/load profile screens improved so you can move on to play the f---ing game

<br/>

## Version 2.98 - Early Thanksgiving and Black Friday Preview Edition (2022-11-21)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

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
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- Fixed PAL PS1 Optimal 320 timing
- Optimal timings for hi-resolutions (ADC sample rate > 2048) can have the H. Interpolation size adjusted downward for further tweaks
- Recalibrated RGB/YPbPr inputs to 714 mV peak-to-peak standard
- Increased active picture area for 480p sources by 16 lines

<br/>

## Version 2.7 (2022-04-19)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- Shaved 500 microseconds in Min-Lag mode
- Note: Glitching colors in 1440p

<br/>

## Version 2.69 (2022-04-17)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- Press and hold remote control button to keep changing <> values
- Added a 1080p (Min-Lag) mode that should achieve line-doubler latency (~1 ms) while keeping standard timings. available for 240p, 480i and 480p sources.
- Added support for 2048 x 1536p (iPad screen) for 240p, 480i, 480p and 360p sources

<p style="margin:20px;"></p>

Advanced resolutions are enabled by going into [OSD] -> Advanced Res option first to clarify that these modes are experimental and unsupported

<br/>

## Version 2.60 (2022-02-07)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
No need to install unless the below items are of interest to you:
- Frame lock now works for 4K
- 288P/576I frame locks to 25 Hz
- 240P/480I/480P frame locks to 30 Hz
- 480P to 4K crop fixed

<p style="margin:20px;"></p>

The success rate here will be spotty since this pushes the clock to 260+ MHz. Triple buffer mode remains at 24 Hz for this mode as a safety fall back.

<br/>

## Version 2.59 (2022-02-06)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
Usual disclaimers for experimental builds apply.

- 240P/480I, 480P can be scaled to 4K24
- 288P/576I can be scaled to 4K25
- Optimal sampling available for RGB/YPbPr sources
- Leave in triple buffer
- May be best to get stable signal from console before entering 4K

<br/>

## Version 2.58 (2022-02-05)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
Same disclaimers as 2.57 apply, not retyping it. No need to apply this firmware unless the items below matter to you:
- 9x Scaling for GBI to 2560 x 1440
- 2560 x 1440 output timings changed slightly to match mClassic and PC
- CSC (Limited Full) bug on startup might (?) be fixed (I have no way of replicating)
- 720p now outputs 59.94 Hz in triple-buffer

<br/>

## Version 2.57 (2022-02-01)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

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
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- Special 1440p mode for 240p/480i (RGB/YPbPr) and 720p sources
- Note: Cropping/centering is messed up

<br/>

## Version 2.53 (2022-01-30)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

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

## Version 2.40 (2022-01-11)
### Download link to be added
CRC-32: `PLACEHOLDER`  
SHA-256: `PLACEHOLDER`

### Changelog:
- 480p/720p pre-scale function