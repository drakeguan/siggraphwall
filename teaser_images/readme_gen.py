#!/usr/bin/env python

import os
import sys

def main(argv=sys.argv[:]):
    markdown = '![%s](%s)\n'
    with open('README.md', 'w') as fout:
        for imgname in filter(lambda f: f.endswith('.jpg'), os.listdir('.')):
            print imgname
            fout.write(markdown % (imgname, imgname))
    return 0


if __name__ == '__main__':
    sys.exit(main())
