#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

def FetchCitiBikeData():
  '''Fetches data from CitiBike's JSON endpoint.'''
  u = 'http://www.citibikenyc.com/stations/json'
  r = requests.get(u)
  return r.json()

def ExtractStationData(data, id):
  '''Extracts station data from CitiBike dictionary.'''
  out = {
    'time': data['executionTime'],
    'data': None
  }

  for station in data['stationBeanList']:
    if station['id'] == id:
      out['data'] = station
      return out

