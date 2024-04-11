---
title: Electrosmith Daisy Seed to make Custom Synth Modules
date_created: April 10, 2024
---

## Introduction

The Center for Concrete and Abstract Machines (<a target="\_blank" href="https://ccam.world/">CCAM</a>) has invited me to be on their Synthesis Team for the audio software development of three DIY synths that will be showcased in a workshop called <a target="\_blank" href="https://ccam.world/programs/24-5-10-future-rhythm-machines-chicago-house/">FUTURHYTM MACHINES: Chicago House Music</a>. Each synth will have their own name and sonic output:

- "Chronos/Khairos": Drum Sequencer
- "Pocket Calculated": Bass
- "Harmonia Terra": Lead Synth

Each synth circuit uses a custom PCB circuit with potentiometers and buttons for ease of control of parameters. It will also have:

- Stereo audio output/input
- 2 CV outs/ins

<img width="400px" src="./imgs/pcb.png"></img>

A major goal is for ease of interaction between these synths to create a wonderful sonic experience.

--- 

## Max/MSP gen~ and the Electrosmith Daisy Seed

The heart of this synth is the Electrosmith <a target="\_blank" href="https://electro-smith.com/products/daisy-seed">Daisy Seed</a>. The Kickstarter for this board started in 2020 and has already become a popular choice for audio programmers that want to make their programs come to life by taking a more physical and portable form. This is a perfect board for sound artists wanting to make sound installations, and for performers/musicians wanting to make custom synths for their Eurorack setups. Before this board, the <a target="\_blank" href="https://www.pjrc.com/teensy/">Teensy</a> was a popular choice.

There are several ways to write an audio program to flash into the Daisy, for example you can use Arduino or Pure Data, but I will use the <a target="_blank" href="https://docs.cycling74.com/max8/vignettes/gen_topic">Max/MSP gen~</a> environment, which uses lower-level objects allowing the ability to compile a patch into code that the Daisy can understand. The Max package for flashing the board is called <a target="\_blank" href="https://github.com/electro-smith/oopsy">Oopsy</a>.

For more options and info about how to get started check out this wiki page: <a target="\_blank" href="https://github.com/electro-smith/DaisyWiki/wiki">https://github.com/electro-smith/DaisyWiki/wiki</a>

--- 

## Chronos/Khairos

**Description**:

- This synth is a 3-voice drum machine with a bass, snare, and hi-hat.
- Patterns can modulated by randomness. It works with a "topographic" principle (perlin noise).

**Button Control**:

- Bass Drum pattern hits are manually toggled via the 8 available buttons.

**Potentiometer Control**:

- Randomness: 
- Density:

**Audio Synthesis**:

- Bass Drum (kick) sound
- Snare sound
- Hi-hat sound

### Building a Sequencer

The "Hello World" for any sequencer construction is to have a single event triggered repeatedly by a clock.

To construct a clock, we can start with a `[phasor]` object. The number following phasor is the _frequency_ parameter. `[phasor 1]` will create a ramp that goes from 0.0 to 1.0 in one second.

<img width="300px" src="./imgs/ramp1s.png"></img>

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">The live.scope~ object defaults to plotting 44.1k samples.</i></div>

<img width="500px" src="./imgs/ramp1s_plot.png"></img>

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">This plot better shows what the X and Y axes represent.</i></div>

What we want is for this ramp to trigger an event when it resets its cycle. In the analog synthesis world, the term trigger is a very short pulse that is used to activate something, in Max/MSP gen~ the term _click_ is used. A click is simply an output of 1.0 for one sample.

  <img src="./imgs/click.png"></img>

### Events and Hits
