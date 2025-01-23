import uuid
import sys
 
def generate_uuids(count):
    """
    Generate a list of Version 4 UUIDs.
    :param count: Number of UUIDs to generate.
    :return: List of UUID strings.
    """
    return [str(uuid.uuid4()) for _ in range(count)]
 
def main():
    # Display usage instructions
    if len(sys.argv) != 2:
        print("Usage: python UUID-Generator.py <number_of_uuids>")
        print("Example: python UUID-Generator.py 10")
        sys.exit(1)
 
    # Parse and validate the number of UUIDs
    try:
        num_uuids = int(sys.argv[1])
        if num_uuids <= 0:
            raise ValueError("Number of UUIDs must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        print("Please provide a valid positive integer as the number of UUIDs to generate.")
        sys.exit(1)
 
    # Generate UUIDs
    uuids = generate_uuids(num_uuids)
    print(f"Generated {num_uuids} UUID(s):")
    for u in uuids:
        print(u)
 
if __name__ == "__main__":
    main()
