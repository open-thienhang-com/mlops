from packages.adapters.http import TestAPI
from .index import ns_model as model1

views = TestAPI(
    api_name="api",
    pre_path="/api/v1",
    doc_path="/ui",
    doc_title="thienhang",
    doc_version="1.0",
    doc_description="No thing here",
    license_url="thienhang"
)

views.add_custom_namespace(model1)
