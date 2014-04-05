# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# system modules
import difflib
from functools import partial
import os
from pprint import pprint
import re

# 3rd-party modules
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
from scrapy.exceptions import DropItem


class KesenPipeline(object):
    def __init__(self):
        self.files = os.listdir("../bibtex/siggraph2013")
        self.RATIO = 0.9

    def process_item(self, item, spider):
        basename = '_'.join([w.lower() for w in re.findall(r"[\w'-]+", item['title'])]) + '.bib'
        junk = partial(difflib.IS_CHARACTER_JUNK, ws="-_:\"' ,.")
        key = lambda i: i[1]
        # likely_file = (basename, similarity 0~1)
        likely_file = max([(f, difflib.SequenceMatcher(junk, basename, f).ratio()) for f in self.files], key=key)
        if likely_file[1] > self.RATIO:
            with open(os.path.join('..', 'bibtex', 'siggraph2013', likely_file[0])) as fin:
                bib = BibTexParser(fin, customization=convert_to_unicode)
                data = bib.get_entry_list()[0]
                try:
                    data['website'] = item['url']
                except KeyError:
                    print(data['title'], 'No url')
                else:
                    pprint(data)
            return item
        else:
            raise DropItem("No corresponding .bib for %s." % item['title'])

