# UUID Generator Script

This Python script generates a specified number of Version 4 UUIDs (Universally Unique Identifiers). It is designed to be simple, efficient, and easy to use from the command line.

## Features
- Generates Version 4 UUIDs (randomly generated).
- Accepts user input to specify the number of UUIDs to generate.
- Includes error handling for invalid or missing input.
- Provides clear usage instructions.

## Prerequisites
Ensure that you have Python installed on your system. This script is compatible with Python 3.

## Usage
### Step 1: Save the Script
Save the script as `UUID-Generator.py` in your desired directory. 

### Step 2: Run the Script
Open a terminal or command prompt, navigate to the directory containing the script, and run the following command:

```bash
python UUID-Generator.py <number_of_uuids>
```

Replace `<number_of_uuids>` with the number of UUIDs you want to generate.

### Example
To generate 5 UUIDs:

```bash
python UUID-Generator.py 5
```

#### Output:
```
Generated 5 UUID(s):
b48c65a8-83c9-4ad5-b1e9-1ccfc9c4ed45
2fcb85fa-2976-4fc6-a4ae-c15da08ff4c0
5c793f36-843e-4841-85dc-e68e055cd635
4a9e1e62-1d78-4882-868c-335c46fb4caf
a3d96d84-d4f9-4b0f-aa4b-17f430648644
```

## Error Handling
- If you do not provide the correct number of arguments, the script will display usage instructions.
- If you provide a non-integer or negative value, the script will display an error message and terminate.

### Examples of Invalid Input:
#### Missing Argument:
```bash
python UUID-Generator.py
```
**Output:**
```
Usage: python UUID-Generator.py <number_of_uuids>
Example: python UUID-Generator.py 10
```

#### Invalid Argument (e.g., negative or non-integer):
```bash
python UUID-Generator.py -5
```
**Output:**
```
Error: Number of UUIDs must be a positive integer.
Please provide a valid positive integer as the number of UUIDs to generate.
```

## License
This script is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contributions
Feel free to submit issues or pull requests if you would like to contribute to improving this script.

## Author
This script was created to simplify the generation of UUIDs for various development and testing purposes.
