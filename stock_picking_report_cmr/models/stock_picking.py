from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    cmr_code = fields.Integer(
        string="CMR Code",
        default=0,
        help="Code needed for CMR Report",
    )
    nature_of_goods = fields.Char()
    effective_package_type = fields.Char(compute="_compute_effective_package_type")

    def _compute_effective_package_type(self):
        for picking in self:
            if hasattr(picking, "package_type"):
                picking.effective_package_type = picking.package_type
                continue
            picking.effective_package_type = picking.move_line_ids.mapped(
                "result_package_id.packaging_id.name"
            )
