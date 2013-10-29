# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import re

class KesenPipeline(object):
    def process_item(self, item, spider):
        basename = '_'.join([w.lower() for w in re.findall(r"[\w'-]+", item['title'])]) + '.bib'
        filename = os.path.join('..', 'bibtex', 'siggraph2013', basename)
        print os.path.exists(filename), filename
        return item

