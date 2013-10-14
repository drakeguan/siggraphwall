#!/usr/bin/env python

# built-in
import os
from pprint import pprint
import sys

# 3rd party by pip

# local
from bibpy import bib


def main(argv=sys.argv[:]):
    # example = 'bibtex/robust_inside-outside_segmentation_using_generalized_winding_numbers.bib'
    example = argv[1]
    data = bib.clear_comments(open(example, 'r').read())
    parser = bib.Bibparser(data)
    parser.parse()
    data = parser.json()
    #pprint(data)
    pprint(parser.records)
    return 0


if __name__ == '__main__':
    sys.exit(main())
