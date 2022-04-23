# VMWare 安装
官网地址：https://www.vmware.com/
![img.png](img.png)
注意点：
- 取消软件自动更新

# 安装Archlinux系统
## Archlinux系统pacman包管理器常用命令（地址：https://www.jianshu.com/p/ea651cdc5530）

安装教程地址：  
http://blog.ccyg.studio/article/4f6cfa0a-ad98-4adb-af08-79a8a5b1d674/
注意点:
- ArchLinux默认没有ifconfig命令请使用 ip addr 命令
- 出现error: failed to get canonical path of `airootfs' 是因为你没有安装系统并生成完成文件系统表后，没有输入 arch-chroot /mnt 进入系统如图所示![img_1.png](img_1.png)
- 出现以下错误请删除 C:/Users/11931/.ssh/known_hosts下的192.168.....这一行![img_2.png](img_2.png)
- 通过df -h命令可以查看磁盘的使用情况。 

## 安装镜像
- `pacman -Sy` 将pacman同步最新的数据库。出现问题请重启虚拟机
- `pacman -Ss mirrorlist` 在pacman中搜索镜像链接文件![img_4.png](img_4.png)
- `pacman -S pacman-mirrorlist` 下载镜像链接文件
- `cd /etc/pacman.d` 然后`ls` 查看下载后的链接文件名![img_6.png](img_6.png)
- 然后`cat mirrorlist.pacnew | grep China -A 24 > mirrorlist` 找到24个中国的镜像链接的添加到mirrorlist中
- 最后`vim mirrorlist`选着一个镜像http链接打开并保存。![img_7.png](img_7.png)
## 安装系统引导![img_9.png](img_9.png)
注意点：
- /dev/sdb 是磁盘不是分区。

#安装gnome图形界面
- `pacman -Syu` 更新系统
- `pacman -S gnome gnome-extra`,安装 gnome，出现选项之后点击 Enter，时间较长，请耐心等待，(若安装失败，请使用上面的命令更新系统)
- `pacman -S xorg xorg-xinit` 安装驱动
- `echo "exec gnome-session" > ~/.xinitrc` 编辑文件 ~/.xinitrc 输入 exec gnome-session 保存（在root和账户都要设置）
- 然后在虚拟机中输入命令 `startx` ，稍等片刻，就可以启动 gnome 图形界面了
- `vim /etc/default/grub` 打开default/grub修改GRUB_TIMEOUt的值为0![img_10.png](img_10.png)
- `grub-mkconfig -o /boot/grub/grub.cfg` 更新grup配置文件。
- `systemctl enable gdm` 开机自启动图形化界面。
- 添加终端快捷键 https://blog.csdn.net/qq_15601471/article/details/92781475
