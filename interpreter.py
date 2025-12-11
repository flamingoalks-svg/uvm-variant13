import json
import struct

def interpret(code_file, memory_dump_file):
    with open(code_file, 'rb') as f:
        code = f.read()

    stack = []
    memory = {}
    pc = 0

    while pc < len(code):
        first_byte = code[pc]
        A = first_byte & 0x3F
        
        if A == 46:
            if pc + 4 > len(code):
                break
            cmd_bytes = code[pc:pc+4]
            cmd = int.from_bytes(cmd_bytes, 'little')
            B = cmd >> 6
            stack.append(B)
            pc += 4
            
        elif A == 44:
            if pc + 3 > len(code):
                break
            cmd_bytes = code[pc:pc+3]
            cmd = int.from_bytes(cmd_bytes + b'\x00', 'little')
            B = cmd >> 6
            stack.append(memory.get(B, 0))
            pc += 3
            
        elif A == 51:
            if pc + 3 > len(code):
                break
            cmd_bytes = code[pc:pc+3]
            cmd = int.from_bytes(cmd_bytes + b'\x00', 'little')
            B = cmd >> 6
            val = stack.pop()
            memory[B] = val
            pc += 3
            
        elif A == 53:
            val = stack.pop()
            bswapped = ((val & 0xFF) << 24) | ((val & 0xFF00) << 8) | \
                       ((val & 0xFF0000) >> 8) | ((val & 0xFF000000) >> 24)
            stack.append(bswapped)
            pc += 1
            
        else:
            print(f'Неизвестная команда: A={A}')
            break

    with open(memory_dump_file, 'w', encoding='utf-8') as f:
        json.dump(memory, f, indent=2)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: python interpreter.py <input.bin> <memory.json>')
        exit(1)
    interpret(sys.argv[1], sys.argv[2])
