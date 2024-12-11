{
    "name": "POS Container Deposit",
    "version": "16.0.1.0.0",
    "category": "Point of Sale",
    "summary": "This module is used to manage container deposits for products"
    " in Point of Sale.",
    "author": "Sunflower IT, Open2bizz, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/pos",
    "license": "AGPL-3",
    "depends": ["point_of_sale"],
    "data": ["views/product_view.xml"],
    "assets": {
        "web.assets_backend": ["/pos_deposit/static/src/js/pos.js"],
        "web.assets_qweb": ["/pos_deposit/static/src/xml/pos.xml"],
    },
    "installable": True,
}
