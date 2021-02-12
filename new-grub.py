with open('/mnt/etc/default/grub', 'r') as gf:
    lines = gf.readlines()


new_grub = []
for line in lines:
    if line.find("GRUB_CMDLINE_LINUX_DEFAULT") < 0:
        if line[-1] != "\n":
            nlt = True
            new_line = line[:-1] + ' intel_idle.max_cstate=4' + line[-1]
        else:
            nlt = False
            new_line = line[:-2] + ' intel_idle.max_cstate=4' + line[-2]
        line = new_line
    new_grub.append(line)

with open('/mnt/etc/default/grub.new', 'w') as gf:
    if nlt:
        gf.write("".join(new_grub))
    else:
        gf.write("\n".join(new_grub))
