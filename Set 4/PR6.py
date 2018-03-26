import daily
from weekly import weekly_forecast
print("\nToday's weather:")
print(daily.daily_forecast(),'\n')
forecast = weekly_forecast()
print('\nWeekly Forecast:')
for day in forecast:
    print('{}: {}'.format(day,forecast[day]))