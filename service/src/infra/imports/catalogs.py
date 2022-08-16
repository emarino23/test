"""catalogs module."""
import os
import json
import pandas as pd
import requests
from naver_core import *
any_module(__file__, 3)
from src.infra.web.app.routes import app

IMPORT_DIR = os.path.dirname(__file__)
INFRA_DIR = os.path.dirname(IMPORT_DIR)
SRC_DIR = os.path.dirname(INFRA_DIR)
ROOT_DIR = os.path.dirname(SRC_DIR)
CERT_FILE = os.path.join(ROOT_DIR, ("ca_bundle.cert"))


def upload_catalogs(**kwargs):
    """_summary_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """
    server = os.environ.get("SERVER")
    catalogs = get_catalogs(**kwargs)
    relation = kwargs.get("relation") or '{}'
    update = kwargs.get("update") or False
    print(catalogs[0])
    for catalog in catalogs:
        try:
            data = {}
            data = {"data": catalog, "relation": relation, "update": update}
            res = requests.post(
                url=f"{server}/Admin/CreateCatalog", data=json.dumps(data)
            )
            print(res.json())
        except Exception as error:
            print(error)
            raise error


def get_catalogs(**kwargs):
    """_summary_

    Returns:
        _type_: _description_
    """
    cid = kwargs.get("cid")
    tags = kwargs.get("tags")
    rows = get_rows(**kwargs)
    catalogs = []
    i = 1
    for row in rows:
        tag = get_tag(row, tags)
        catalog = {
            "catalog_id": cid,
            "order": 0,
            "description": f"{tag}",
            "is_active": True,
            "code": i,
            "value": row,
        }
        catalogs.append(catalog)
        i += 1
    return catalogs


def get_rows(**kwargs):
    """_summary_

    Returns:
        _type_: _description_
    """
    data = load_file(**kwargs)
    rows = []
    for col, values in data.items():
        dto = {}
        dto[col] = None
        for row, value in values.items():
            if len(rows) <= row:
                rows.append({})
            dto[col] = value
            rows[row] = {**rows[row], **dto}
    return rows


def load_file(**kwargs):
    """
    load_file Function
    ~~~~~~~~~~~~~~~~~~~~~

    Requests is an HTTP library, written in Python, for human beings.
    Basic usage:

    """
    filename = kwargs.get("filename")
    page = kwargs.get("page")
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    rows_xlsx = pd.ExcelFile(file_path, engine="openpyxl")
    data = rows_xlsx.parse(rows_xlsx.sheet_names[page]).to_dict()
    return data


def get_tag(row, tags):
    """_summary_

    Args:
        row (_type_): _description_
        tags (_type_): _description_

    Returns:
        _type_: _description_
    """
    res = ""
    for tag in tags:
        res += row.get(tag) 
    return res


if __name__ == "__main__":
    upload_catalogs(
        filename="countries.xlsx",
        page=0,
        cid=56,
        tags=["name"],
        relation={ 
        },
        update=False

    )
