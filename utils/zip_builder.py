import zipfile
from pathlib import Path

def build_zip(title="product", include_image=True):
    zip_name = f"{title.replace(' ', '_')}.zip"

    with zipfile.ZipFile(zip_name, 'w') as zipf:
        # Add required files
        for file in ["README.txt", "LICENSE.txt"]:
            if Path(file).exists():
                zipf.write(file)

        if include_image and Path("generated_image.png").exists():
            zipf.write("generated_image.png")

    print(f"📦 Created ZIP file: {zip_name}")
    return zip_name
