#!/user/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from xml.dom import minidom

def getMinerals():
	ret = []
	page = urllib2.urlopen('http://www.ceve-market.org/api/evemon')  
	xmlStr = page.read()
	document = minidom.parseString(xmlStr)
	root = document.documentElement
	for x in root.childNodes:
		i = {}
		i["name"] = x.getElementsByTagName("name")[0].childNodes[0].nodeValue
		i["price"] = x.getElementsByTagName("price")[0].childNodes[0].nodeValue
		ret.append(i)
	return ret
