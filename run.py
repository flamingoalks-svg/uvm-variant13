import sys
from assembler import assemble
from interpreter import interpret


def main():
    if len(sys.argv) != 4:
        print("Usage: python run.py <input.yaml> <output.bin> <memory.json>")
        sys.exit(1)

    yaml_file = sys.argv[1]
    bin_file = sys.argv[2]
    json_file = sys.argv[3]

    print("Assembling...")
    assemble(yaml_file, bin_file)

    print("Interpreting...")
    interpret(bin_file, json_file)

    print("Done. Memory dump saved to", json_file)


if __name__ == '__main__':
    main()
