import glob
import re

files = glob.glob("SOMNARAK-WORLD/**/*.md", recursive=True)

# 1. Regex to replace word., with word;
# e.g., "discrepancy., personnel" -> "discrepancy; personnel"
# "action., a" -> "action; a"
p_dot_comma = re.compile(r'\b([a-z]{2,})\.,\s*([a-zA-Z])')

# 2. Regex to replace exact double dot (..) with single dot (.)
p_double_dot = re.compile(r'(?<!\.)\.\.(?!\.)')

cleaned_files = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        orig = fp.read()
    
    txt = p_dot_comma.sub(r'\1; \2', orig)
    txt = p_double_dot.sub(r'.', txt)
    
    if txt != orig:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(txt)
        cleaned_files += 1

print(f"Cleaned dot-comma and double-dot artifacts in {cleaned_files} files!")
