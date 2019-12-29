=====================
 POS restaurant base
=====================

Technical module in POS.

The standard ``Printer`` class in ``pos_restaurant/static/src/js/multiprint.js`` does not allow you to override the functions of this class.
This module duplicates the ``Printer`` class and allows you to redefine it.

Also, here were redefined the ``computeChanges``, ``printChanges``, ``hasChangesToPrint``, ``build_line_resume`` functions from ``Order`` class and ``set_dirty`` function from ``Orderline`` class to improve speed and were added new functions such as ``print_order_receipt``, ``get_line_resume`` for speed improvement of load POS.

In the ``orderline_change`` function of the ``OrderWidget`` class, the orderline rendering was moved to a separate function to optimize the orderline rendering speed in the order after sending this orderline to the kitchen.

Usage
=====

Example of using for the Printer class

Connection::

    var Printer = require('pos_restaurant.base');

Using::

    Printer.include({
        print: function(receipt){
            // your code
            // call super method this._super(receipt);
        }

Credits
=======

Contributors
------------
* Dinar Gabbasov <gabbasov@it-projects.info>

Sponsors
--------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__

Maintainers
-----------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__

