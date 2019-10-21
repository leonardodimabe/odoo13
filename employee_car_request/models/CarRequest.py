from odoo import models, fields, api

class CarRequest(models.Model):
    _name = "car.request" # table in db => car_request
    _description = "Car Request"

    name = fields.Char(string="Request", required = True)
    date_from = fields.Datetime(string="Starting Date",required= False, default= fields.Datetime.now()) 
    date_to = fields.Datetime(string="End Date",required= False) 
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True)
    car_id = fields.Many2one(comodel_name='fleet.vehicle', string="Car", require=True)

    