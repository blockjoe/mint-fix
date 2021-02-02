#!/bin/bash

set -e

sudo mount /dev/sda2 /mnt

sudo mount --bind /dev /mnt/dev
sudo mount --bind /sys /mnt/sys
sudo mount --bind /proc /mnt/proc

sudo python3 new-grub.py

sudo mv /mnt/etc/default/grub /mnt/etc/default/grub.bak
sudo mv /mnt/etc/default/grub.new /mnt/etc/default/grub

sudo chroot /mnt

sudo update-grub

exit
