class DayDetailDto():
    def __init__(self, data):
        self.day_detail_id = data.get("day_detail_id") or None
        self.service_id = data.get("service_id") or None
        self.experience_id = data.get("experience_id") or None
        self.created = data.get("created") or None
        self.updated = data.get("updated") or None
        self.day_id = data.get("day_id") or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "day_detail_id":self.day_detail_id,
            "service_id":self.service_id,
            "experience_id":self.experience_id,
            "created":self.created,
            "updated":self.updated,
            "day_id":self.day_id,
        }


class DayDetailListDto():
    def __init__(self, data):
        self.day_detail_list = []
        for d in data:
            dayDetailDto = DayDetailDto(d) 
            self.day_detail_list.append(dayDetailDto)

    def __dict__(self):
        return {
            "day_detail_list": self.day_detail_list
        }

    def __list__(self):
        return self.day_detail_list
