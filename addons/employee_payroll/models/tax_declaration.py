from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TaxDeclaration(models.Model):
    _name = "employee.tax.declaration"
    _description = "Declaración de la Renta Anual"

    year = fields.Integer(
        string="Año",
        required=True,
    )
    employee_id = fields.Many2one(
        "hr.employee",
        string="Empleado",
        required=True,
    )
    payroll_ids = fields.Many2many(
        "employee.payroll",
        string="Nóminas",
        help="Máximo 14 nóminas, todas del mismo año natural y del mismo empleado.",
    )

    total_gross_salary = fields.Monetary(
        string="Sueldo bruto total",
        compute="_compute_totals",
        store=True,
    )
    total_irpf_paid = fields.Monetary(
        string="IRPF total pagado",
        compute="_compute_totals",
        store=True,
    )
    currency_id = fields.Many2one(
        "res.currency",
        string="Moneda",
        required=True,
        default=lambda self: self.env.company.currency_id.id,
    )

    @api.depends("payroll_ids", "payroll_ids.gross_salary", "payroll_ids.irpf_amount")
    def _compute_totals(self):
        for rec in self:
            rec.total_gross_salary = sum(rec.payroll_ids.mapped("gross_salary"))
            rec.total_irpf_paid = sum(rec.payroll_ids.mapped("irpf_amount"))

    @api.constrains("payroll_ids", "year", "employee_id")
    def _check_payrolls(self):
        for rec in self:
            if len(rec.payroll_ids) > 14:
                raise ValidationError("Una declaración de la renta solo puede tener un máximo de 14 nóminas.")

            for payroll in rec.payroll_ids:
                if payroll.employee_id != rec.employee_id:
                    raise ValidationError(
                        "Todas las nóminas de la declaración deben pertenecer al mismo empleado."
                    )
                if not payroll.date:
                    raise ValidationError("Todas las nóminas deben tener fecha.")
                if payroll.date.year != rec.year:
                    raise ValidationError(
                        "Todas las nóminas deben pertenecer al mismo año natural que la declaración."
                    )
