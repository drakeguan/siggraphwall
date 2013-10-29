#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set hls is ai et sw=4 sts=4 ts=8 nu ft=python:
#
# Copyright © 2013 drake <drake.guan@gmail.com>
#
# Distributed under terms of the MIT license.

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector 

from kesen.items import KesenItem

class KesenSpider(BaseSpider):
    name = 'kesen'
    allowed_domains = ['kesen.realtimerendering.com']
    start_urls = ['http://kesen.realtimerendering.com/sig2013.html']

    def parse(self, response):
        """

        sample:
            <dt><B>User-Assisted Image Compositing for Photographic Lighting</B>
            <a href="http://www.cs.cornell.edu/projects/light_compositing/"><img alt="Paper Abstract" src="Abstract.png" border="0"></a>
            <a href="http://www.cs.cornell.edu/projects/light_compositing/"><img alt="Author Preprint" src="Preprint.png" border="0"></a>
            <a href="https://vimeo.com/64976852"><img alt="Paper Video" src="Video.png" border="0"></a>
            </dt>
        """
        x = HtmlXPathSelector(response)
        items = []
        for dt in x.select('//dt'):
            item = KesenItem()
            try:
                item['title'] = dt.select(".//b/text()").extract()[0]
            except:
                continue
            try:
                item['url'] = dt.select(".//a[1]/@href").extract()[0]
            except IndexError:
                pass
            items.append(item)
        return items
