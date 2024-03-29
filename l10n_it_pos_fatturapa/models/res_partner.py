# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create_from_ui(self, partner):
        if "electronic_invoice_subjected" in partner:
            electronic_invoice_subjected = bool(
                partner.get("electronic_invoice_subjected", False)
            )

            partner.update(
                {
                    "electronic_invoice_subjected": electronic_invoice_subjected,
                    "electronic_invoice_obliged_subject": electronic_invoice_subjected,
                }
            )
        return super(ResPartner, self).create_from_ui(partner)
