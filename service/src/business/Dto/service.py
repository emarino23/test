class ServiceDto():
    def __init__(self, data):
        self.service_id = data.get("service_id") or None
        self.created = data.get("created") or None
        self.updated = data.get("updated") or None
        self.me = data.get("me") or None
        self.open_days = data.get("open_days") or None
        self.close_time = data.get("close_time") or None
        self.open_time = data.get("open_time") or None
        self.cost = data.get("cost") or None
        self.selling_price = data.get("selling_price") or None
        self.name = data.get("name") or None
        self.description = data.get("description") or None
        self.duration = data.get("duration") or None
        self.age_friendly_range_id = data.get("age_friendly_range_id") or None
        self.child_frendly = data.get("child_frendly") or None
        self.infant_friendly = data.get("infant_friendly") or None
        self.observation = data.get("observation") or None
        self.max_capacity = data.get("max_capacity") or None
        self.pet_friendly = data.get("pet_friendly") or None
        self.props = data.get("props") or None
        self.supplier_id = data.get("supplier_id") or None
        self.destination_id = data.get("destination_id") or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "service_id": self.service_id,
            "created": self.created,
            "updated": self.updated,
            "me": self.me,
            "open_days": self.open_days,
            "close_time": self.close_time,
            "open_time": self.open_time,
            "cost": self.cost,
            "selling_price": self.selling_price,
            "name": self.name,
            "description": self.description,
            "duration": self.duration,
            "age_friendly_range_id": self.age_friendly_range_id,
            "child_frendly": self.child_frendly,
            "infant_friendly": self.infant_friendly,
            "observation": self.observation,
            "max_capacity": self.max_capacity,
            "pet_friendly": self.pet_friendly,
            "props": self.props,
            "supplier_id": self.supplier_id,
            "destination_id": self.destination_id,
        }


class ServiceListDto():
    def __init__(self, data):
        self.service_list = []
        for d in data:
            serviceDto = ServiceDto(d)
            self.service_list.append(serviceDto)

    def __dict__(self):
        return {
            "service_list": self.service_list
        }

    def __list__(self):
        return self.service_list
