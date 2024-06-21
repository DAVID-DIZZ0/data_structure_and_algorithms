def character_frequency(string):
   
    # Initialize an empty dictionary to store character frequencies
    frequency_dict = {}
    
    # Iterate through each character in the string
    for char in string:
        # Check if the character is alphabetic
        if char.isalpha():
            # Convert the character to lowercase to handle case insensitivity
            char_lower = char.lower()
            # If the character is already in the dictionary, increment its count
            if char_lower in frequency_dict:
                frequency_dict[char_lower] += 1
            # If the character is not in the dictionary, add it with count 1
            else:
                frequency_dict[char_lower] = 1
    
    # Return the dictionary containing character frequencies
    return frequency_dict
