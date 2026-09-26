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

    # accept button - marks this application as accepted and
    # moves the gig to "In Progress" since someone is now working on it
    def action_accept(self):
        for application in self:
            application.status = 'accepted'
            application.gig_id.state = 'in_progress'

    # reject button - just marks this application as rejected
    def action_reject(self):
        for application in self:
            application.status = 'rejected'