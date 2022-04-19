
import pin

FETCH = [
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.IR_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.DST_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.SRC_IN | pin.PC_INC,
]

MOV = (0 << pin.ADDR2_SHIFT) | pin.ADDR2
ADD = (1 << pin.ADDR2_SHIFT) | pin.ADDR2
SUB = (2 << pin.ADDR2_SHIFT) | pin.ADDR2
CMP = (3 << pin.ADDR2_SHIFT) | pin.ADDR2
AND = (4 << pin.ADDR2_SHIFT) | pin.ADDR2
OR = (5 << pin.ADDR2_SHIFT) | pin.ADDR2
XOR = (6 << pin.ADDR2_SHIFT) | pin.ADDR2
RCMP = (7 << pin.ADDR2_SHIFT) | pin.ADDR2


INC = (0 << pin.ADDR1_SHIFT) | pin.ADDR1
DEC = (1 << pin.ADDR1_SHIFT) | pin.ADDR1
NOT = (2 << pin.ADDR1_SHIFT) | pin.ADDR1
JMP = (3 << pin.ADDR1_SHIFT) | pin.ADDR1
JO = (4 << pin.ADDR1_SHIFT) | pin.ADDR1
JNO = (5 << pin.ADDR1_SHIFT) | pin.ADDR1
JZ = (6 << pin.ADDR1_SHIFT) | pin.ADDR1
JNZ = (7 << pin.ADDR1_SHIFT) | pin.ADDR1
JP = (8 << pin.ADDR1_SHIFT) | pin.ADDR1
JNP = (9 << pin.ADDR1_SHIFT) | pin.ADDR1
PUSH = (10 << pin.ADDR1_SHIFT) | pin.ADDR1
POP = (11 << pin.ADDR1_SHIFT) | pin.ADDR1
CALL = (12 << pin.ADDR1_SHIFT) | pin.ADDR1
INT = (13 << pin.ADDR1_SHIFT) | pin.ADDR1


NOP = 0
RET = 1
IRET = 2
STI = 3
CLI = 4
OBREAK = 5
HLT = 0x3f





