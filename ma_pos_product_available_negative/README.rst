.. image:: https://img.shields.io/badge/license-LGPL--3-blue.png
   :target: https://www.gnu.org/licenses/lgpl
   :alt: License: LGPL-3

==================================
 Restrict out-of-stock POS Orders
==================================

The module depends on the pos_pin module. Before POS order validation the module checks whether the order contains
products with no positive quantity. If it does then a cashier gets popup to select users. A sale is take place
if the selected user has group which is specified in the POS config parameter "Negative Order Group". Otherwise
the sale is rejected.

Credits
=======

Contributors
------------
* `Stanislav Krotov <https://it-projects.info/team/ufaks>`__

Sponsors
--------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__

Maintainers
-----------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__

      To get a guaranteed support
      you are kindly requested to purchase the module
      at `odoo apps store <https://apps.odoo.com/apps/modules/12.0/pos_product_available_negative/>`__.

      Thank you for understanding!

      * `Mediterranean Apps <mediterranean.apps@gmail.com>`__


