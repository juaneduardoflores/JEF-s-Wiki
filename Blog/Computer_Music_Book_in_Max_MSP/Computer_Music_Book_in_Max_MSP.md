---
title: Computer Music Book in Max MSP gen~
date_created: March 28, 2023
---

<script type="text/javascript" src="js/rnbo.js"></script>
<script type="text/javascript" src="js/app.js"></script>

## Introduction

This post is about exploring some fundamental concepts in Digital Signal Processing (DSP) and Digital Sound Synthesis by using a program called Max, a visual programming language.

### Computer Music Book

<img src="./imgs/book.jpg" width="50%" />

One of the authors of *Computer Music*, Charles Dodge, was active in computer music composition when it became a new field. In the 1960s, he was at Columbia and Princeton working on an IBM mainframe computer for his early work, but had to go to Bell Labs to use a digital-to-analog conversion system in order to hear it.[^1]

<img src="./imgs/ibm_computer.jpg" alt="IBM 360/91 console and 2250 display" width="80%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">IBM 360/91 console and 2250 display</i></div>

In 1970, he worked with three physicists to compose *Earth's Magnetic Field*, where he mapped sounds to magnetic field data. He also worked on synthesizing the human voice with *Speech Songs (1974)*. Another notable work is *Any Resemblance is Purely Coincidental (1980)* which combined live piano performance with a digital manipulation of a recording.

<img src="./imgs/dodge.png" alt="IBM 360/91 console and 2250 display" width="80%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">Dodge at the Columbia University Computer Center in 1970 while he was working on Earth's Magnetic Field.</i></div>

It is important to keep in mind that *Computer Music* was first published in 1985. Dodge demonstrates some code examples using the programming languages *Csound* and *Cmusic*. Despite the incredible difference between the computing power when this was written and now, it still serves as a good introduction to digital signal processing. The ideas are the same, the only difference is that it is now faster and easier to get results with computers that are cheaper, accessible, and more powerful. I will be covering:

- Chapter 4: Synthesis Fundamentals

### Max/MSP

