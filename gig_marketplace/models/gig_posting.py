from odoo import models, fields

class GigPosting(models.Model):
    _name = 'gig.posting'
    _description = 'Student Gig Posting'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    poster_id = fields.Many2one('res.partner', string='Posted By')
    category = fields.Char(string='Category')
    budget = fields.Float(string='Budget')
    deadline = fields.Date(string='Deadline')
    state = fields.Selection([
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='open')