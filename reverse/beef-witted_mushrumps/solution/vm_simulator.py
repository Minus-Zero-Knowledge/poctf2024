import sys


class VirtualMachine:
    def __init__(self):
        self.memory = bytearray(0x100) # 256 bytes of memory
        self.temp = 0  # Register for computation (v6)
        self.program_counter = 0  # Pointer/index into the memory (v7)

    def initialize_memory(self):
        # Initialize memory with a predefined bytestring (64 bytes)
        self.memory[:64] = b"#1 6;L0# 9%k_ f#8*62p,&m0-!?>$20!5$!:7;-05(>,(76?=&1.#45</0;-1'!"
        return self.memory

    def execute_vm(self, a1: bytes, a2: int):
        while True:
            if self.program_counter >= a2:
                break

            opcode = a1[self.program_counter]       # Opcode (first byte)  v5
            index = a1[self.program_counter + 1]   # Index (second byte)  v4
            self.program_counter += 2

            match opcode:
                case 0x1:
                    self.temp = self.memory[index]  # Load value from memory at index v4 to v6
                case 0x2:
                    self.memory[index] = self.temp  # Store value in v6 to memory at index v4
                case 0x3:
                    self.temp += self.memory[index]  # Add memory value at index v4 to v6
                case 0x4:
                    self.temp -= self.memory[index]  # Subtract memory value at index v4 from v6
                case 0x5:
                    self.temp ^= self.memory[index]  # XOR memory value at index v4 with v6
                case 0x6:
                    sys.stdout.write(chr(self.temp))  # Print v6 as a character
                case 0xff:
                    print(f"\nVM stopped...")
                    return self.temp  # End VM execution
                case _:
                    print(f"Unknown instruction: {opcode}")
                    return None

        return self.temp


def main():
    vm = VirtualMachine()

    # Initialize memory
    memory = vm.initialize_memory()

    a1 = b"\x01\x00\x05\x01\x06\x00\xff\x00"  #0xFF000601050001
    a2 = len(a1)
    assert a2 == 8

    # Start executing the VM
    vm.execute_vm(a1, a2)

    print(memory)

if __name__ == "__main__":
    main()