INSTRUCTIONS = {
    2:{
        MOV:{
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_W | pin.SRC_OUT,
            ],
            (pin.AM_REG, pin.AM_DIR): [
                pin.SRC_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.DST_W,
            ],
            (pin.AM_DIR, pin.AM_INS): [
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_OUT,
            ],
            (pin.AM_RAM, pin.AM_INS): [
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_OUT,
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_W | pin.SRC_R,
            ],
            (pin.AM_DIR, pin.AM_REG): [
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_R,
            ],
            (pin.AM_RAM, pin.AM_REG): [
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_R,
            ],
            (pin.AM_REG, pin.AM_DIR): [
                pin.SRC_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.DST_W
            ],
            (pin.AM_DIR, pin.AM_DIR): [
                pin.SRC_OUT | pin.MAR_IN,
                pin.T1_IN | pin.RAM_OUT,
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
            (pin.AM_RAM, pin.AM_DIR): [
                pin.SRC_OUT | pin.MAR_IN,
                pin.T1_IN | pin.RAM_OUT,
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
            (pin.AM_REG, pin.AM_RAM): [
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.DST_W,
            ],
            (pin.AM_DIR, pin.AM_RAM): [
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
            (pin.AM_RAM, pin.AM_RAM): [
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],

        },
        ADD:{
            (pin.AM_REG, pin.AM_INS):[
                pin.SRC_OUT | pin.B_IN,
                pin.DST_R | pin.A_IN,
                pin.OP_ADD | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
            (pin.AM_REG, pin.AM_REG):[
                pin.SRC_R | pin.B_IN,
                pin.DST_R | pin.A_IN,
                pin.OP_ADD | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
        },
        SUB: {
            (pin.AM_REG, pin.AM_INS): [
                pin.SRC_OUT | pin.B_IN,
                pin.DST_R | pin.A_IN,
                pin.OP_SUB | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.SRC_R | pin.B_IN,
                pin.DST_R | pin.A_IN,
                pin.OP_SUB | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
        },
        CMP: {
            (pin.AM_REG, pin.AM_INS): [
                pin.SRC_OUT | pin.B_IN,
                pin.DST_R | pin.A_IN,
                pin.OP_SUB | pin.ALU_PSW
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.SRC_R | pin.B_IN,
                pin.DST_R | pin.A_IN,
                pin.OP_SUB | pin.ALU_PSW
            ],
        },
        RCMP: {
            (pin.AM_REG, pin.AM_INS): [
                pin.SS_OUT | pin.MSR_IN | pin.ALU_PSW_OUT ,
                pin.SP_OUT | pin.MAR_IN | pin.ALU_PSW_OUT,
                pin.SRC_OUT | pin.B_IN | pin.ALU_PSW_OUT,
                pin.DST_R | pin.A_IN | pin.ALU_PSW_OUT,
                pin.OP_SUB | pin.ALU_PSW | pin.RAM_OUT | pin.PC_IN,
                pin.SP_OUT | pin.A_IN | pin.ALU_PSW_OUT ,
                pin.OP_INC | pin.ALU_OUT | pin.SP_IN | pin.ALU_PSW_OUT,
                pin.MSR_IN | pin.CS_OUT | pin.ALU_PSW_OUT,
            ],
        },
        AND: {
            (pin.AM_REG, pin.AM_INS): [
                pin.SRC_OUT | pin.B_IN,
                pin.DST_R | pin.A_IN,
                pin.OP_AND | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.SRC_R | pin.B_IN,
                pin.DST_R | pin.A_IN,
                pin.OP_AND | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
        },
        OR: {
            (pin.AM_REG, pin.AM_INS): [
                pin.SRC_OUT | pin.B_IN,
                pin.DST_R | pin.A_IN,
                pin.OP_OR | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.SRC_R | pin.B_IN,
                pin.DST_R | pin.A_IN,
                pin.OP_OR | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
        },
        XOR: {
            (pin.AM_REG, pin.AM_INS): [
                pin.SRC_OUT | pin.B_IN,
                pin.DST_R | pin.A_IN,
                pin.OP_XOR | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
            (pin.AM_REG, pin.AM_REG): [
                pin.SRC_R | pin.B_IN,
                pin.DST_R | pin.A_IN,
                pin.OP_XOR | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
        },
    },
    1:{
        INC:{
            (pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.OP_INC | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
        },
        DEC:{
            (pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
        },
        NOT: {
            (pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.OP_NOT | pin.ALU_OUT | pin.ALU_PSW | pin.DST_W
            ],
        },
        JMP: {
            (pin.AM_INS): [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JO: {
            (pin.AM_INS): [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JNO: {
            (pin.AM_INS): [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JZ: {
            (pin.AM_INS): [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JNZ: {
            (pin.AM_INS): [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JP: {
            (pin.AM_INS): [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JNP: {
            (pin.AM_INS): [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        PUSH:{
            (pin.AM_REG): [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.ALU_PSW | pin.SP_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.DST_R,
                pin.MSR_IN | pin.CS_OUT,
            ],
            (pin.AM_INS): [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.ALU_PSW | pin.SP_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.DST_OUT,
                pin.MSR_IN | pin.CS_OUT,
            ],
        },
        POP: {
            (pin.AM_REG): [
                pin.SS_OUT | pin.MSR_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.DST_W,
                pin.SP_OUT | pin.A_IN,
                pin.OP_INC | pin.ALU_OUT | pin.ALU_PSW | pin.SP_IN,
                pin.MSR_IN | pin.CS_OUT,
            ],
        },
        CALL:{
            (pin.AM_INS): [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.ALU_PSW | pin.SP_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.PC_OUT,
                pin.MSR_IN | pin.CS_OUT,
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        INT:{
            (pin.AM_INS): [
                pin.SP_OUT | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.ALU_PSW | pin.SP_IN,
                pin.SS_OUT | pin.MSR_IN,
                pin.SP_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.PC_OUT,
                pin.MSR_IN | pin.CS_OUT,
                pin.DST_OUT | pin.PC_IN | pin.ALU_PSW | pin.ALU_CLI,
            ],
        },
    },
    0:{
        NOP:[
            pin.CYC,
        ],
        HLT:[
            pin.HLT,
        ],
        RET:[
            pin.SS_OUT | pin.MSR_IN,
            pin.SP_OUT | pin.MAR_IN,
            pin.RAM_OUT | pin.PC_IN,
            pin.SP_OUT | pin.A_IN,
            pin.OP_INC | pin.ALU_OUT | pin.ALU_PSW | pin.SP_IN,
            pin.MSR_IN | pin.CS_OUT,
        ],
        IRET: [
            pin.SS_OUT | pin.MSR_IN,
            pin.SP_OUT | pin.MAR_IN,
            pin.RAM_OUT | pin.PC_IN,
            pin.SP_OUT | pin.A_IN,
            pin.OP_INC | pin.ALU_OUT | pin.ALU_PSW | pin.SP_IN,
            pin.MSR_IN | pin.CS_OUT | pin.ALU_PSW | pin.ALU_STI,
        ],
        CLI:[
            pin.ALU_PSW | pin.ALU_CLI,
        ],
        STI: [
            pin.ALU_PSW | pin.ALU_STI,
        ],
        OBREAK:[
            pin.SS_OUT | pin.MSR_IN | pin.ALU_PSW_OUT,
            pin.SP_OUT | pin.MAR_IN | pin.ALU_PSW_OUT,
            pin.RAM_OUT | pin.PC_IN | pin.ALU_PSW_OUT,
            pin.SP_OUT | pin.A_IN | pin.ALU_PSW_OUT,
            pin.OP_INC | pin.ALU_OUT | pin.SP_IN | pin.ALU_PSW_OUT,
            pin.MSR_IN | pin.CS_OUT | pin.ALU_PSW_OUT,
        ],
    }
}