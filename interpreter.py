import json

def interpret(code_file, memory_dump_file):
    with open(code_file, 'rb') as f:
        code = f.read()

    stack = []
    memory = {}
    pc = 0

    while pc < len(code):
        op = code[pc]
        
        if op == 46:  # load_const (46)
            if pc + 4 > len(code):
                break
            # Читаем следующие 3 байта как число
            # Это числа типа 100, 200, 300
            const_bytes = code[pc+1:pc+4]
            const = int.from_bytes(const_bytes, 'little')
            stack.append(const)
            pc += 4
            
        elif op == 44:  # read (44)
            if pc + 3 > len(code):
                break
            addr = int.from_bytes(code[pc+1:pc+3], 'little')
            stack.append(memory.get(addr, 0))
            pc += 3
            
        elif op == 51:  # write (51)
            if pc + 3 > len(code):
                break
            addr = int.from_bytes(code[pc+1:pc+3], 'little')
            val = stack.pop()
            memory[addr] = val
            pc += 3
            
        elif op == 53:  # bswap (53)
            val = stack.pop()
            # Разворот байтов 32-битного числа
            bswapped = ((val & 0xFF) << 24) | ((val & 0xFF00) << 8) | \
                       ((val & 0xFF0000) >> 8) | ((val & 0xFF000000) >> 24)
            stack.append(bswapped)
            pc += 1
            
        else:
            print(f'Неизвестный код операции: {op}')
            break

    with open(memory_dump_file, 'w', encoding='utf-8') as f:
        json.dump(memory, f, indent=2)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: python interpreter.py <input.bin> <memory.json>')
        exit(1)
    interpret(sys.argv[1], sys.argv[2])
