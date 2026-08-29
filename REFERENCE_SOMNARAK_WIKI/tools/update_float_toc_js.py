import os

with open('/home/user/01_Somnarak_Wiki/assets/js/wiki.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace float-toc trigger handler to support both static and dynamic float-tocs
old_trigger_code = """    const trigger = q('.float-toc-trigger', floatToc);
    if (trigger) {
      trigger.onclick = (e) => {
        e.stopPropagation();
        const isOpen = floatToc.classList.toggle('open');
        trigger.setAttribute('aria-expanded', String(isOpen));
      };

      document.addEventListener('click', (e) => {
        if (floatToc.classList.contains('open') && !floatToc.contains(e.target)) {
          floatToc.classList.remove('open');
          trigger.setAttribute('aria-expanded', 'false');
        }
      });
    }"""

new_trigger_code = """    const triggers = qa('.float-toc-trigger, .float-toc > button', floatToc);
    triggers.forEach(trigger => {
      trigger.onclick = (e) => {
        e.stopPropagation();
        const isOpen = floatToc.classList.toggle('open');
        trigger.setAttribute('aria-expanded', String(isOpen));
      };
    });

    document.addEventListener('click', (e) => {
      if (floatToc && floatToc.classList.contains('open') && !floatToc.contains(e.target)) {
        floatToc.classList.remove('open');
        triggers.forEach(tr => tr.setAttribute('aria-expanded', 'false'));
      }
    });"""

if old_trigger_code in js:
    js = js.replace(old_trigger_code, new_trigger_code)
    with open('/home/user/01_Somnarak_Wiki/assets/js/wiki.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("SUCCESS: Updated float-toc event listener in wiki.js!")
else:
    print("Trigger code block not directly matched, let's check...")
