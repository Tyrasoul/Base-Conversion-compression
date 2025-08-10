# Base Conversion Compressor

A lightweight compression/decompression tool using base conversion.  
I tested multiple approaches (dictionary coding (using unicode), pattern replacement, etc.), but for datasets with **less than ~100 unique characters** in randomness, base conversion consistently performed best.

---

## Features
- Supports alphabets (`a-z`)
- Supports numbers (`0-9`)
- Simple CLI interface with cinematic printing
- Easy to integrate as a Python module
- Includes automated tests

---

## How It Works
1. Each character is mapped to a number.
2. The string is converted into a large decimal integer using base conversion.
3. This integer is stored as compressed binary-like characters.
4. Decompression reverses the process.


---

## Notes
- This method works best when the variety of characters (randomness) in the dataset is **<100 unique characters**, even if the dataset is large in size.
- No external dependencies required.
- Best results when length of given data is large


## Example
