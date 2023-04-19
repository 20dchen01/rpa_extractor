import sys
import os
import unrpa

def main():
    if len(sys.argv) != 2:
        print("Usage: drag and drop an .rpa file onto this script to decompile it.")
        return

    rpa_file = sys.argv[1]

    if not os.path.isfile(rpa_file) or not rpa_file.endswith(".rpa"):
        print("Please provide a valid .rpa file.")
        return

    output_folder = os.path.splitext(rpa_file)[0] + "_decompiled"
    os.makedirs(output_folder, exist_ok=True)

    try:
        unrpa.extract(rpa_file, output_folder)
        print(f"Decompiled .rpa file saved to: {output_folder}")
    except Exception as e:
        print(f"Error occurred while decompiling: {e}")

if __name__ == "__main__":
    main()
