from sense_hat import SenseHat
from app.pixels import GeneratePixels
from app.fetch import FetchCitiBikeData, ExtractStationData

def Main():
  '''Wrapper.'''

  #
  # Collect data.
  #
  data = FetchCitiBikeData()
  station = ExtractStationData(data=data,id=445)

  #
  # Generate pixels.
  #
  pixels = GeneratePixels(station['data']['availableBikes'])

  #
  # Send to SenseHAT.
  #
  sense = SenseHat()
  sense.set_pixels(pixels)

#
# Starting schedule.
#
schedule.every(1).minute.do(Main)
