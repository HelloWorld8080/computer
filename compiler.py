import os
import re

import  pin
import assembly as ASM
dirname = os.path.dirname(__file__)
inputfile =  os.path.join(dirname, 'program1.asm')
outputfile = os.path.join(dirname, 'program.bin')
annotation = re.compile(r'(.*?);.*')

codes = []

op2 = {
    'MOV':ASM.MOV,
    'ADD':ASM.ADD,
    'SUB':ASM.SUB,
    'CMP':ASM.CMP,
    'AND':ASM.AND,
    'OR':ASM.OR,
    'XOR':ASM.XOR,
    'RCMP':ASM.RCMP
}
op1 = {
    'INC': ASM.INC,
    'DEC': ASM.DEC,
    'NOT': ASM.NOT,
    'JMP': ASM.JMP,
    'JO': ASM.JO,
    'JNO': ASM.JNO,
    'JZ': ASM.JZ,
    'JNZ': ASM.JNZ,
    'JP': ASM.JP,
    'JNP': ASM.JNP,
    'PUSH': ASM.PUSH,
    'POP': ASM.POP,
    'CALL':ASM.CALL,
    'INT': ASM.INT
}

op0 = {
    'NOP': ASM.NOP,
    'RET': ASM.RET,
    'IRET': ASM.IRET,
    'CLI': ASM.CLI,
    'STI': ASM.STI,
    'OBREAK':ASM.OBREAK,
    'HLT': ASM.HLT
}

OP2SET = set(op2.values())
OP1SET = set(op1.values())
OP0SET = set(op0.values())

REGISTERS = {
    "A": pin.A,
    'B': pin.B,
    'C': pin.C,
    'D': pin.D,
    'SP': pin.SP,
    'SS': pin.SS,
    'CS': pin.CS,
    'SI': pin.SI,
    'DI': pin.DI,
    'DS': pin.DS,
    'ES': pin.ES
}

marks = {}


class Code():
    def __init__(self, number, source:str):
        self.TYPE_CODE = 0
        self.TYPE_LABEL = 1
        self.number = number
        self.source = source.upper()
        self.op = None
        self.src = None
        self.dst = None
        self.index = 0
        self.name = None
        self.type = self.TYPE_CODE
        self.prepare_compile()
    def __repr__(self):
        return f'[{self.number}]-{self.source}'

    def get_op(self):
        if self.op in op2:
            return op2[self.op]
        if self.op in op1:
            return op1[self.op]
        if self.op in op0:
            return op0[self.op]
        raise SyntaxError(self)

    def get_am(self, addr):
        if not addr:
            return 0, 0
        if addr in marks:
            return pin.AM_INS, marks[addr].index*3
        if addr in REGISTERS:
            return pin.AM_REG, REGISTERS[addr]
        if re.match(r'^[0-9]+$',addr):
            return pin.AM_INS, int(addr)
        if re.match(r'^0X[0-9A-F]+$',addr):
            return pin.AM_INS,int(addr, 16)
        match = re.match(r'^\[(.+)\]$', addr)
        if match:
            if re.match(r'^[0-9]+$', match.group(1)):
                return pin.AM_DIR, int(match.group(1))
            if re.match(r'^0X[0-9A-F]+$',match.group(1)):
                return pin.AM_DIR, int(match.group(1), 16)
            if match.group(1) in REGISTERS:
                return pin.AM_RAM, REGISTERS[match.group(1)]
        raise SyntaxError(self)
    def prepare_compile(self):
        if self.source.endswith(":"):
            self.type = self.TYPE_LABEL
            self.name = self.source.strip(":")
            return

        tup = self.source.split(',')
        if len(tup) > 2:
            raise SyntaxError(self)
        if len(tup) == 2:
            self.src = tup[1].strip()
        tup = re.split(r' +', tup[0])
        if len(tup) > 2:
            raise SyntaxError(self)
        if len(tup) == 2:
            self.dst = tup[1].strip()

        self.op = tup[0].strip()
    def compile_code(self):
        op = self.get_op()

        amd, dst = self.get_am(self.dst)
        ams, src = self.get_am(self.src)
        if op in OP2SET:
            ir = op | (amd << 2) | ams
        elif op in OP1SET:
            ir = op | amd
        else:
            ir = op
        return [ir, dst, src]


class SyntaxError(Exception):
    def __init__(self, code:Code, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.code = code



def compile_program():
    with open(inputfile, encoding='utf-8') as file:
        lines = file.readlines()
    for index,line in enumerate(lines):
        source = line.strip()
        if not source:
            continue
        if ';' in source:
            match = annotation.match(source)
            source = match.group(1)
        source = source.strip()
        code = Code(index+1, source)
        codes.append(code)
    code = Code(index + 2, 'HLT')
    codes.append(code)

    results = []
    current = None
    for var in range(len(codes) - 1, -1, -1):
        code = codes[var]
        if code.type == code.TYPE_CODE:
            current = code
            results.insert(0, code)

            continue
        if code.type == code.TYPE_LABEL:
            marks[code.name] = current
            continue
        raise SyntaxError(code)
    for index,var in enumerate(results):
        var.index = index

    with open(outputfile,'wb') as file:
        for code in results:
            values = code.compile_code()
            for value in values:
                result = value.to_bytes(1, byteorder='little')
                file.write(result)


def main():
    # try:
        compile_program()
    # except SyntaxError as e:
    #     print(f'Syntax error at {e.code}')
    #     return
    # print("compile finished")
if __name__ == '__main__':
    main()