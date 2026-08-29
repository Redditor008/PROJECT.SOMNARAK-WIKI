import os
import glob
import re

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# Let's fix relative icon paths across all generated HTML files
for html_path in glob.glob(os.path.join(WIKI_DIR, "**/*.html"), recursive=True):
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    orig = content
    
    # In subdirectories (characters/, lore/, factions/, departments/, locations/, mechanics/)
    # replace ../assets/icons/icon_dept_f* with ../assets/layout/hand/icons/icon_dept_f*
    content = re.sub(r'\.\./assets/icons/icon_dept_f([1-8])', r'../assets/layout/hand/icons/icon_dept_f\1', content)
    content = re.sub(r'\.\./assets/icons/the_hand_dr_icon_styled\.svg', r'../assets/layout/hand/icons/the_hand_dr_icon_styled.svg', content)
    content = re.sub(r'\.\./assets/icons/somnarak_city_icon\.svg', r'../assets/layout/city/icons/somnarak_city_icon.svg', content)
    
    # In root pages
    content = re.sub(r'assets/icons/icon_dept_f([1-8])', r'assets/layout/hand/icons/icon_dept_f\1', content)
    content = re.sub(r'assets/icons/the_hand_dr_icon_styled\.svg', r'assets/layout/hand/icons/the_hand_dr_icon_styled.svg', content)
    content = re.sub(r'assets/icons/somnarak_city_icon\.svg', r'assets/layout/city/icons/somnarak_city_icon.svg', content)
    
    if orig != content:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Icon paths updated across all HTML files.")
