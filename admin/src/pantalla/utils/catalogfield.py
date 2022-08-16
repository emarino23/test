from django.db import models
from django.utils.translation import gettext_lazy as _
def CatalogField(name, Master, Detail):
    try:
        catalogs = Master.objects.values_list(
            'catalog_id', 'description').filter(description=name)
        # print(name)
        # print(catalog)
        # print(catalog[0][0])
        choices = list()
        if len(catalogs) > 0:
            catalog_id = catalogs[0][0]
            details = Detail.to_list(Detail)
            if len(details) > 0:
                for detail in details:
                    if detail[1] == catalog_id and detail[5]:
                        choices.append((detail[2],
                                        _(detail[3])))
                tuple_choices = (*choices,)
                return tuple_choices
        return tuple(choices)
    except Exception as e:
        print(e)
        pass
class TestField(models.BigIntegerField):
    pass


def MasterCatalogField(Master):
    try:
        choices = list()
        catalogs = Master.objects.values_list(
            'catalog_id', 'description')
        for catalog in catalogs:
            choices.append((catalog[0],
                            _(catalog[1])))
        tuple_choices = (*choices,)
        return tuple_choices 
    except Exception as e:
        print(e)
        pass