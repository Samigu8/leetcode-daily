import os
from datetime import datetime

solutions_dir = "solutions"
files = sorted(os.listdir(solutions_dir))

with open("README.md", "w") as readme:
    readme.write("# LeetCode Daily Progress\n\n")
    readme.write("Automatically updated after each push.\n\n")
    readme.write("## Latest Solutions\n\n")

    for f in files[-10:]:
        readme.write(f"- {f}\n")

    readme.write("\n---\n")
    readme.write(f"Last updated: {datetime.now()}\n")
