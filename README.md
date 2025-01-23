# Fast Fourier Transform (FFT) Implementation
## Overview
This project implements the Fast Fourier Transform (FFT) using the Radix-2 algorithm in Python. It includes functionality to zero-pad the input to the next power of 2, compute the FFT recursively, and round the FFT result for better readability.

## Features
- Radix-2 FFT implementation.
- Zero-padding for input signals to the next power of 2.
- Recursive computation of FFT.
- Rounding of FFT results (both real and imaginary parts).
- User-friendly input and output display.

## Installation
No external dependencies are required. The implementation uses Python's built-in math and cmath modules.

## Usage
Run the script and provide a list of numbers separated by spaces. The program will compute the FFT and display the result.

### Running the Program
```bash
python fft.py
```

### Example Input & Output
#### Example 1:
```
Enter a list of numbers separated by spaces: 1 2 3 4
FFT result (rounded):
10.00 + 0.00i
-2.00 + 2.00i
-2.00 + 0.00i
-2.00 - 2.00i
```

#### Example 2:
```
Enter a list of numbers separated by spaces: 5 6 7 8
FFT result (rounded):
26.00 + 0.00i
-2.00 + 2.00i
-2.00 + 0.00i
-2.00 - 2.00i
```

## Functions
- `radix2(input_signal)`: Pads the input signal to the next power of 2 and computes FFT.
- `fastFourierTransform(input_signal)`: Recursively computes the FFT of the input signal.
- `round_fft_result(fft_result)`: Rounds the real and imaginary parts of the FFT output to two decimal places.
## Notes
- The program uses a recursive approach to compute the FFT using the Radix-2 algorithm.
- The input signal is padded with zeros to the next power of 2 if necessary.
- Results are rounded to two decimal places for better readability.
