def swap_and_concat(str1, str2):
    # Check if both strings have at least 2 characters
    '''if len(str1) < 2 or len(str2) < 2:
        print("Both strings should have at least 2 characters.")
        return None'''
    
    # Swap characters at position 1
    swapped_str1 = str2[0] + str1[1:]
    swapped_str2 = str1[0] + str2[1:]

    # Concatenate the swapped strings with a space in between
    result_string = swapped_str1 + ' ' + swapped_str2

    return result_string

# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = swap_and_concat(string1, string2)

if result:
    print("Result:", result)
