---
title: Computer Music Book in Max MSP gen~
date_created: March 28, 2023
---


## Introduction

<img src="./imgs/book.jpg" width="50%" />

### Computer Music Book

It is important to keep in mind that *Computer Music* was first published in 1985. Despite the incredible difference between computing power when this was written and now, it still serves as a good introduction to digital signal processing. I will be covering:

- Chapter 4: Synthesis Fundamentals

### Max/MSP gen~

`gen~` is an extension of the *Max* patching environment that is more efficient and lower level. It is great because it runs at the signal rate (audio rate), instead of using signal vectors (chunks of samples at a time). This is ideal for designing audio effects because we can work from a sample by sample basis. I will be using this environment to go over concepts that are covered in *Computer Music*....

