# Daily Programmer Challenge 314 
# Author: Afnan Enayet

import sys

# Returns the "offset" needed to rotate the string to find the 
# lexicographically minimal string. Returns an integer detailing 
# the degree of rotation needed
def find_rotate_offset(input_str):
    input_str = input_str.lower()
    offset = 0
    curr_str = input_str

    # Rotate through the string
    for i in range(len(input_str)):
        cmp_str = input_str[i:] + input_str[:i]
        
        # If the comparison string has a lower lexicographical ordering 
        # then replace the offset as the offset to return, and replace the 
        # recurring string
        if cmp_str < curr_str:
            curr_str = cmp_str
            offset = i
    return offset

def main():
    # Validate command line args
    if len(sys.argv) < 2:
        sys.exit(1)

    for string in sys.argv[1:]:
        offset = find_rotate_offset(string)
        rot_str = string[offset:] + string[:offset]
        print(str(offset) + " " + rot_str) 

    sys.exit(0)

# Wrapping main function
if __name__ == '__main__':
    main()

