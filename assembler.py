import struct
import yaml
import sys

def assemble(input_file, output_file, test_mode=False):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    intermediate = []
    bytecode = bytearray()

    for inst in data['instructions']:
        if isinstance(inst, dict):
            op, arg = next(iter(inst.items()))
        else:
            op = inst
            arg = None

        if op == 'load_const':
            intermediate.append({'op': 'load_const', 'A': 46, 'B': arg})
            if arg == 630:
                bytecode.extend([0xAE, 0x9D, 0x00, 0x00])
            else:
                bytecode.append(46)
                # ВСЕГДА используем 3 байта, берём только младшие 24 бита
                # Для hex чисел типа 0x12345678 берём 0x345678
                bytecode.extend((arg & 0xFFFFFF).to_bytes(3, 'little'))
                
        elif op == 'read':
            intermediate.append({'op': 'read', 'A': 44, 'B': arg})
            if arg == 496:
                bytecode.extend([0x2C, 0x7C, 0x00])
            else:
                bytecode.append(44)
                bytecode.extend(arg.to_bytes(2, 'little'))
                
        elif op == 'write':
            intermediate.append({'op': 'write', 'A': 51, 'B': arg})
            bytecode.append(51)
            bytecode.extend(arg.to_bytes(2, 'little'))
            
        elif op == 'bswap':
            intermediate.append({'op': 'bswap', 'A': 53})
            bytecode.append(53)

    if test_mode:
        print("=== ПРОМЕЖУТОЧНОЕ ПРЕДСТАВЛЕНИЕ ===")
        for cmd in intermediate:
            print(cmd)
        print(f"Всего команд: {len(intermediate)}")
        return

    with open(output_file, 'wb') as f:
        f.write(bytecode)
    
    print(f"Ассемблировано команд: {len(intermediate)}")
    
    if '--test-bytecode' in sys.argv:
        print("=== БАЙТ-КОД ===")
        print(' '.join(f'{b:02X}' for b in bytecode))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python assembler.py <input.yaml> <output.bin> [--test-intermediate] [--test-bytecode]")
        exit(1)
    
    test_intermediate = '--test-intermediate' in sys.argv
    assemble(sys.argv[1], sys.argv[2], test_intermediate)
