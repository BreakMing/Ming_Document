import re

filepath = r'C:\Users\84580\Documents\Obsidian_Document\Ming_Document\technical_file\Kalman Filter.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Replace _{...} with \sb{...} (already-braced subscripts)
# e.g., _{k} -> \sb{k}, _{k-1} -> \sb{k-1}
count1 = len(re.findall(r'_\{(.+?)\}', content))
content = re.sub(r'_\{(.+?)\}', r'\\sb{\1}', content)

# Step 2: Replace single-char subscripts _x with \sb{x}
# e.g., _k -> \sb{k}, _0 -> \sb{0}
count2 = len(re.findall(r'(?<!\\)_(?=[a-zA-Z0-9])', content))
content = re.sub(r'(?<!\\)_(?=[a-zA-Z0-9])', r'\\sb{', content)
# Now we need to close the braces after the single char
# We inserted \sb{ before the char, so _k becomes \sb{k
# We need to add } after the char: \sb{k}
# Find \sb{X pattern and close with }
content = re.sub(r'(\\sb\{[a-zA-Z0-9])(?=[\^\\\s\$,\)\]\}\;\.\-\+])', r'\1}', content)
# Also handle end-of-string or end-of-line cases
content = re.sub(r'(\\sb\{[a-zA-Z0-9])$', r'\1}', content, flags=re.MULTILINE)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! Replaced {count1} braced subscripts and {count2} single-char subscripts.")
