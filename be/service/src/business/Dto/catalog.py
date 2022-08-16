class CatalogDto():
    def __init__(self, data):

        self.catalog_id = data.get("catalog_id") or None
        self.description = data.get("description") or None
        self.created = data.get("created") or None
        self.updated = data.get("updated") or None

    def __dict__(self):
        return {

            "catalog_id":self.catalog_id,
            "description":self.description,
            "created":self.created,
            "updated":self.updated,
        }
