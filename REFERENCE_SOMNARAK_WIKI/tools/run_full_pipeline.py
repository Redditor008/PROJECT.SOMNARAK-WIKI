import subprocess

steps = [
    ("Removing floor rails from articles", "python3 /home/user/tools/remove_floor_rail_from_articles.py"),
    ("Standardizing all headers", "python3 /home/user/tools/standardize_all_headers.py"),
    ("Fixing icon paths", "python3 /home/user/tools/fix_icon_paths.py"),
    ("Wrapping tables safely", "python3 /home/user/tools/wrap_tables_safely.py"),
    ("Injecting inline wiki links and icons", "python3 /home/user/tools/inject_wiki_links_and_icons.py"),
    ("Updating hub index directories", "python3 /home/user/tools/update_hub_indices.py"),
    ("Re-fixing icon paths after hub update", "python3 /home/user/tools/fix_icon_paths.py"),
    ("Rebuilding search index", "python3 /home/user/tools/rebuild_search_index.py"),
]

for desc, cmd in steps:
    print(f"--> Running: {desc}...")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"ERROR in {desc}:\n{res.stderr}")
    else:
        print(f"    {res.stdout.strip()}")

print("\nPipeline Complete. Running final audit...")
