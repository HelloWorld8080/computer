#include<stdio.h>
typedef struct descriptor /* 共 8 个字节 */
{
    unsigned short limit_low;      // 段界限 0 ~ 15 位
    unsigned int base_low : 24;    // 基地址 0 ~ 23 位 16M
    unsigned char type : 4;        // 段类型
    unsigned char segment : 1;     // 1 表示代码段或数据段，0 表示系统段
    unsigned char DPL : 2;         // Descriptor Privilege Level 描述符特权等级 0 ~ 3
    unsigned char present : 1;     // 存在位，1 在内存中，0 在磁盘上
    unsigned char limit_high : 4;  // 段界限 16 ~ 19;
    unsigned char available : 1;   // 该安排的都安排了，送给操作系统吧
    unsigned char long_mode : 1;   // 64 位扩展标志
    unsigned char big : 1;         // 32 位 还是 16 位;
    unsigned char granularity : 1; // 粒度 4KB 或 1B
    unsigned char base_high;       // 基地址 24 ~ 31 位
} __attribute__((packed)) descriptor;
void make_descripter(descriptor *dest,unsigned int base,unsigned int limit){
  dest->base_low = base & 0xffffff;
  dest->base_high = (base >> 24) & 0xff;
  
  dest->limit_low = limit & 0xffff;
  dest->limit_high = (limit >> 16) & 0xf;

}
int main(){
  descriptor dest;
  make_descripter(&dest, 0x10000,0x1000 - 1);
  dest.granularity = 0;
  dest.big = 1;
  dest.long_mode = 0;
  dest.present = 1;
  dest.DPL = 0;
  dest.segment = 1;
  dest.type = 0b0010;

  char *ptr = (char *)&dest;
  unsigned short value16 = *(short *)ptr;
  printf("dw 0x%x\n",value16);
  ptr +=2;
  value16 = *(short *)ptr;
  printf("dw 0x%x\n",value16);
  ptr +=2;
  unsigned char value8 = *(char *)ptr;
  printf("db 0x%x\n",value8);
  ptr++;
  value8 = *(char *)ptr;
  printf("db 0x%x\n",value8);
  ptr++;
  value8 = *(char *)ptr;
  printf("db 0x%x\n",value8);
  ptr++;
  value8 = *(char *)ptr;
  printf("db 0x%x\n",value8);
  return 0;
}