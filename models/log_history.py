from odoo import models, fields, api

class LogHistoryWizard(models.TransientModel):
    _name = 'log.history.wizard'
    _description = 'Log History Wizard'

    patient_id = fields.Many2one('hms.patient', string='Patient', required=True)
    description = fields.Text(string='Description', required=True)

    def action_save(self):

        log_entry = self.env['log.history'].create({
            'patient_id': self.patient_id.id,
            'description': self.description,
        })
        return {'type': 'ir.actions.act_window_close'}
