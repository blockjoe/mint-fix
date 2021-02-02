with open('/etc/default/grub', 'r') as gf:
    lines = gf.readlines()


new_grub = []
for line in lines:
    if line.find("GRUB_CMDLINE_LINUX_DEFAULT") < 0:
        new_line = line[:-1] + ' intel_idle.max_cstate=4' + line[-1]
        line = new_line
    new_grub.append(line)

with open('/etc/default/grub.new', 'w') as gf:
    gf.write("\n".join(new_grub))
