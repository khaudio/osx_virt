#!/usr/bin/env python

import sys


filename = sys.argv[1]
ovmf_code = f'{sys.argv[2]}/OVMF_CODE.fd'
ovmf_vars = f'{sys.argv[2]}/OVMF_VARS.fd'


def replace(line, keyword, path, opts=''):
    if f'<{keyword}' in line and opts in line:
        head = ' '.join((keyword, opts)) if opts else keyword
        return f'<{head}>{path}</{keyword}>'


print(f'Opening {filename}...')
lines, omitNext = [], False
with open(filename, 'r') as xml:
    for line in xml:
        if omitNext and "<qemu:arg value=" in line:
            omitNext = False
        elif "<qemu:arg value='-object'/>" in line:
            omitNext = True
        else:
            lines.append(line)
    lines.append('</domain>')

with open(filename, 'w') as xml:
    for line in lines:
        line = replace(
                line, 'loader', ovmf_code,
                "readonly='yes' type='pflash'"
            )
        line = replace(line, 'nvram', ovmf_vars)
        line = replace(line, 'name', 'Hackintosh')
        xml.write(line)
