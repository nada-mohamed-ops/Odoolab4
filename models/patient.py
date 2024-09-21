from odoo import models, fields, api

class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient Information'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date()
    cr_ratio = fields.Float()
    blood_type = fields.Selection(
        [('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
         ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')],
        string='Blood Type'
    )
    pcr = fields.Boolean(default=False)
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer(compute='_compute_age', store=True)
    state = fields.Selection(
        [('undetermined', 'Undetermined'), ('good', 'Good'),
         ('fair', 'Fair'), ('serious', 'Serious')],
        default='undetermined'
    )
    department_id = fields.Many2one('hms.department', string="Department")
    doctor_ids = fields.Many2many('hms.doctor', string="Doctors")  # Ensure this line is present

    @api.depends('birth_date')
    def _compute_age(self):
        for patient in self:
            if patient.birth_date:
                patient.age = (fields.Date.today() - patient.birth_date).days // 365

    def action_set_undetermined(self):
        self.state = 'undetermined'
