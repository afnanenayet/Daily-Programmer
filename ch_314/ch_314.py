# Daily Programmer Challenge 314 
# Author: Afnan Enayet

import sys

# Returns the "offset" needed to rotate the string to find the 
# lexicographically minimal string. Returns an integer detailing 
# the degree of rotation needed
def find_rotate_offset(input_str):
    return min(
        [
            (i, input_str[i:] + input_str[:i]) 
            for i in range(len(input_str.lower()))
        ], 
        key = lambda x: x[1]
    )

def main():
    # Validate command line args
    if len(sys.argv) < 2:
        sys.exit(1)

    for string in sys.argv[1:]:
        offset = find_rotate_offset(string)
        print(offset[0], offset[1])

    sys.exit(0)

# Wrapping main function
if __name__ == '__main__':
    main()

