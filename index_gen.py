#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in modules
import os
from pprint import pprint
from random import shuffle
import sys

# 3rd-party through PyPI
import tenjin
#tenjin.set_template_encoding('utf-8')  # optional (defualt 'utf-8')
from tenjin.helpers import *
from tenjin.html import *

# local
from bibpy import bib


def main(argv=sys.argv[:]):
    if len(argv) > 1:
        layoutfn = argv[1]
    else:
        layoutfn = '_layout.pyhtml'
    filter_names = set()
    with open('index.html', 'w') as fout:
        items = []
        bib_files = os.listdir('bibtex')
        shuffle(bib_files)
        for fn in filter(lambda fn: fn.endswith('bib'), bib_files):
            parser = bib.Bibparser(bib.clear_comments(open(os.path.join('bibtex', fn), 'r').read()))
            parser.parse()
            data = parser.records.values()[0]
            # teaser image url
            data['teaser'] = 'teaser_images/%s.jpg' % os.path.splitext(fn)[0]
            data['thumb'] = 'teaser_images/thumb/%s.jpg' % os.path.splitext(fn)[0]
            # keywords
            keywords = map(lambda k: k.strip(), data.get('keywords', '').split(','))
            data['keywords'] = keywords
            filter_names.update(keywords)
            # pprint(data)
            # print '========================================================'
            items.append(data)
        engine = tenjin.Engine(path=['views'], layout=layoutfn)
        html = engine.render('items.pyhtml', {'items':items})
        fout.write(html)
    print 'Filters:'
    pprint(filter_names)
    print 'Filter #: %d' % len(filter_names)


if __name__ == '__main__':
    sys.exit(main())
