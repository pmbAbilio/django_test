import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)

STATIC_ROOT = os.path.join(BASE_DIR, "../static/")

print(STATIC_ROOT)
