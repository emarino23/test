"""routes module.""" 

from .core import app,RecoveryForm, api, resource_fields, Resource, request, reqparse, make_response, render_template

from src.business.Mascota.GetMascota import FSGetMascota


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
    
from src.business.Mascota.CreateMascota import FSCreateMascota

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

from src.business.System.FindCatalog import FSFindCatalog


@api.route("/System/FindCatalog")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class FindCatalog(Resource):
    # # @secure_method
    def post(self):
        """Método para mostrar catálogos
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        res = FSFindCatalog(data)
        return res
    def get(self):
        """Método para mostrar catálogos
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        res = FSFindCatalog("")
        return res

# endregion
# region user

from src.business.User.Forgot import FSForgot


@api.route("/User/Forgot")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class Forgot(Resource):
    # @secure_method
    def post(self):
        """Método para recuperar contraseña Backend

        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        form = RecoveryForm(request.form)
        if form.validate():
            parser = reqparse.RequestParser()
            parser.add_argument("confirmation")
            data = parser.parse_args()
            input = {
                "password": request.form["password"],
                "confirmation": data["confirmation"],
            }
            FSForgot(input)
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("success.html"), 200, headers)

    def get(self):
        """Método para recuperar contraseña Frontend

        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        # data = request.get_json(force=True)
        form = RecoveryForm(request.form)
        parser = reqparse.RequestParser()
        parser.add_argument("confirmation")
        confirmation = request.args.get("confirmation")
        headers = {"Content-Type": "text/html"}
        return make_response(
            render_template("recovery.html", form=form, data=confirmation), 200, headers
        )


from src.business.User.Confirm import FSConfirm


@api.route("/User/Confirm")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class Confirm(Resource):
    def get(self):
        """Método para Confirmar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        parser = reqparse.RequestParser()
        parser.add_argument("confirmation")
        data = parser.parse_args()
        return FSConfirm(data)


from src.business.User.Connect import FSConnect


@api.route("/User/Connect")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class Connect(Resource):
    def head(self):
        """Método Inicial para conectar un usuario
        Returns:
            header: {"state":True/False, "data":salt}
        """
        # res = FSConnect(None)
        return True, 200, {"token": "gAAAAABhjtSOlFafpsgJ70Sx11gM7Iv_6RuTpnOs1UWf4ELEnYC1gsvx7E2OZjRAUkkflPMXqR7ua7MtC7Y3LCWoB8uo5lmBV-Sns1lIpIy0YPuPXhdPx96We9xqbRcEylp8Fz91PAQf"}
    def options(self):
        """Método Inicial para conectar un usuario
        Returns:
            header: {"state":True/False, "data":salt}
        """
        # res = FSConnect(None)
        return True, 200

    # @encrypted
    # # @secure_method
    def post(self):
        """Método para conectar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        try:
            data = request.get_json(force=True)
            # return FSConnect(decryptdata())
            return FSConnect(data)
        except Exception as e:
            print(e)
            return ErrorResponse(e)


from src.business.User.Logout import FSLogout


@api.route("/User/Logout")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class Logout(Resource):
    # @secure_method
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSLogout(data)


# endregion
# region Client
