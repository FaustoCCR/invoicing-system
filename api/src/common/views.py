from apiflask.views import MethodView

class ItemView(MethodView):
  # init_every_request = False
  def _get_item(self, id: int):
    return self