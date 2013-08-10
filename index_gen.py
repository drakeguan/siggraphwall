#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in modules
import os
from pprint import pprint
import sys

# 3rd-party through PyPI
import tenjin
#tenjin.set_template_encoding('utf-8')  # optional (defualt 'utf-8')
from tenjin.helpers import *
from tenjin.html import *

# local
from bibpy import bib


def main(argv=sys.argv[:]):
    with open('index.html', 'w') as fout:
        items = []
        for fn in filter(lambda fn: fn.endswith('bib'), os.listdir('bibtex')):
            parser = bib.Bibparser(bib.clear_comments(open(os.path.join('bibtex', fn), 'r').read()))
            parser.parse()
            data = parser.records.values()[0]
            data['teaser'] = 'teaser_images/%s.jpg' % os.path.splitext(fn)[0]
            pprint(data)
            print '========================================================'
            items.append(data)
        engine = tenjin.Engine(path=['views'], layout='_layout.pyhtml')
        html = engine.render('items.pyhtml', {'items':items})
        fout.write(html)


if __name__ == '__main__':
    sys.exit(main())
