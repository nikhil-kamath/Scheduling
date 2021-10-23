import datetime as dt

def main() -> None:
    today = (dt.date.today())
    tomorrow = dt.date.today() + dt.timedelta(days=1)
    print(tomorrow)
    print(tomorrow.weekday())
    print(today < today)

if __name__ == "__main__":
    main()