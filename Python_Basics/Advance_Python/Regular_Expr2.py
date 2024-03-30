import re

text = "The cat sat on the mat"

# Define a regular expression pattern with a capturing group for the word "cat" and "mat"
pattern = r'(\bcat\b).*(\bmat\b)'

# Find the match
match = re.search(pattern, text)

# Check if there's a match
if match:
    # Using match.group() to retrieve the entire matched substring
    print("Entire match:", match.group())
    
    # Using match.group(n) to retrieve specific capturing groups
    print("First capturing group (cat):", match.group(1))
    print("Second capturing group (mat):", match.group(2))
    
    # Using match.groups() to retrieve all captured groups as a tuple
    captured_groups = match.groups()
    print("All captured groups:", captured_groups)
else:
    print("No match found")

