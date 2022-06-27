# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Trial_report(models.Model):
    _name = 'trial_report.input'
    _description = 'trial_report_input'
    _rec_name = 'employee_id'

    emp_name = fields.Char()
    
    employee_id = fields.Many2one('hr.employee.public', 'Employees', default=lambda self:self.env['hr.employee.public'].search([('user_id','=',self.env.uid)]).id, readonly=True)
    work_phone = fields.Char(related="employee_id.work_phone", string='Work phone')
    grade_id = fields.Char(related='employee_id.job_title',string='Position')
    manager_id = fields.Many2one(related='employee_id.parent_id', string='Manager')
    coach_id = fields.Many2one(related='employee_id.coach_id', string='Coach')
    department_id = fields.Many2one(related='employee_id.department_id', string='Department')
    birthday = fields.Date(related='employee_id.user_id.birthday')
    probationary_start_day = fields.Date(string="Probationary start day")
    probationary_end_day = fields.Date(string="Probationary end day")
    assigned_work = fields.Text('Assigned work')
    work_content = fields.Many2many('trial_report.work_content')
    difficulties = fields.Text('Difficulties')
    suggest_support = fields.Text('Suggest support')
    mentors_comments = fields.Text("Mentor's comments")
    manager_comments = fields.Text("Manager's comments")
    hr_comments = fields.Text("HR's comments")
    company_comments = fields.Text("Company's comments")
    
    @api.constrains('probationary_start_day', 'probationary_end_day')
    def _check_valid(self):
        for r in self:
            if r.probationary_start_day and r.probationary_end_day:
                if r.probationary_start_day > r.probationary_end_day:
                    raise ValidationError("The probationary start day must be before the probationary end day")
            
            
         

    
class Work_content(models.Model):
    _name = 'trial_report.work_content'
    _description = 'trial_report_work_content'
    _rec_name = 'week'
    
    week = fields.Integer('Week',required = True)
    from_date = fields.Date('From date')
    end_date = fields.Date('End date', compute='compute_date')
    content = fields.Text('Work_content' ,required = True)
    status = fields.Selection(selection=[('completed', 'Completed'),
                                        ('studying', 'Studying')])
    note = fields.Text('Note')
    created_by = fields.Char(compute='compute_emp')
    
    @api.depends('from_date')
    def compute_date(self):
        for r in self:
            if r.from_date:
                r.end_date = fields.Date.add(r.from_date,days=7)
            else:
                r.end_date = ""
    
    
    @api.depends()
    def compute_emp(self):
        for r in self:
            print(r.create_uid.id)
            r.created_by = r.env['hr.employee.public'].search([('user_id','=',r.create_uid.id)]).name
         
        
    sql_constraints = [('week_unique', 'unique(week)', "Week be unique!")]

