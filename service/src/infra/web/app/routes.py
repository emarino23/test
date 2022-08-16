"""routes module."""

from .core import app, api, resource_fields, Resource, request

from src.business.Mascota.GetMascota import FSGetMascota
from src.business.Mascota.CreateMascota import FSCreateMascota


@api.route("/Mascota/GetMascota")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class GetMascota(Resource):
    def get(self):
        id = request.args.get("id")

        res = FSGetMascota(id)
        return res
    

@api.route("/Mascota/CreateMascota")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class CreateMascota(Resource):
    def post(self):
        """Método para mostrar catálogos
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        input = request.get_json(force=True)
        res = FSCreateMascota(input)
        return res
# endregion
