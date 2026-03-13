def binary2decimal(binary: str) -> int:
    decimal = 0
    
    for index, digit in enumerate(reversed(binary)):
        if digit not in '01':
            raise ValueError("Input must be a binary string containing only '0' and '1'.")

        decimal += int(digit) * (2 ** index)

    return decimal


if __name__ == "__main__":
    try:
        binary_input = input("Enter your Binary: ")
        result = binary2decimal(binary_input)
        print("Decimal : ", result)
    except ValueError as e:
        print("Error:", e)