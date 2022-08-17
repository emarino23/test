class SupplierDto():
    def __init__(self, data):
        self.supplier_id=data.get("supplier_id") or None
        self.created=data.get("created") or None
        self.updated=data.get("updated") or None
        self.supplier_type_id=data.get("supplier_type_id") or None
        self.supplier_rule_id=data.get("supplier_rule_id") or None
        self.props=data.get("props") or None
        self.tax_id=data.get("tax_id") or None
        self.legal_name=data.get("legal_name") or None
        self.city_id=data.get("city_id") or None
        self.commercial_name=data.get("commercial_name") or None
        self.contact_name=data.get("contact_name") or None
        self.website=data.get("website") or None
        self.payment_type_id=data.get("payment_type_id") or None
        self.credit_days=data.get("credit_days") or None
        self.finance_email=data.get("finance_email") or None
        self.commercial_email=data.get("commercial_email") or None
        self.finance_phone=data.get("finance_phone") or None
        self.commercial_phone=data.get("commercial_phone") or None
        self.sector=data.get("sector") or None
        self.principal_street=data.get("principal_street") or None
        self.secondary_street=data.get("secondary_street") or None
        self.building_number=data.get("building_number") or None
        self.lat=data.get("lat") or None
        self.long=data.get("long") or None
        self.description=data.get("description") or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
        "supplier_id":self.supplier_id,
        "created":self.created,
        "updated":self.updated,
        "supplier_type_id":self.supplier_type_id,
        "supplier_rule_id":self.supplier_rule_id,
        "props":self.props,
        "tax_id":self.tax_id,
        "legal_name":self.legal_name,
        "city_id":self.city_id,
        "commercial_name":self.commercial_name,
        "contact_name":self.contact_name,
        "website":self.website,
        "payment_type_id":self.payment_type_id,
        "credit_days":self.credit_days,
        "finance_email":self.finance_email,
        "commercial_email":self.commercial_email,
        "finance_phone":self.finance_phone,
        "commercial_phone":self.commercial_phone,
        "sector":self.sector,
        "principal_street":self.principal_street,
        "secondary_street":self.secondary_street,
        "building_number":self.building_number,
        "lat":self.lat,
        "long":self.long,
        "description":self.description,
        }


class SupplierListDto():
    def __init__(self, data):
        self.supplier_list = []
        for d in data:
            supplierDto = SupplierDto(d)
            self.supplier_list.append(supplierDto)

    def __dict__(self):
        return {
            "supplier_list": self.supplier_list
        }

    def __list__(self):
        return self.supplier_list
