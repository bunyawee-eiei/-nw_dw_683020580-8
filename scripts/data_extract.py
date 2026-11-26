import os
import glob

def main():
    raw_files = glob.glob("data/raw/*.csv")
    legacy_files = glob.glob("data/legacy/*.csv")
    print(f"Extracted {len(raw_files)} raw files and {len(legacy_files)} legacy files.")

if __name__ == "__main__":
    main()
