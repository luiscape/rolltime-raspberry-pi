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
schedule.every(30).seconds.do(Main)

def Main(verbose=True):
  '''Wrapper to run all the scheduled tasks.'''

  if verbose:
    print '%s Running scheduler.' % item('prompt_bullet')

  try:
    while True:
      schedule.run_pending()
      time.sleep(1)

  except Exception as e:
    print e
    return False


if __name__ == '__main__':
  Main()
