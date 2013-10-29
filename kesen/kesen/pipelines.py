# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# system modules
import os
from pprint import pprint
import re

# 3rd-party modules
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode


class KesenPipeline(object):
    def process_item(self, item, spider):
        basename = '_'.join([w.lower() for w in re.findall(r"[\w'-]+", item['title'])]) + '.bib'
        filename = os.path.join('..', 'bibtex', 'siggraph2013', basename)
        # print os.path.exists(filename), filename
        try:
            with open(filename, 'r') as fin:
                bib = BibTexParser(fin, customization=convert_to_unicode)
                data = bib.get_entry_list()[0]
                try:
                    data['website'] = item['url']
                except KeyError:
                    print('No url')
                pprint(data)
        except IOError:
            pass
        return item

