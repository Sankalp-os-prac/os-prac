
import platform
import os
import sys

print("=== Tiny System Info ===")
print(f"Operating system: {platform.system()}")
print(f"OS version: {platform.release()}")
print(f"Python version: {sys.version.split()[0]}")
print(f"Architecture: {platform.machine()}")
print(f"Working directory: {os.getcwd()}")
print(f"Computer name: {platform.node()}")
