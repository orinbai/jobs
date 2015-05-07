import time, datetime

class DateTrans:
    def __init__(self, timefmt='%Y-%m-%d', outputfmt='%Y-%m-%d'):
        self.timefmt = timefmt
        self.outfmt = outputfmt

    def str2posix(self, timestr):
        ''' Timestr Fmt: YYYY-mm-dd '''
        return time.mktime(time.strptime('%s' % timestr,self.timefmt))

    def daterange(self, bgtime, period):
        return [time.strftime('%s' % self.outfmt, time.localtime(self.str2posix(bgtime)+i*86400)) for i in range(period)]

    def dateCount(self, stime, etime):
        a = time.strptime(stime, '%s' % self.timefmt)
        b = time.strptime(etime, '%s' % self.timefmt)
        return (datetime.datetime(*b[:3]) - datetime.datetime(*a[:3])).days
