# import pyowm
#
# owm = pyowm.OWM('a4d8a1f64517055225e7a8f89fd8c9b5')  # You MUST provide a valid API key

from pyowm.owm import OWM
owm = OWM('a4d8a1f64517055225e7a8f89fd8c9b5')
mgr = owm.weather_manager()
weather = mgr.weather_at_place('Uong Bi, VN').weather
temp_dict_kelvin = weather.temperature()   # a dict in Kelvin units (default when no temperature units provided)
print(temp_dict_kelvin['temp_min'])
temp_dict_kelvin['temp_max']
temp_dict_fahrenheit = weather.temperature('fahrenheit')  # a dict in Fahrenheit units
temp_dict_celsius = weather.temperature('celsius')  # guess?
print(temp_dict_celsius)
observation = mgr.weather_at_place('Uong Bi, VN')
wind_dict_in_meters_per_sec = observation.weather.wind()   # Default unit: 'meters_sec'
print(wind_dict_in_meters_per_sec)
weather = observation.weather
print(weather.detailed_status)