---
title: Computer Music Book in Max MSP gen~
date_created: March 28, 2023
---

## Introduction

This post is about exploring some fundamental concepts in Digital Signal Processing (DSP) and Digital Sound Synthesis by using a program called Max, a visual programming language.

### Computer Music Book

<img src="./imgs/book.jpg" width="50%" />

One of the authors of *Computer Music*, Charles Dodge, was active in computer music composition when it became a new field. In the 1960s, he was at Columbia working on an IBM mainframe computer for his early work, but had to go to Bell Labs to use a digital-to-analog conversion system in order to hear it[^1].

<img src="./imgs/ibm_computer.jpg" alt="IBM 360/91 console and 2250 display" width="80%" />

<div style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">IBM 360/91 console and 2250 display</i></div>

In 1970, he worked with three physicists to compose *Earth's Magnetic Field*, where he mapped sounds to magnetic field data. He also worked on synthesizing the human voice with *Speech Songs (1974)*. Another notable work is *Any Resemblance is Purely Coincidental (1980)* which combined live piano performance with a digital manipulation of a recording.

<img src="./imgs/dodge.png" alt="IBM 360/91 console and 2250 display" width="80%" />

<div style="text-align: center; padding-bottom: 1em;"><i style="color: #ccd3d5;">Dodge at the Columbia University Computer Center in 1970 while he was working on Earth's Magnetic Field.</i></div>

It is important to keep in mind that *Computer Music* was first published in 1985. Dodge demonstrates some code examples using the programming languages *Csound* and *Cmusic*. Despite the incredible difference between the computing power when this was written and now, it still serves as a good introduction to digital signal processing. I will be covering:

- Chapter 4: Synthesis Fundamentals

### Max/MSP

Coincidentally also in 1985, *Max* started to get developed by Miller Puckette. It wasn't until 1989 when it started to use a dedicated DSP board. In 1997, Max saw its first release by the company [Cycling '74](https://cycling74.com/) to include Max/MSP, MSP seeming to stand for "Max Signal Processing" or Miller Smith Puckette's initials. It made Max capable of manipulating real-time digital audio signals without a dedicated DSP board, which made it possible to synthesize sound using a general purpose computer.

The name Max, by the way, is named after [Max Mathews](https://en.wikipedia.org/wiki/Max_Mathews), another pioneer in computer music.

### gen~

`gen~` is an extension of the *Max* patching environment that is more efficient and lower level. It is great because it runs at the signal rate (audio rate), instead of using signal vectors (chunks of samples at a time). This is ideal for designing audio effects because we can work from a sample by sample basis. I will be using this environment to go over concepts that are covered in *Computer Music*.

I won't go over too much about how `gen~` works here, instead there is this [online tutorial](https://cycling74.com/tutorials/gen~-for-beginners-part-1-a-place-to-start) written by Gregory Taylor, author of [Generating Sound & Organizing Time](https://cycling74.com/books/go).

## Synthesis Fundamentals

The chapters starts by introducing the concept of Unit Generators, which is essentially an algorithm for audio.

[^1]: An interview with Charles Dodge (1993). <a href="https://www.jstor.org/stable/3681298">https://www.jstor.org/stable/3681298</a> 
