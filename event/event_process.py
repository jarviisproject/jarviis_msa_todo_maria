from datetime import datetime

from icecream import ic


class ScheduleTimeCheck(object):

    def __init__(self):
        pass

    # def create_date(self):
    #     start_time = '2021-11-30T09:51:25.830000+09:00'
    #     d_start = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%f+09:00')

    def start(self, start):
        # start_time = 'date_check'
        start_date = datetime.strptime(start, '%Y-%m-%d %H:%M')
        start_year = start_date.year
        start_month = start_date.month
        start_date = start_date.day

    def end(self, end):
        # end_time = '2021-11-25 12:00'
        end_date = datetime.strptime(end, '%Y-%m-%d %H:%M')
        end_year = end_date.year
        end_month = end_date.month
        end_day = end_date.day

    def date_check(self, start, end):

        start_date = datetime.strptime(start, '%Y-%m-%d %H:%M')
        end_date = datetime.strptime(end, '%Y-%m-%d %H:%M')
        start_month = start_date.month
        start_day = start_date.day
        end_month = end_date.month
        end_day = end_date.day
        month_compare = end_month - start_month
        day_compare = end_day - start_day
        ic(month_compare, day_compare)
        # year_period =
        [i for i in range(start_day, end_day+1)]




if __name__ == '__main__':
    sc = ScheduleTimeCheck()
    # sc.start()
    # sc.end()
    sc.date_check('2021-11-25 12:00', '2021-11-28 18:00')