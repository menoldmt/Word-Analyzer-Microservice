import time
import os

def get_word_length(word):
    return len(word)

def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

def count_repeats(word):
    char_counts = {}
    for char in word:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    repeats = [char for char, count in char_counts.items() if count > 1]
    return len(repeats) if repeats else "n"

def process_command(command, word):
    if command == "length":
        return get_word_length(word)
    elif command == "vowels":
        return count_vowels(word)
    elif command == "repeats":
        return count_repeats(word)
    else:
        return "Invalid command"

def microservice_A():
    input_file = "../input.txt"
    output_file = "../output.txt"

    while True:
        print("Checking for input...")
        if os.path.exists(input_file) and os.path.getsize(input_file) > 0:
            with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
                for line in file_in:
                    line = line.strip()
                    print(f"Read line: {line}")
                    parts = line.split(',')
                    if len(parts) != 2:
                        file_out.write("Invalid command\n")
                        print("Output: Invalid command")
                    else:
                        command, word = parts
                        result = process_command(command, word)
                        file_out.write(str(result) + "\n")
                        print(f"Processing line: {line}")
                        print(f"Output: {result}")

            # Clear input file after processing
            open(input_file, "w").close()

        time.sleep(3)  # Wait before checking again

if __name__ == "__main__":
    microservice_A()

