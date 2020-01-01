import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    @classmethod
    def publish_offer(cls, trips_list):
        list_of_errors = []
        for trip in trips_list:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append('<{}>:{}'.format(trip.symbol, e))
            except Exception as e:
                list_of_errors.append('<{}>:{}'.format(trip.symbol, e))
        if len(list_of_errors)>0:
            raise Exception('The list of trips has errors: {}'.format(i for i in list_of_errors))
        else:
            print('the offer will be published...')

    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
    ]
try:
    Trip.publish_offer(trips)
except Exception as e:
    print('THERE ARE ERRORS')
    print(e)
    print('The offer cannot be published')