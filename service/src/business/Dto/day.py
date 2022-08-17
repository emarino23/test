import json


class DayDto():
    def __init__(self, data):
        self.date = data.get('date') or None
        self.day_description = data.get('day_description') or None
        self.day_name = data.get('day_name') or None
        self.destination = data.get('destination') or None
        self.key_activities = data.get('key_activities') or None
        self.tour_detail_id = data.get('tour_detail_id') or None
        self.meals = data.get('meals') or None
        self.observation = data.get('observation') or None
        self.option_id = data.get('option_id') or None
        self.parent = data.get('parent') or None
        self.transport_id = data.get('transport_id') or None
        self.experiences = json.dumps(data.get('experiences')) or None

    def set(self, key, value):
        """Setter

        Args:
            key (str): Key
            value (Any): Value
        """
        setattr(self, key, value)

    def __dict__(self):
        return {
            "date": self.date,
            "day_description": self.day_description,
            "day_name": self.day_name,
            "destination": self.destination,
            "key_activities": self.key_activities,
            "tour_detail_id": self.tour_detail_id,
            "meals": self.meals,
            "observation": self.observation,
            "option_id": self.option_id,
            "parent": self.parent,
            "transport_id": self.transport_id,
            "experiences": self.experiences,

        }


class DayListDto():
    def __init__(self, data):
        self.day_list = []
        for d in data:
            dayDto = DayDto(d)
            self.day_list.append(dayDto)

    def __dict__(self):
        return {
            "day_list": self.day_list
        }

    def __list__(self):
        return self.day_list
