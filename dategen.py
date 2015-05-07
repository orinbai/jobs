import urllib2, timetrans
sinapi = 'http://top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=china&top_time=%s&top_show_num=100&top_order=ASC&js_var=news_'

t = timetrans.DateTrans(outputfmt='%Y%m%d')
datenum = t.dateCount('2012-11-1', '2015-04-20')
dateArray = t.daterange('2012-11-1', datenum)
print '\n'.join(dateArray)
