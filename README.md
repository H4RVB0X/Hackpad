# Macropad
Macropad is a 6 key pad with a rotary encoder, an OLED display and 12 LED's. It uses KMK firmware.

It is inspired by the Hackpad YSWS (which has now ended so it is a now a hackpad blueprint)

## Features
- 3D printed custom case that is angled towards the user for easier use.
- 6 MX switches.
- 12 RGB LED's.
- A rotary encoder.
- A 128x32 OLED display.

## CAD Model for Case
It is screwed in using 3 M3 bolts and heatset inserts. It has a 10 degree tilt.

It is all one complete part with an open top to showcase the pcb and components.

<img src=assets/cad.png alt="Schematic" width="500"/>

Made in Solidworks.

## PCB
My PCB was designed in KiCad.

It was a challenge trying to route it all as I've never created a PCB before so ignore the messy wiring.

<img src=assets/schematic.png alt="Schematic" width="300"/>

<img src=assets/pcb.png alt="Schematic" width="300"/>

## Firmware Overview
It uses KMK firmware and may in the future be upgraded to QMK if I learn how to use it.

- The rotary encoder changes volume and is pressed to change layer.
- The 6 keys currently are assigned differently for each layer - Base (Gaming), Function, Media
- The OLED just tells you what layer your on and will in future have pictures or custom icons on there - maybe even temps if I can get that to work

## BOM

- 6x Cherry MX Switches
- 6x DSA Keycaps
- 3x M3x5x4 Heatset inserts
- 3x M3x16mm SHCS Bolts
- 6x 1N4148 DO-35 Diodes
- 12x WS2812B LEDs
- 1x 0.91" 128x32 OLED Display
- 1x EC11 Rotary Encoder
- 1x XIAO RP2040
- 1x Case (3D PrinteD)
