"""routes module."""

from .deps import *
WSGIRequestHandler.protocol_version = "HTTP/1.1"
 

# region video
from src.business.System.EditVideo import FSEditVideo


@api.route("/System/EditVideo")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class EditVideo(Resource):
    # @secure_method
    def post(self):
        """Método para procesar opciones de inclusión
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSEditVideo(data)
# endregion



# region admin
from src.business.Admin.CreateCatalog import FSCreateCatalog


@api.route("/Admin/CreateCatalog")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class CreateCatalog(Resource):
    def post(self):
        """Método para crear catalogo
        Returns:
            json: {"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        input = request.get_json(force=True)
        res = FSCreateCatalog(input)
        return res

from src.business.Agent.Query import FSQuery


@app.route("/video.html", methods=["GET"])
def view_video():
    try:
        doc = request.args.get("doc")
        if "-" in doc:
            doc = doc.split("-")[-1]
        doc = FSQuery({
            "data": {

                "table": {
                    "name": "tour",
                    "id": doc
                }
            }
        })["data"][0]["playlist_slug"]
    except:
        doc = "PLRiOTYOXvFzaARHOdX5Q7aw70NLaIMPem"
    template = f"video.html"
    return render_template(template, doc=doc)

from src.business.Tour.FindTour import FSFindTour

@app.route("/<ext>.html", methods=["GET"])
def view_pdf(ext):
    try:
        doc = request.args.get("doc")
        if "-" in doc:
            doc = doc.split("-")[-1]
        doc = FSFindTour({
            "data": {
                "tour_id": doc
            }
        })["data"][0]["travel_code"]
    except:
        doc = "example"
    template = f"{ext}.html"
    SERVER = os.environ.get('SERVER')
    return render_template(template, doc=doc, server=SERVER)


@app.route("/gallery.html", methods=["GET"])
def view_gallery():
    doc = request.args.get("doc")
    return render_template("gallery.html", doc=doc)


@app.route("/Admin/UploadCatalog", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            input = request.get_json(force=True)
            res = FSCreateCatalog(input)
            return render_template("empty.html")

    # return render_template('upload.html')
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    """


# endregion

# region process
from src.business.System.ProcessOptions import FSProcessOptions


@api.route("/System/ProcessOptions")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class ProcessOptions(Resource):
    # @secure_method
    def post(self):
        """Método para procesar opciones de inclusión
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSProcessOptions(data)


# endregion
# region catalog
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



from src.business.Client.ClientEdit import FSClientEdit


@api.route("/Client/Edit")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class ClientEdit(Resource):
    # @secure_method
    def post(self):
        """Método para Editar un cliente
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSClientEdit(data)


# endregion
# region Tour

from src.business.Tour.PlayTour import FSPlayTour
import binascii


@api.route("/Tour/PlayTour/<doc>")
@api.param("doc", "Documento del cliente")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class PlayTour(Resource):
    def get(self, doc):
        """Método para reproducir un tour
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        headers = {"Content-Type": "text/html"}
        try:
            if "-" in doc:
                doc = doc.split("-")[-1]
            doc = FSPlayTour(doc)
        except:
            doc = "PLRiOTYOXvFzaARHOdX5Q7aw70NLaIMPem" 
        return make_response(render_template("video.html", doc=doc), 200, headers)

from src.business.Tour.FindHotel import FSFindHotel


@api.route("/Tour/FindHotel")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class FindHotel(Resource):
    # # @secure_method
    def post(self):
        """_summary_
        Returns:
            _type_: _description_
        """
        input = request.get_json(force=True)
        return FSFindHotel(input)

        
from src.business.Tour.FindCruise import FSFindCruise


@api.route("/Tour/FindCruise")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class FindCruise(Resource):
    # @secure_method
    def post(self):
        """_summary_
        Returns:
            _type_: _description_
        """
        input = request.get_json(force=True)
        return FSFindCruise(input)

        

from src.business.Tour.FindTour import FSFindTour


@api.route("/Tour/FindTour")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class FindTour(Resource):
    # @secure_method
    def post(self):
        """_summary_
        Returns:
            _type_: _description_
        """
        input = request.get_json(force=True)
        return FSFindTour(input)


from src.business.Tour.GenTour import FSGenTour


@api.route("/Tour/GenTour")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class GenTour(Resource):
    # @secure_method
    def post(self):
        """_summary_
        Returns:
            _type_: _description_
        """
        input = request.get_json(force=True)
        return FSGenTour(input)


from src.business.Tour.CalculateNetRate import FSCalculateNetRate


@api.route("/Tour/CalculateNetRate")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class CalculateNetRate(Resource):
    # @secure_method
    def post(self):
        """_summary_
        Returns:
            _type_: _description_
        """
        input = request.get_json(force=True)
        return FSCalculateNetRate(input)


from src.business.Tour.TourEdit import FSTourEdit


@api.route("/Tour/Edit")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class TourEdit(Resource):
    # @secure_method
    def post(self):
        """Método para Editar un Presupuesto
        Returns:
            json: {"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        input = request.get_json(force=True)
        res = FSTourEdit(input)
        return res


from src.business.Tour.NewTour import FSNewTour


@api.route("/Tour/NewTour")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class NewTour(Resource):
    # @secure_method
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSNewTour(data)


from src.business.Tour.NewId import FSNewId


@api.route("/Tour/NewId")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class NewId(Resource):
    # # @secure_method
    def post(self):
        # data = request.get_json(force=True)
        res = FSNewId()
        return res


from src.business.Tour.ProcessTour import FSProcessTour


@api.route("/Tour/ProcessTour")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class ProcessTour(Resource):
    # @secure_method
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSProcessTour(data)


from src.business.Tour.PromoteTour import FSPromoteTour


@api.route("/Tour/PromoteTour")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class PromoteTour(Resource):
    # @secure_method
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSPromoteTour(data)


from src.business.Tour.UpdateTour import FSUpdateTour


@api.route("/Tour/UpdateTour")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class UpdateTour(Resource):
    # @secure_method
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSUpdateTour(data)


# endregion
# region File
from src.business.File.MakeEmail import FSMakeEmail


@api.route("/Email/MakeEmail")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class MakeEmail(Resource):
    # @secure_method
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSMakeEmail(data)


from src.business.File.MakePdf import FSMakePdf


@api.route("/Email/MakePdf")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class MakePdf(Resource):
    # @secure_method
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSMakePdf(data)


from src.business.File.MakePlaylist import FSMakePlaylist


@api.route("/Email/MakePlaylist")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class MakePlaylist(Resource):
    # @secure_method
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSMakePlaylist(data)


# endregion

# region Agent
from src.business.Agent.Start import FSStart


@api.route("/Agent/Start")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class Start(Resource):
    # @encrypted
    # @secure_method
    def post(self):
        """Método para conectar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        # return FSStart(decryptdata())
        return FSStart(data)


from src.business.Agent.GetExperience import FSGetExperience


@api.route("/Agent/GetExperience")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class GetExperience(Resource):
    # @encrypted
    # @secure_method
    def post(self):
        """Método para conectar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        # return FSGetExperience(decryptdata())
        return FSGetExperience(data)


from src.business.Agent.GetDestination import FSGetDestination


@api.route("/Agent/GetDestination")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class GetDestination(Resource):
    # @encrypted
    # @secure_method
    def post(self):
        """Método para conectar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        # return FSGetDestination(decryptdata())
        return FSGetDestination(data)


from src.business.Agent.Query import FSQuery


@api.route("/Agent/Query")
@api.doc(
    body=resource_fields,
    responses={
        400: "Error: BAD REQUEST",
        200: '{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}',
    },
)
class Query(Resource):
    # @encrypted
    # @secure_method
    def post(self):
        """Método para conectar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        # return FSQuery(decryptdata())
        return FSQuery(data)


# endregion6
