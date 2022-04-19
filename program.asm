 mov ss,1
 mov sp,0x10
 JMP start
show:
    mov D,255
    iret
start:
    mov c,0
increase:
    inc c
    mov d,c
    JP disable
enable:
    sti
    jmp interrupt
disable:
    cli

interrupt:
    int show
    jmp increase

    HLT