"""core module."""
 
from .deps import *


dotenv_path = Path(ENV_PATH)
load_dotenv(dotenv_path=dotenv_path)
app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.url_map.strict_slashes = False
api = Api(app, doc=False)
config = NaverConfig(app)
pksalt = config.core.myVariables["PKSALT"]
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# cors = CORS(app)
db = SQLAlchemy()
resource_fields = api.model('Resource', {
    'data': fields.Raw,
})
