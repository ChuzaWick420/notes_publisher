---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Transmission Medium
Data is encoded in form of energy and transmitted over a medium called `transmission medium`. This can be air, wire etc.

## Copper Wire
These show very low resistance to electric current.  
**Example:** Twisted wire pair.

## Coaxial Cable
Single wire surrounded by an insulator and a metallic mesh to shield against interference.

## Types of Transmission Medium
**Guided:** Where the path is physically defined, such as a wire.  
**Unguided:** Where the path is air.

## Optical Fiber
It uses light for carrying data.

## Radio Waves
These are used for TV and public radio etc.

## Satellites
### Geosync Satellites
These are placed about 35785 KMs above the surface of the earth and appear stationary as the earth revolves.

### Low Orbit Satellites
They are about 200 or 400 miles above the earth and do not appear stationary as the earth revolves.

## Microwaves
This uses higher frequency as compared to radio waves and can be uni-directed.

## Infrared
These are used for TVs etc.  
They have very limited range.

# Local Async Communication
The sender and receiver do not coordinate with each other and receiver should be able to interpret signals anytime it receives them.

The negative voltage represents `1` while `0` is represented by positive voltage.

The standards of communication define the timings and voltage specifications regarding the signals.

The `RS-232-C` standard is used for modems and keyboards  
The `RS-232` standard is used as serial for async communication.

## RS-232-C
- Supports wire length of 50 feet.
- -15V for `1` and +15 for `0`.
- One character is `7` or `8` bits.
- No delay between character bits.
- When idle, it puts `1` on the bus.
- Each character starts with `start bit` `0` and ends with `stop bit` `1`.

## Baud Rate
It is defined to be number of changes in the signal per second.

## Frame Errors
These occur when the end bits do not occur at the expected times.

# Full-Duplex Async Communication
It uses 2 wires in which 1 carries the data signal and other one carries the return path called `ground`.  
The 2 directional communication at same time is called `full-duplex` communicaion.

# Long Distance Communication
## Modulation
The original signal is slightly modified by the transmitter by using a carrier. This process is called `modulation`.

### Types of Modulation
1. Amplitude Modulation
2. Frequency Modulation
3. Phase Modulation

## Modem
A `modem` is a device which combines both the `modulator` and `demodulator` together.

## Multiplexing
It is the process of passing multiple signals over the same wire by using multiple frequencies.

### Types of Multiplexing
1. Frequency Division
2. Wave Division
3. Time Division

#### Frequency Division
Different frequencies are passed onto the same medium

#### Wave Division
Same concept but applied to optical fibers.

#### Time Division
In this type, the sources take turns to send their data.  
Meaning they do not send data all at once, rather, they wait for their turns.
