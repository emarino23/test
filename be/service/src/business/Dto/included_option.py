class IncludedOptionDto():
    def __init__(self, data):
        self.included_option_id=data.get("included_option_id") or None
        self.tour_id=data.get("tour_id") or None
        self.option_id=data.get("option_id") or None
        self.is_included=data.get("is_included") or None
        self.description=data.get("description") or None
        self.created=data.get("created") or None
        self.updated=data.get("updated") or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "included_option_id":self.included_option_id,
            "tour_id":self.tour_id,
            "option_id":self.option_id,
            "is_included":self.is_included,
            "description":self.description,
            "created":self.created,
            "updated":self.updated,
        }


class IncludedOptionListDto():
    def __init__(self, data):
        self.included_option_list = []
        for d in data:
            included_optionDto = IncludedOptionDto(d)
            self.included_option_list.append(included_optionDto)

    def __dict__(self):
        return {
            "included_option_list": self.included_option_list
        }

    def __list__(self):
        return self.included_option_list
