from odoo import models, fields

class GigApplication(models.Model):
    _name = 'gig.application'
    _description = 'Gig Application'

    gig_id = fields.Many2one('gig.posting', string='Gig', required=True)
    applicant_id = fields.Many2one('res.partner', string='Applicant', required=True)
    message = fields.Text(string='Message')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], string='Status', default='pending')