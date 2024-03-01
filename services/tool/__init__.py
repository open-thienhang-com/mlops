from packages.adapters.http import TestHttpService
# from .apis import api_v1
from .views import views

class BaseService:
    def __init__(self):
        service = TestHttpService()
        # service.add_api(api_v1.get_api())
        service.add_ui(views.get_api())
        # service.add_api(api_v2.get_api())
        service.run()