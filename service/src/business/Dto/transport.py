class TransportDto():
    def __init__(self, data):
        self.transport_id = data.get("transport_id") or None
        self.transport_range_id = data.get("transport_range_id") or None
        self.transport_service_id = data.get("transport_service_id") or None
        self.rate = data.get("rate") or None
        self.created = data.get("created") or None
        self.updated = data.get("updated") or None
        self.description = data.get("description") or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "transport_id": self.transport_id,
            "transport_range_id": self.transport_range_id,
            "transport_service_id": self.transport_service_id,
            "rate": self.rate,
            "created": self.created,
            "updated": self.updated,
            "description": self.description,
        }


class TransportListDto():
    def __init__(self, data):
        self.transport_list = []
        for d in data:
            transportDto = TransportDto(d)
            self.transport_list.append(transportDto)

    def __dict__(self):
        return {
            "transport_list": self.transport_list
        }

    def __list__(self):
        return self.transport_list
