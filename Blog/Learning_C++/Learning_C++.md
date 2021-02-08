---
title: Learning_C++
creating_date: February 8th, 2021
---

## Learning C++

### Resources
Beginner:
  * Dan Buzzo's youtube series [Programming for
  Artists](https://www.youtube.com/watch?v=HGbkTHCO8P8&list=PL6QF0yo3Zj7DlRpQlfBULd3ngzi-qbLCY).
  * Open Frameworks Book. [C++ Language Basics](https://openframeworks.cc/ofBook/chapters/cplusplus_basics.html)
Intermediate:
  * [OneLoneCoder](https://www.youtube.com/c/javidx9/videos)

### First Things to Know
  * C++ is a compiled language, which means you need a compiler in order to turn it into machine code and run it.
  * C++ is based on C with some added features (represented by `++`). Because of this, it is important to have a thorough knowledge of C.

### Examples to Get Started 
#### Hello Moon 
A simple program that prints a phrase is the common way to get familiar with a programming language's
syntax and setup.

##### Setup  
  * **Text Editor**  
You can use any plain text editor.

  * **Compiler**  
The most frequently used and free compiler is [GNU C/C++ compiler](https://gcc.gnu.org/install/). If
you are using MacOS, then you can use the `clang` C++ compiler available in the "Command Line Tools
for XCode". You can download it at the [Apple Developer Site](https://developer.apple.com/downloads/).

##### The Program:
```cpp
#include <iostream>

using namespace std;

int main() {
  cout << "hello moon\n";
}
```

`#include <iostream>`  
This is including a library called 'iostream'. `<iostream>` is what we use to get input and output.

`using namespace std;`  
In this line we are using a namespace called `std` (standard). 

`cout << "hello moon\n";`  
This line prints "hello moon" follow by a new line `\n` in the console. The `c` in `cout` stands for "character". `out` stands for "output". `cout` is a stream which outputs to the stream specified. It is by default the standard output stream. By default, most systems have their standard output set to the console where text messages are shown. `<<` is an insertion operator. It writes the second argument onto its first.

##### Compile It Into An Executable
```bash
$ g++ hello_moon.cpp -o hello
```

This should create a file called "hello". The `-o` flag here means it will output to a native
executable file with the specified name. In this case the name we specified is "hello". Go to your terminal and write `./hello` to execute it.

It should print "hello moon" in the terminal!

#### Variables
```cpp
#include <iostream>

using namespace std;

int main() {
  int numOfPeople;
  string location;
  float weightOfStuff;
  bool isItHappening;
  
  numOfPeople = 10;
  location = "Sausalito";
  weightOfStuff = 7.25;
  isItHappening = true; 
  
  cout << "number of people coming to BBQ is " << numOfPeople << endl;
  cout << "location of BBQ is " << location << endl;
  cout << "weight of all the stuff is " << weightOfStuff << " kgs." << endl;
  cout << "is is happening? " << isItHappening << endl;
}
```
`endl`  
This inserts a newline (`\n`) character and *flushes* the stream. Flushing a stream here ensures that all data that has been written to that stream is output, including clearing any that may have been buffered.

#### Input
```cpp
#include <iostream>

using namespace std;

int main() {
  int numOfPeople;
  float weightOfStuff = 7.25;
  
  cout << "enter number of people attending BBQ:" << endl;
  cin >> numOfPeople;
  
  cout << "number of people coming to BBQ is " << numOfPeople << endl;
  cout << "weight of all the stuff is " << weightOfStuff * numOfPeople << " kgs." << endl;
}
```

#### Vectors
Vectors in C++ are sequence containers representing arrays that can change in size.

### Data Types

* Integer (int) - Whole numbers.
* Float (float) - Decimal numbers.
* String (string) - Pieces of text.
* Boolean - True or False.
* Vectors

test
