#!/usr/bin/python
import urllib2, os, sys, re

sinapi = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=china&top_time=%s&top_show_num=100&top_order=ASC&js_var=news_'
transcode = re.compile(r'\\/')

for datestr in sys.stdin:
    datestr = datestr.strip()
    m = urllib2.urlopen(sinapi % datestr)
    tmpstr = m.readlines()[0]
    tmpstr = tmpstr[tmpstr.index('{'):tmpstr.rindex('}')+1]
    tmphash = eval('''%s''' % tmpstr)
    for tmpele in tmphash['data']:
        m = transcode.sub('/', tmpele['url'])
        print >>sys.stdout, '\t'.join([m, tmpele['top_time']])



