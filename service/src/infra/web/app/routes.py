"""routes module."""

from .core import app, api, resource_fields, Resource, request

from src.business.Mascota.GetMascota import FSGetMascota


@api.route("/Mascota/GetMascota")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class Todo(Resource):
    def get(self):
        id = request.args.get("id")

        res = FSGetMascota(id)
        return res
# endregion
