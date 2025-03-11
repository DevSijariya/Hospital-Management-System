from odoo import models,fields

class HealthCenterBuldings(models.Model):
    _name="healthcenter.building"
    name=fields.Char("Name",required=True)
    institute=fields.Char("institute",required=True)


class HealthCenterUnit(models.Model):
    _name="healthcenter.unit"
    name=fields.Char("Name",required=True)
    institution=fields.Many2one('healthcenter.building')

class HealthCenterwards(models.Model):
    _name="healthcenter.ward"
    name=fields.Char("Name",required=True)
    number_bed=fields.Integer("Numbers of Beds",required=True)
    gender=fields.Selection([('Male','Male'),('Female','Female'),('unisex','Unisex')],required=True)
    instituion=fields.Many2one('healthcenter.building',required=True)
    status=fields.Selection([('available','Available'),('unavailable','Unavailable')],required=True)


class HospitalOperatingRoom(models.Model):
    _name="hospitaloperating.room"
    name=fields.Char("Name",required=True)
    institution=fields.Many2one('healthcenter.building',string="Institution",required=True)
    units=fields.Many2one('healthcenter.unit',string="Units",required=True)

# Operational Areas

class OperationAreas(models.Model):
    _name="operational.areas"
    name=fields.Char("Operational Areas",required=True)

class OperationalSectors(models.Model):
    _name="operational.sectors"
    name=fields.Char("Name",required=True)
    area=fields.Many2one('operational.areas',string="Operational Area",required=True)