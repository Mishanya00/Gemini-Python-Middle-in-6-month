from datetime import date, timedelta


class DateRange:
    def __init__(self, start: str, end: str):
        self.start = date.fromisoformat(start)
        self.end = date.fromisoformat(end)
        self.curr = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr <= self.end:
            current = self.curr
            self.curr += timedelta(days=1)
            return current
        raise StopIteration


a = DateRange('2026-01-01', '2026-03-01')

for el in a:
    print(el)

