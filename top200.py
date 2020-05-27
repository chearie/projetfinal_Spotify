# coding : utf-8

from fycharts.SpotifyCharts import SpotifyCharts
api = SpotifyCharts()

api.top200Daily(output_file= "top_200_daily.csv", start= "2017-01-01", end= "2017-02-22", region= ["global"])
api.top200Daily(output_file= "top_200_daily.csv", start= "2017-02-24", end= "2017-05-29", region= ["global"])
api.top200Daily(output_file= "top_200_daily.csv", start= "2017-06-01", end= "2017-06-01", region= ["global"])
api.top200Daily(output_file= "top_200_daily.csv", start= "2017-06-03", end= "2019-12-31", region= ["global"])

print(api)