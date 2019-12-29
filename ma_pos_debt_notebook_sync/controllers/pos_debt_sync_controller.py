# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import odoo
from odoo.http import request


try:
    from odoo.addons.bus.controllers.main import BusController
except ImportError:
    BusController = object


class Controller(BusController):
    @odoo.http.route('/pos_order_test/update', type="json", auth="public")
    def order_test_update(self, message):
        channel_name = "pos.order_test"
        res = request.env["pos.config"]._send_to_channel(channel_name, message)
        return res
