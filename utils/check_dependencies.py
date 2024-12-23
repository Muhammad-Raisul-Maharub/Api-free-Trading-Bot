import importlib
import sys
import tkinter as tk
root = tk.Tk()
print(f"Tkinter version: {tk.TkVersion}")
root.destroy()
def check_dependencies():
    required_packages = {
        'selenium': 'selenium',
        'pandas': 'pandas',
        'numpy': 'numpy',
        'webdriver_manager': 'webdriver-manager',
        'dotenv': 'python-dotenv',
        'requests': 'requests',
        'tkinter': 'tk'
    }

    all_installed = True
    installed_versions = {}

    for package, pip_name in required_packages.items():
        try:
            module = importlib.import_module(package)
            if package == 'tkinter':
                root = tk.Tk()
                version = tk.TkVersion
                root.destroy()
            else:
                version = getattr(module, '__version__', 'Version not found')
            installed_versions[package] = version
            print(f"✓ {package} {version} is installed")
        except ImportError:
            all_installed = False
            print(f"✗ {package} is not installed")

    if all_installed:
        print("\nAll dependencies are properly installed!")
        print("\nInstalled versions:")
        for package, version in installed_versions.items():
            print(f"{package}: {version}")
    else:
        print("\nSome dependencies are missing. Run:")
        print("pip install -r requirements.txt")

if __name__ == "__main__":
    check_dependencies()
