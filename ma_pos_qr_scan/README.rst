=========================
 QR Code Scanning in POS
=========================

Scans QR codes via device's camera.

Usage
=====

To subscribe to scanning event use following code in js::

    var core = require('web.core');
    core.bus.on('qr_scanned', this, function(value){
        // your handler here
    })


Credits
=======

Contributors
------------
* `Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>`__

Sponsors
--------
* `Sinomate <http://sinomate.net/>`__

Maintainers
-----------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__


