mov c,5
mov ss,2
mov sp,0x10

mov SI,1
mov DI,0xE0
call save

mov C,5
mov SI,1
mov DI,0xF0
call save

mov c,5
mov DS,0xF0
mov ES,0xE0
mov D,0
call solve

HLT
save:
    cmp c,1
    obreak
    dec c
    mov [DI],SI
    INC SI
    INC DI
    JMP save
    HLT

solve:
    cmp c,1
    obreak
    dec c
    mov DI,[DS]
    mov SI,[ES]
    call mutiAB
    INC DS
    INC ES
    JMP solve
    HLT

mutiAB:
    cmp DI,1
    obreak
    DEC DI
    add d,SI
    JMP mutiAB
    HLT

