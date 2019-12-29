# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl.html).

import odoo.tests
from odoo.api import Environment


@odoo.tests.common.at_install(True)
@odoo.tests.common.post_install(True)
class TestUi(odoo.tests.HttpCase):

    def test_pos_scan_ref(self):
        cr = self.registry.cursor()
        env = Environment(cr, self.uid, {})
        env['ir.module.module'].search([('name', '=', 'pos_scan_ref')], limit=1).state = 'installed'
        env['product.template'].search([('name', '=', "Boni Oranges")], limit=1).write({
            'default_code': '1234567890333',
        })
        cr.release()
        # without a delay there might be problems on the steps whilst opening a POS
        # caused by a not yet loaded button's action
        self.phantom_js("/web",
                        "odoo.__DEBUG__.services['web_tour.tour'].run('tour_pos_scan_ref', 1000)",
                        "odoo.__DEBUG__.services['web_tour.tour'].tours.tour_pos_scan_ref.ready",
                        login="admin", timeout=140)
