from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    vehicle_count = fields.Integer(string='Vehicle Count', compute='_compute_vehicle_count')

    def _compute_vehicle_count(self):
        for record in self:
            record.vehicle_count = self.env['my.company.vehicle'].search_count([('partner_id', '=', record.id)])
