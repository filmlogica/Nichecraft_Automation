import subprocess
import importlib

REQUIRED_LIBS = [
    "requests", "flask", "python-dotenv", "pytrends", "pillow", "openai", "pandas"
]

def install_if_missing(package):
    try:
        importlib.import_module(package)
        print(f"✅ {package} already installed.")
    except ImportError:
        print(f"📦 Installing {package}...")
        subprocess.check_call(["pip", "install", package])

if __name__ == "__main__":
    for lib in REQUIRED_LIBS:
        install_if_missing(lib)
