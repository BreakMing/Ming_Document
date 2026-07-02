import re

filepath = r'C:\Users\84580\Documents\Obsidian_Document\Ming_Document\technical_file\Kalman Filter.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Revert \sb{text} back to _{text}
content = re.sub(r'\\sb\{(.+?)\}', r'_{\1}', content)

# Step 2: Check for any remaining \sb patterns (shouldn't be any)
remaining = len(re.findall(r'\\sb', content))
print(f"Remaining \\sb occurrences: {remaining}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted all \\sb back to _")
