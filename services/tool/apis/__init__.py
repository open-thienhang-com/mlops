from packages.adapters.http import TestAPI
from .model1 import ns_model as model1
from .model2 import ns_model as model2

api_v1 = TestAPI(
    api_name="api",
    pre_path="/api/v1",
    doc_path="/ui",
    doc_title="TestBOOK",
    doc_version="1.0",
    doc_description="No thing here",
    license_url="thienhang"
)

api_v1.add_custom_namespace(model1)
api_v1.add_namespace(model2)
