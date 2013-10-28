#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4:


__version__ = '0.3'


# system modules
import os
from random import shuffle
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 3rd-party modules
from bibpy import bib
from PIL import Image
from staticjinja import Renderer


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
                data['teaser-size'] = Image.open(data['teaser']).size
                # thumb image url
                data['thumb'] = 'teaser_images/thumb/%s.jpg' % os.path.splitext(fn)[0]
                data['thumb-size'] = Image.open(data['thumb']).size
                # author list
                try:
                    data['authors'] = ", ".join(["%s %s" % (a['given'], a['family']) for a in data['author']])
                except KeyError:
                    print 'No author:', data['title']
                    data['authors'] = ''
                try:
                    data['website']
                except KeyError:
                    print 'No website:', data['title']
                ooxx.append(data)
            works.append(ooxx)
    return {
            'row_size':12/n,
            'works':works,
            'version':__version__,
            }


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
