class NetRateDto():
    def __init__(self, data):
        self.net_rate_id=data.get("net_rate_id") or None
        self.created=data.get("created") or None
        self.updated=data.get("updated") or None
        self.final_detail=data.get("final_detail") or None
        self.tour_id=data.get("tour_id") or None
        self.description=data.get("description") or None
        self.has_approbed=data.get("has_approbed") or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "net_rate_id":self.net_rate_id,
            "created":self.created,
            "updated":self.updated,
            "final_detail":self.final_detail,
            "tour_id":self.tour_id,
            "description":self.description,
            "has_approbed":self.has_approbed,
        }


class NetRateListDto():
    def __init__(self, data):
        self.net_rate_list = []
        for d in data:
            net_rateDto = NetRateDto(d)
            self.net_rate_list.append(net_rateDto)

    def __dict__(self):
        return {
            "net_rate_list": self.net_rate_list
        }

    def __list__(self):
        return self.net_rate_list
