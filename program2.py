def longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
    - s: Input string
    
    Returns:
    - Length of the longest substring without repeating characters
    """
    if not s:
        return 0
    
    char_index = {}  # Dictionary to store the index of each character
    max_length = 0
    start = 0  # Start index of the current substring
    
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1  # Move the start index to the next character after the repeated one
        char_index[char] = i  # Update the index of the current character
        max_length = max(max_length, i - start + 1)  # Update the maximum length
        
    return max_length
