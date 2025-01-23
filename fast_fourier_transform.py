import math
import cmath

def radix2(input):
    """
    pads input to the next power of 2 and computes FFT
    """
    N = 2**math.ceil(math.log2(len(input))) # Next power of 2
    input += [0]* (N- len(input)) # Zero-padding
    return fastFourierTransform(input)

def fastFourierTransform(input):
    """
    Recursively compute the FFT of the input
    """
    N = len(input)
    if N == 1:
        return input # Base case
    
    # FFT for even and odd indexed elements
    a = fastFourierTransform(input[::2])
    b = fastFourierTransform(input[1::2])

    result = [0]*N

    # Compute results with twiddle factors
    for k in range(N//2):
        W = cmath.exp(-2j * cmath.pi * k / N)
        result[k] = a[k] + W*b[k]
        result[k + N//2] = a[k] - W*b[k]

    return result

def round_fft_result(fft_result):
    """
    Round the real and imaginarypart of each FFT output
    """
    rounded_result = [complex(round(c.real), round(c.imag)) for c in fft_result]
    return rounded_result

if __name__ == "__main__":
    # Accept user input and perform FFT
    input = input("Enter a list of numbers separated by spaces: ")
    try:

        list = [float(x) for x in input.split()]
        result = round_fft_result(radix2(list))
        print(result)
    except ValueError:
        print("Please enter a valid list of numbers.")