class TourDetailDto():
    def __init__(self, data):
        self.tour_id= data.get("tour_id") or None
        self.created= data.get("created") or None
        self.updated= data.get("updated") or None
        self.detail= data.get("detail") or None
        self.tour_detail_id= data.get("tour_detail_id") or None
        self.destination_id= data.get("destination_id") or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "tour_id":self.tour_id,
            "created":self.created,
            "updated":self.updated,
            "detail":self.detail,
            "tour_detail_id":self.tour_detail_id,
            "destination_id":self.destination_id,
        }


class TourDetailListDto():
    def __init__(self, data, id):
        self.tour_detail_list = []
        for d in data:
            tour_detailDto = TourDetailDto(d) 
            tour_detailDto.tour_detail_id = id
            self.tour_detail_list.append(tour_detailDto)

    def __dict__(self):
        return {
            "tour_detail_list": self.tour_detail_list
        }

    def __list__(self):
        return self.tour_detail_list
