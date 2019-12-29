/*  
    License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html). */
odoo.define('pos_orders_history_reprint.tour', function(require) {
    "use strict";

    var tour = require('web_tour.tour');
    var HistoryTour = require('pos_orders_history.tour');

    function reprint_order() {
        return [{
            trigger: '.button.reprint',
            content: "reprint selected order",
        }];
    }

    var hist_tour = new HistoryTour();
    var steps = [].concat(
        hist_tour.open_pos_steps(),
        hist_tour.create_order_steps(),
        hist_tour.orders_history(),
        reprint_order(),
        hist_tour.close_pos()
    );

    tour.register('pos_orders_history_reprint_tour', {test: true, url: '/web' }, steps);
});
