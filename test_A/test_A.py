import time

def write_to_input(commands):
    input_file = "../input.txt"
    print("Sending commands to microservice A:")
    with open(input_file, "w") as file:
        for command in commands:
            print(f"Sent: {command}")
            file.write(command + "\n")

def read_output():
    output_file = "../output.txt"
    time.sleep(6)  # Allow time for processing
    try:
        with open(output_file, "r") as file:
            results = [line.strip() for line in file.readlines()]
            print("Received responses from microservice A:")
            for result in results:
                print(f"Received: {result}")
            return results
    except FileNotFoundError:
        print("Error: output.txt not found")
        return []

def test_microservice():
    test_cases = {
        "length,dog": "3",
        "vowels,cat": "1",
        "repeats,tennis": "n"
    }

    commands = list(test_cases.keys())
    write_to_input(commands)
    read_output()

if __name__ == "__main__":
    test_microservice()
