import requests
# Run below command in Terminal to install REQUESTS package with pip before running 'python main.py' command
# python3 -m pip install requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json",
)

last_twenty_years = response.json()[1][:20] # get first 2o records from reponse json

for year in last_twenty_years:
  if not year["value"]:
    continue
  display_width = year["value"] // 10_000_000 # underscore keep number readable friendly
  print(f"{year['date']}: {year['value']}", display_width * "=") # it gives date of year and its value

