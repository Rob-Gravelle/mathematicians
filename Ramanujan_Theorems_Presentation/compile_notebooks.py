import os
from glob import glob
import subprocess
import sys
import asyncio

# Fix zmq warning on Windows
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Directory configuration
base_dir = "ramanujan"  # .ipynb files
output_dir = "html"     # .html files
template = "lab"        # Jupyter lab template for HTML

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Convert notebooks to HTML
for nb in sorted(glob(os.path.join(base_dir, "0*_*.ipynb"))):
    nb_name = os.path.splitext(os.path.basename(nb))[0]
    
    # Convert to HTML
    print(f"📘 Exporting {nb} → HTML...")
    html_cmd = f'jupyter nbconvert --to html --execute "{nb}" --template {template} --output-dir="{output_dir}"'
    html_result = subprocess.run(html_cmd, shell=True, capture_output=True, text=True)
    if html_result.returncode != 0:
        print(f"❌ Error converting {nb} to HTML: {html_result.stderr}", file=sys.stderr)
        continue

print("✅ Compilation complete!")