---
title: QEmu
bookCollapseSection: true
---

Manual:

```sh
qemu-img create -f qcow2 ubuntu.img 50G
qemu-system-x86_64 -boot d -cdrom ubuntu.iso -m 4G -smp 2 -hda ubuntu.img -nic user,hostfwd=tcp::8888-:22
# reboot without cdrom
qemu-system-x86_64 -m 4G -smp 2 -hda ubuntu.img -nic user,hostfwd=tcp::8888-:22 -virtfs local,path=$PWD,mount_tag=host0,security_model=passthrough,id=host0 -nographic
```
