import json
import ast
import json
from naver_core import *


class DestinationDto(object):
    def __init__(self, data):
        self.explorationDay = data.get("explorationDay") or None
        self.arrival_hour = data.get("arrival_hour") or None
        self.key_activities = data.get("key_activities") or None
        self.travel_rhythm = data.get("travel_rhythm") or None
        self.type = data.get("type") or None
        self.index = data["index"]
        self.destination = data.get("destination") or None
        self.daysData = json.dumps(
            prepareJsonData(data.get("daysData"))) or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "explorationDay": self.explorationDay,
            "arrival_hour": self.arrival_hour,
            "key_activities": self.key_activities,
            "travel_rhythm": self.travel_rhythm,
            "type": self.type,
            "index": self.index,
            "destination": self.destination,
            "daysData": self.daysData,
        }


class DestinationListDto(object):
    def __init__(self, data, id):
        self.destination_list = []
        for d in data:
            destinationDto = None
            destinationDto = DestinationDto(d)
            self.destination_list.append(destinationDto.__dict__)

    def __dict__(self):
        return self.destination_list

    def __list__(self):
        return self.destination_list
