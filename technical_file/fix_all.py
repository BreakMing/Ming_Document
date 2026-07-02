import re

filepath = r'C:\Users\84580\Documents\Obsidian_Document\Ming_Document\technical_file\Kalman Filter.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Replace \\ with \cr (matrix row separators)
# \\\\ in Python raw string = two literal backslashes in the file
count_cr = content.count('\\\\')
content = content.replace('\\\\', '\\cr')
print(f"Fix 1 (\\\\ -> \\cr): {count_cr} replacements")

# Fix 2: Replace _ with \_ for LaTeX subscripts
# Only match _ followed by { or alphanumeric, not preceded by \
# This avoids matching escaped underscores or underscores in regular text
pattern = r'(?<!\\)_(?=\{|[a-zA-Z0-9])'
count_us = len(re.findall(pattern, content))
content = re.sub(pattern, r'\\_', content)
print(f"Fix 2 (_ -> \\_): {count_us} replacements")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
