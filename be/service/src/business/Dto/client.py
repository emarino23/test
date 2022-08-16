class ClientDto():
    def __init__(self, data):

        self.client_id = data.get("client_id") or None
        self.created = data.get("created") or None
        self.updated = data.get("updated") or None
        self.contact_name = data.get("contact_name") or None
        self.legal_client_type_id = data.get("legal_client_type_id") or None
        self.client_type_id = data.get("client_type_id") or None
        self.client_dni = data.get("client_dni") or None
        self.is_owner = data.get("is_owner") or None
        self.contact_name_2 = data.get("contact_name_2") or None
        self.email = data.get("email") or None
        self.origin_id = data.get("origin_id") or None
        self.phone = data.get("phone") or None
        self.address = data.get("address") or None
        self.description = data.get("description") or None
        self.brith_date = data.get("brith_date") or None

    def __dict__(self):
        return {

            "client_id": self.client_id,
            "created": self.created,
            "updated": self.updated,
            "contact_name": self.contact_name,
            "legal_client_type_id": self.legal_client_type_id,
            "client_type_id": self.client_type_id,
            "client_dni": self.client_dni,
            "is_owner": self.is_owner,
            "contact_name_2": self.contact_name_2,
            "email": self.email,
            "origin_id": self.origin_id,
            "phone": self.phone,
            "address": self.address,
            "description": self.description,
            "brith_date": self.brith_date,
        }
