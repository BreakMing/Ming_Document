import re

filepath = r'C:\Users\84580\Documents\Obsidian_Document\Ming_Document\technical_file\Kalman Filter.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace _ with \_ (escaped underscore) in math subscript patterns
# This way: \_ → Markdown → _ → MathJax → subscript
# Works on both GitHub and Obsidian reading mode

# Step 1: Replace _{...} with \_{...} (already-braced subscripts)
count1 = len(re.findall(r'(?<!\\)_\{', content))
content = re.sub(r'(?<!\\)_\{', r'\\_{', content)

# Step 2: Replace _X with \_{X} (single-char subscripts, wrap in braces)
count2 = len(re.findall(r'(?<!\\)_(?=[a-zA-Z0-9])', content))
content = re.sub(r'(?<!\\)_(?=[a-zA-Z0-9])', r'\\_{', content)
# Close the braces we just opened
# \_{X should become \_{X}
content = re.sub(r'(\\_\{[a-zA-Z0-9])(?=[\^\\\s\$,\)\]\}\;\.\-\+a-zA-Z0-9])', r'\1}', content)
# Also close at end of line/string
content = re.sub(r'(\\_\{[a-zA-Z0-9])$', r'\1}', content, flags=re.MULTILINE)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done!")
print(f"  Step 1 (braced: _{{...}} -> \\_{{...}}): {count1} replacements")
print(f"  Step 2 (single-char: _X -> \\_{{X}}): {count2} replacements")
