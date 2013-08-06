#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def inject(fout):
    fout.write('<ul id="Grid">\n')
    for fn in filter(lambda fn: fn.endswith('bib'), os.listdir('bibtex')):
        name = os.path.basename(fn)[:-4]
        fout.write('<li class="mix"><img src="teaser_images/%s.jpg" /></li>\n' % name)
    fout.write('</ul>\n')


def main(argv=sys.argv[:]):
    with open('index.html', 'w') as fout:
        for line in open('index_template.html', 'r'):
            if '<!-- teaser_images_anchor -->' in line:
                inject(fout)
            else:
                fout.write(line)
    return 0

if __name__ == '__main__':
    sys.exit(main())
