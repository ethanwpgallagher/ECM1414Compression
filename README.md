# ECM1414 Compression
Huffman Compression algorithm with compression and decompression functionality.

# INTRODUCTION
This project is affiliated with the University of Exeter and the BSc Computer Science course. It is a functioning compression module that utilises the Huffman algorithm. It has **compression** and **decompression** features, with the compressed files saving the Huffman tree needed for decompression.

Several packages are needed for this module and they're specified below. 

To submit bug reports please email eg546@exeter.ac.uk

# PREREQUISITES

This project is run on Python 3.8.6, with all modules working as intended on this version. Any future updates may change this functionality.

# INSTALLATIONS

This module requires the following modules to be downloaded via **pip**, the default Python package manager:
bitstring --> this is used to convert the binary string into a bit array. This needs to be installed via the command **pip install bitstring**. Ensure that the **BitArray** module is imported from this.
tqdm --> this package is used to show the progress of the compression in the form of a progress bar. This needs to be installed via the command **pip install tqdm**. Ensure that the **tqdm** and **trange** modules are imported from this package.

## GETTING STARTED

To get started with this module go into the directory of the file and run it using the following commands:
**py HuffmanCompression.py compress filename.txt filename.bin** or **py HuffmanCompression.py decompress filename.bin filename.txt**
It is essential that the file extensions are .txt and .bin for compressing and .bin and .txt for decompressing.
Furthermore if the files being read are not in the directory of the .py file then you either need to move them into the same directory or specify the full directory in the command line.
The new files will be saved to the current directory so if you want to move them this will have to be done manually. 

## DEVELOPER DOCUMENTATION 

The structure of the code:
All functions are above the main chunk of code for functionality with doc strings explaining functionality. 
The functionality within the try-except code can be edited to print certain messages or change the update level of the progress bar (how much the bar increases based on what has been completed).

## DETAILS
Author --> Ethan Gallagher
URI --> https://github.com/ethanwpgallagher/ECM1414Compression
License --> MIT License
Copyright (c) 2020 Ethan Gallagher
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
