# demo.py
# Interactive CLI for compressor

from compressor import compress_data, decompress_data

print("Welcome to Base Conversion Compressor!")

while True:
    print("\nMenu:")
    print("1. Compress")
    print("2. Decompress")
    print("3. Exit")
    choice = input("- ")

    if choice == "1":
        mode = input("Enter mode ('alpha' for letters, 'num' for numbers): ").strip().lower()
        data = input("Enter data: ").strip()
        try:
            compressed = compress_data(data, mode)
            print("Compressed data:", compressed)
            print(f"Original length: {len(data)} | Compressed length: {len(compressed)}")
            print(f"Compression: {round(100 - (len(compressed) * 100 / len(data)), 2)}%")
        except ValueError as e:
            print("Error:", e)

    elif choice == "2":
        data = input("Enter compressed data: ")
        try:
            decompressed = decompress_data(data)
            print("Decompressed data:", decompressed)
        except ValueError as e:
            print("Error:", e)

    elif choice == "3":
        break
    else:
        print("Invalid choice.")
