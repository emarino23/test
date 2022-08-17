class ExperienceDto():
    def __init__(self, data):
        self.experience_id = data.get("experience_id") or None
        self.destination_id = data.get("destination_id") or None
        self.created = data.get("created") or None
        self.updated = data.get("updated") or None
        self.key_activity_id = data.get("key_activity_id") or None
        self.budget_id = data.get("budget_id") or None
        self.delimiter_id = data.get("delimiter_id") or None
        self.travel_ritm_id = data.get("travel_ritm_id") or None
        self.experience_title = data.get("experience_title") or None
        self.experience_photo = data.get("experience_photo") or None
        self.description = data.get("description") or None
        self.experience_previous = data.get("experience_previous") or None
        self.experience_next = data.get("experience_next") or None
        self.detail = data.get("detail") or None
        self.destination_option_id = data.get("destination_option_id") or None
        self.key_activity2_id = data.get("key_activity2_id") or None
        self.supplier_id = data.get("supplier_id") or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "experience_id": self.experience_id,
            "destination_id": self.destination_id,
            "created": self.created,
            "updated": self.updated,
            "key_activity_id": self.key_activity_id,
            "budget_id": self.budget_id,
            "delimiter_id": self.delimiter_id,
            "travel_ritm_id": self.travel_ritm_id,
            "experience_title": self.experience_title,
            "experience_photo": self.experience_photo,
            "description": self.description,
            "experience_previous": self.experience_previous,
            "experience_next": self.experience_next,
            "detail": self.detail,
            "destination_option_id": self.destination_option_id,
            "key_activity2_id": self.key_activity2_id,
            "supplier_id": self.supplier_id,
        }


class ExperienceListDto():
    def __init__(self, data):
        self.experience_list = []
        for d in data:
            experienceDto = ExperienceDto(d)
            self.experience_list.append(experienceDto)

    def __dict__(self):
        return {
            "experience_list": self.experience_list
        }

    def __list__(self):
        return self.experience_list
