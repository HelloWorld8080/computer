import os

# dirname = os.path.dirname(os.path.abspath(__file__))
# with open(os.path.join(dirname,'8bit2_8.bin'),'wb') as file:
#     for var in range(256):
#         var = int(str(var),base = 16);
#         print(var)
#         byte = var.to_bytes(2,byteorder='little')
#         file.write(byte)

#微程序控制
# dirname = os.path.dirname(os.path.abspath(__file__))
# WE_A = 2**0
# CS_A = 2**1
#
# WE_B = 2**2
# CS_B = 2**3
#
# WE_C = 2**4
# CS_C = 2**5
#
# ALU_ADD = 0
# ALU_SUB = 2**6
# ALU_OUT = 2**7
#
# WE_M = 2**8
# CS_M = 2**9
#
# WE_PC = 2**10
# EN_PC = 2**11
# CS_PC = 2**12
#
# HLT = 2**15
#
# micro = [
#     CS_M | CS_A | WE_A | WE_PC | EN_PC | CS_PC,
#     CS_M | CS_B | WE_B | WE_PC | EN_PC | CS_PC,
#     ALU_OUT | CS_C | WE_C,
#     WE_M | CS_M | CS_C,
#     HLT
# ]
# with open(os.path.join(dirname,'inst.bin'),'wb') as file:
#     for var in micro:
#         # var = int(str(var),base = 16);
#         # print(var)
#         byte = var.to_bytes(2,byteorder='little')
#         file.write(byte)


# 控制寄存器
dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname,"inst.bin")

with open(filename,'wb') as file:
    for var in range(32):
        var= 1<<var;
        print(var)
        file.write(var.to_bytes(4,byteorder='little'))