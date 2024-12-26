from dateutil.relativedelta import relativedelta
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class MyCompanyVehicle(models.Model):
    """
    MyCompanyVehicle Model
    This model represents a vehicle owned by the company. It includes fields for the vehicle's name, license plate, fuel type, mileage, last service date, and owner. It also includes computed fields and onchange methods to handle business logic.
    Fields:
        - name (Char): The name of the vehicle.
        - license_plate (Char): The license plate of the vehicle.
        - fuel_type (Selection): The type of fuel the vehicle uses (Diesel, Gasoline, Electric).
        - mileage (Float): The mileage of the vehicle.
        - last_service_date (Date): The date of the last service.
        - needs_service (Boolean): Indicates if the vehicle needs service, computed based on mileage and last service date.
        - partner_id (Many2one): The owner of the vehicle, linked to res.partner.
    Methods:
        - _compute_needs_service: Computes if the vehicle needs service based on mileage and last service date.
        - _onchange_fuel_type: Resets mileage to 0 if the fuel type is electric.
        - create: Validates that the license plate is unique before creating a new record.
    Note:
        It is recommended to use @api.constrains for validations instead of the create method.
    """
    _name = 'my.company.vehicle'
    _description = 'My Company Vehicle'
    
    name = fields.Char(string='Name')
    license_plate = fields.Char(string='License Plate')
    fuel_type = fields.Selection([
            ('diesel', 'Diesel'), 
            ('gasoline', 'Gasoline'), 
            ('electric', 'Electric')
        ], 
        string='Fuel Type'
    )
    mileage = fields.Float(string='Mileage')
    last_service_date = fields.Date(string='Last Service Date')
    needs_service = fields.Boolean(string='Needs Service', compute='_compute_needs_service', store=True)
    partner_id = fields.Many2one('res.partner', string='Owner')

    @api.depends('mileage', 'last_service_date')
    def _compute_needs_service(self):
        for record in self:
            record.needs_service = record.mileage > 20000 or (record.last_service_date and record.last_service_date < fields.Date.today() - relativedelta(months=6))

    @api.onchange('fuel_type')
    def _onchange_fuel_type(self):
        if self.fuel_type == 'electric':
            self.mileage = 0.0

    # Validation example using @api.constrains method to verify license plate uniqueness
    # @api.constrains('license_plate')
    # def _check_license_plate(self):
    #     search_result = self.search_count([('license_plate', '=', self.license_plate)])
    #     if search_result:
    #         raise ValidationError(_('License plate already exists'))

    @api.model
    def create(self, vals):
        search_result = self.search_count([('license_plate', '=', vals.get('license_plate'))])
        if search_result:
            raise ValidationError(_('License plate already exists'))
        return super(MyCompanyVehicle, self).create(vals)
