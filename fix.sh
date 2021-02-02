#!/bin/bash

sudo python3 new-grub.py

sudo mv /etc/default/grub /etc/default/grub.bak
sudo mv /etc/default/grub.new /etc/default/grub

sudo update-grub