Coincidentally also in 1985, *Max* started to get developed by Miller Puckette at IRCAM (Institut de Recherche et Coordination Acoustique/musique). It wasn't until 1989 when it started to use a dedicated DSP board. In 1997, Max saw its first release by the company [Cycling '74](https://cycling74.com/) to include Max/MSP, MSP seeming to stand for "Max Signal Processing" or Miller Smith Puckette's initials. It made Max capable of manipulating real-time digital audio signals without a dedicated DSP board, which made it possible to synthesize sound using a general purpose computer.

The name Max, by the way, is named after [Max Mathews](https://en.wikipedia.org/wiki/Max_Mathews), another pioneer in computer music.

### gen~

`gen~` is an extension of the *Max* patching environment that is more efficient and [lower level](https://en.wikipedia.org/wiki/Low-level_programming_language). It is great because it runs at the signal rate (audio rate), instead of using signal vectors (chunks of samples at a time). This is ideal for designing audio effects because we can work from a sample by sample basis. I will be using this environment to go over concepts that are covered in *Computer Music*.

I won't go over too much about how `gen~` works here, instead there is this [online tutorial](https://cycling74.com/tutorials/gen~-for-beginners-part-1-a-place-to-start) written by Gregory Taylor, author of [Generating Sound & Organizing Time](https://cycling74.com/books/go).

## Synthesis Fundamentals

### Unit Generator

The chapter starts by introducing the concept of a Unit Generator, or UGen for short, which is essentially an algorithm for audio. The Unit Generator theory was first developed by Max Mathews and his colleagues at Bell Labs, originally for the *Music N* programming languages. He describes them in his 1960 article in the Bell Telephone System Technical Journal: 

> "The instruments are formed by combining a set of basic building blocks called *unit generators*, appropriate combinations of which can produce sounds of almost any desired complexity or simplicity." [^2]

### parameters

A UGen might have [parameters](https://en.wikipedia.org/wiki/Parameter_(computer_programming)), that make it possible to specify the values of certain variables that change the produced audio. Parameters are inputs, that can either be **entered in** by a user manually, or **received** by another UGen. 

For example, one of the most obvious UGens to start with is an oscillator, one that produces a simple sine tone. Possible parameters for this are:

* Frequency (In Hz)
* Phase
* Amplitude

<img src="./imgs/wf.png" alt="Flowchart symbol of a waveform with parameters" width="60%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">Flowchart symbol of a waveform with parameters</i></div>

This is similar to analog synthesis, where an oscillator module with a sine wave generator will usually have a knob for frequency and amplitude (or gain).

<img src="./imgs/vintage_osc.jpg" alt="200A Audio Oscillator Production model for 1939" width="60%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">200A Audio Oscillator Production model for 1939</i></div>


Another programming language for sound synthesis that is still used today, *SuperCollider*, carries on the legacy of UGens. The line of code to produce a sine tone is this:

```C++
// Generates a sine tone.
{ SinOsc.ar(freq: 440.0, phase: 0.0, mul: 1.0) }.play;
```

This is the breakdown:

* `SinOsc` is the name of the [class](https://en.wikipedia.org/wiki/Class_(computer_programming)).
* `.ar` specifies that it will output at the audio rate.
* `(freq: 440.0, phase: 0.0, mul: 1.0)` are the parameters. It will have a frequency of 440 Hz, phase of 0, and amplitude of 1.0.
* `{}.play;` is to start the process. The curly brackets are necessary because by surrounding the SinOsc with them we are creating a [function](https://en.wikipedia.org/wiki/Function_(computer_programming)), which is needed by the `.play` [method](https://en.wikipedia.org/wiki/Method_(computer_programming)). [^3]

I just threw around many computer science terms, don't worry if those don't make sense at the moment.

In Max MSP, the term UGen is not used. Instead, they are called objects, but underneath the surface of objects is essentially the same as UGens, they have pre-defined instructions for the computer to generate or process audio. The MSP objects have a tilde (`~`). The tilde representing a signal, means that it is calculating at the audio rate, just like in SuperCollider where `.ar` is used. So if the audio rate is set to 44,100, that means that it is calculating 44,100 values per second.

<img src="./imgs/sine.png" alt="IBM 360/91 console and 2250 display" width="60%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">A simple sine tone</i></div>

<div id="rnbo-root" style="">
<button class="ezdac-button" id="01_ezdac-button"></button>
<div class="rnbo-parameter-sliders" id="rnbo-parameter-sliders_device_1">
</div>
</div>

Note that for this purpose, phase does not effect the sound.


### Signal Flowcharts

It is common to use a visual representation of signal flow to get an idea of how a digital audio instrument/effect is made.

<img src="./imgs/signalflow.png" alt="example of a signal flowchart" width="60%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">Example of a signal flowchart</i></div>

This figure is used to show what they **could** look like, but everyone has their own preferences when drawing them. This one from the book can be daunting as a first example. One might notice that it's somewhat similar to a Max patch. The MULTIPLIER (`*`) is the same as the `[*~]` object in Max. This can be used to control the amplitude of an audio signal. This is because by multiplying the signal with a value higher than 1 we are performing *amplification*, and if we are multiplying by a value between 0 and 1 we are performing *attenuation*. In this flowchart however, the multiplier is used to modulate one UGen with another, often meaning it is controlling the envelope of a sound. The book example is using a DIVIDER (`a/b`), `[/~]` in Max, to control the overall instrument amplitude, referring its function as attenuation with the variable name ATTEN. The ADDER (`+`) is how to "sum" or "mix" two signals together.

One more thing to note is that each UGen and mathematical operation has one or more inputs, ranging from variables, hardcoded values, or a signal (stream of numbers coming at the audio rate).  Since Max is already a visual programming environment, it is already like a signal flowchart, but it is still good practice to draw these when thinking and sketching out ideas when not in front of the computer, or when branching out to other topics like analog electronics, modular synthesis, etc.

Here is a more minimal patch, a simple amplitude modulation in Max. Also note how the patch cables that are striped with green and black are the ones that are sending audio rate signals.

<img src="./imgs/simple_ampmod.png" alt="Simple amplitude modulation in Max" width="60%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">Simple amplitude modulation in Max</i></div>

<div id="rnbo-root" style="">
<button class="ezdac-button" id="02_ezdac-button"></button>
<div class="rnbo-parameter-sliders" id="rnbo-parameter-sliders_device_2">
</div>

</div>

### Wave Tables

One thing that is the same for all these programs when generating a sine tone, regardless of old or new, is that they are using a `wave table`. This is because this is the most efficient way of doing it. Instead of creating a program that would calculate each following value each time, it is much easier on the CPU to look up pre-stored values of a single wave cycle that are in the computer's memory. A wave table is like an audio recording, or a block of samples, where the program "plays" or goes through each sample and retrieves it, except that in *Wavetable Synthesis* it automatically restarts from the beginning when it reaches the end of the **cycle**. Notice how the MSP object to produce a sine tone is called `[cycle~]`. 

From the Max Documentation:

> "The cycle~ object is an interpolating oscillator that reads repeatedly through one cycle of a waveform, using a wavetable of 512 samples. Its default waveform is one cycle of a cosine wave."

Also in the documentation for the cycle~ object, are examples of how to change the default wavetable. Wavetable data is stored in a [buffer](https://en.wikipedia.org/wiki/Data_buffer), and in Max there exists a `[buffer~]` object where we can store anything we want, including a single waveform to use for the cycle~ object.

To do this, we create a buffer object and specify a name to reference it, then specify the number of samples to be 512. 

There are several ways to specify the sample size:

1) Using an `[attrui]` object to select "Size in Samples" from the dropdown menu.
2) Sending a "sizeinsamps 512" message using a message object.
3) Hardcoding it when creating the buffer~ object. For example: `[buffer~ mybuffer @samps 512]`.

You can view the content in a buffer by using a `[waveform~]` object and specifying the name of the buffer you want to view.

<img src="./imgs/wavetable.png" alt="Filling a buffer with a cosine wave" width="60%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">Filling a buffer with a cosine wave</i></div>

The example of a wavetable from the book uses a sine wave (starts at 0 instead of 1), but the sound is still the same. Note how in the following figure it also has a table for each individual sample value. For the sake of matching the book, we can use a sine wave in Max too.

<img src="./imgs/wavetable_figure.png" alt="Wavetable from the book" width="60%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">Wavetable from the book</i></div>

<img src="./imgs/wavetable_sin.png" alt="Wavetable with sine wave" width="60%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">Wavetable with sine wave</i></div>

<img src="./imgs/wavetable_output.png" alt="Plotting the cycle~ signal" width="60%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">Plotting the cycle~ signal</i></div>

When changing the frequency of the cycle~ object, the computer "plays" through the sample at that frequency.

If we wanted to make a custom waveform, an easy way to do that is to draw directly on the waveform~ object by setting it to "draw mode". You can change the mode by sending it a message `(mode draw)`, allowing you to draw the buffer content by clicking and holding the mouse on the object.

<img src="./imgs/custom_waveform.png" alt="Custom waveform" width="60%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">Custom waveform</i></div>

You can load this onto the cycle~ object like we did earlier, but if you wanted the sound to update as soon as the buffer is updated, it is better to use the `[wave~]` object, which is a variable size wavetable. To play the sound using wave~, the process is a bit different. Instead of specifying the frequency within the object or through an inlet, we have to send it a buffer position (value between 0 - 1). To do this we use a `[phasor~]`. A phasor is a ramp that goes from 0 and 1 periodically. 

<img src="./imgs/wave.png" alt="Custom waveform using wave~" width="60%" />

<div class="caption" style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">Custom waveform using wave~</i></div>

In the Max/MSP documentation called "Basics Tutorial 4", it adds this insightful historical note:

> "In the long ago days of MusicN synthesis, the phasor was the only unit generator that could produce a continuous tone. A phasor had to be connected to a wavetable to generate other waveforms."

[^1]: An interview with Charles Dodge (1993). <a href="https://www.jstor.org/stable/3681298">https://www.jstor.org/stable/3681298</a>
[^2]: Max Mathews, An Acoustical Compiler for Musical and Psychological Stimuli, Bell Telephone System Technical Journal, 1961. <a href="https://ia801601.us.archive.org/32/items/bstj40-3-677">https://archive.org/details/bstj40-3-677</a>
[^3]: <a href="https://doc.sccode.org/Tutorials/Getting-Started/05-Functions-and-Sound.html">https://doc.sccode.org/Tutorials/Getting-Started/05-Functions-and-Sound.html</a>

