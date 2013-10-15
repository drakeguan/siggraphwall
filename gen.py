#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4:

import os
from random import shuffle
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from staticjinja import Renderer

# local
from bibpy import bib


def get_works(n=3):
    works = []
    for root, dirs, files in os.walk('bibtex'):
        files2 = list(filter(lambda fn: fn.endswith('bib'), files))
        shuffle(files2)
        for chunks in [files2[i:i+n] for i in range(0, len(files2), n)]:
            ooxx = []
            for fn in chunks:
                parser = bib.Bibparser(bib.clear_comments(open(os.path.join(root, fn), 'r').read()))
                parser.parse()
                data = parser.records.values()[0]
                # teaser image url
                data['teaser'] = 'teaser_images/%s.jpg' % os.path.splitext(fn)[0]
                data['thumb'] = 'teaser_images/thumb/%s.jpg' % os.path.splitext(fn)[0]
                ooxx.append(data)
            works.append(ooxx)
    return {'row_size':12/n,
            'works': works}


def main(argv=sys.argv[:]):
    template_folder = os.path.join(os.getcwd(), 'templates')
    renderer = Renderer(
            template_folder=template_folder,
            contexts=[
                ('index.html', get_works),
                ])
    renderer.run(debug=True, use_reloader=False)
    return 0

if __name__ == "__main__":
    sys.exit(main())
