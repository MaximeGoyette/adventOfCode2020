data = open('8.txt').read().split('\n')


changed = set()

while True:
    lines2 = []
    found = False
    for i, line in enumerate(data):
        if not found and (line.startswith('nop') or line.startswith('jmp')) and i not in changed:
            changed.add(i)
            found = True
            if line.startswith('nop'):
                lines2.append(line.replace('nop', 'jmp'))
            else:
                lines2.append(line.replace('jmp', 'nop'))
        else:
            lines2.append(line)
    i = 0
    accumulator = 0
    seen = set()
    while True:
        if i >= len(lines2):
            print(accumulator)
            exit()
        if i in seen:
            break
        seen.add(i)
        line = lines2[i]
        if line.startswith('acc'):
            accumulator += int(line.split()[1].replace('+', ''))
        elif line.startswith('jmp'):
            i += int(line.split()[1].replace('+', '')) - 1
        elif line.startswith('nop'):
            pass
        i += 1
