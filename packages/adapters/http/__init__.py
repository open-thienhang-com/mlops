from packages.adapters.base import Config, Service
from packages.glog import logger
from flask import Blueprint
from flask import Flask
from flask_restx import Api, Namespace, Resource
from flask import request
from http import HTTPStatus


class Resource(Resource):
    def __init__(self) -> None:
        super().__init__()


class TestHttpConfig(Config):
    def __init__(self, host: str = "0.0.0.0", port: int = 8000, processes: int = 1, threaded: bool = True):
        super().__init__(host, port)
        self._processes = processes
        self._threaded = threaded


class TestHttpRespone(object):
    def __init__(self, status: HTTPStatus = HTTPStatus.OK, raw_data: any = None, extra_data: any = None):
        self.status = status
        self.data = raw_data
        self.extra = extra_data


class TestNamespace(Namespace):
    def __init__(self, ** kwargs) -> None:
        super().__init__(**kwargs)
        self.logger = logger


class TestAPI():
    def __init__(self,
                 api_name: str = "api",
                 pre_path: str = "/api/v1",
                 doc_path: str = "/ui",
                 doc_title: str = "TestBOOK 🎐",
                 doc_version: str = "1.0",
                 doc_description="",
                 license_url=""):

        self.apis = Blueprint(api_name,
                              __name__,
                              url_prefix=pre_path
                              )

        self._api = Api(
            self.apis,
            doc=doc_path,
            title=doc_title,
            version=doc_version,
            description=doc_description,
            license_url=license_url,
        )

    def add_custom_namespace(self, new_api: Namespace = None):
        self._api.add_namespace(new_api)

    def add_namespace(self, new_api: TestNamespace = None):
        self._api.add_namespace(new_api)

    def get_api(self):
        return self.apis

class TestHttpService(Service):
    def __init__(self, config: TestHttpConfig = TestHttpConfig()):
        super().__init__(config)
        self._config = config
        _app = Flask(__name__)
        self._app = _app

    def add_api(self, new_blueprint):
        self._app.register_blueprint(new_blueprint)

    def add_ui(self, new_blueprint):
        self._app.register_blueprint(new_blueprint)

    def run(self):
        self._app.run(
            host=self._config._host,
            port=self._config._port,
            processes=self._config._processes,
            threaded=self._config._threaded
        )


def response_with_json(status, data, extra):
    if status == 200:
        resp = {
            'error': False,
            'message': "success",
            'data':    data,
            'extra':   extra
        }
    else:
        resp = {
            'error': True,
            'message': "error",
            'data':   data,
            'extra':   extra
        }
    return resp, status
