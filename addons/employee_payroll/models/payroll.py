from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Payroll(models.Model):
    _name = "employee.payroll"
    _description = "Nómina de Empleado"

    employee_id = fields.Many2one(
        "hr.employee",
        string="Empleado",
        required=True,
    )
    date = fields.Date(
        string="Fecha",
        required=True,
        default=fields.Date.context_today,
    )
    base_salary = fields.Monetary(
        string="Sueldo base",
        required=True,
    )
    currency_id = fields.Many2one(
        "res.currency",
        string="Moneda",
        required=True,
        default=lambda self: self.env.company.currency_id.id,
    )

    line_ids = fields.One2many(
        "employee.payroll.line",
        "payroll_id",
        string="Bonificaciones y Deducciones",
    )

    irpf_percent = fields.Float(
        string="IRPF (%)",
        required=True,
        default=15.0,
        help="Porcentaje de IRPF aplicado sobre sueldo base + bonificaciones (sin deducciones).",
    )
    irpf_amount = fields.Monetary(
        string="IRPF pagado",
        compute="_compute_irpf_amount",
        store=True,
    )

    gross_bonus_total = fields.Monetary(
        string="Total bonificaciones",
        compute="_compute_totals",
        store=True,
    )
    gross_deduction_total = fields.Monetary(
        string="Total deducciones",
        compute="_compute_totals",
        store=True,
    )
    gross_salary = fields.Monetary(
        string="Sueldo bruto",
        compute="_compute_totals",
        store=True,
        help="Sueldo base + bonificaciones - deducciones.",
    )

    pdf_transfer = fields.Binary(
        string="Justificante de transferencia (PDF)",
        attachment=True,
    )
    pdf_filename = fields.Char(string="Nombre del PDF")

    state = fields.Selection(
        [
            ("draft", "Redactada"),
            ("confirmed", "Confirmada"),
            ("paid", "Pagada"),
        ],
        string="Estado",
        default="draft",
        tracking=True,
    )

    @api.depends("base_salary", "line_ids.amount", "line_ids.line_type")
    def _compute_totals(self):
        for rec in self:
            bonus = sum(
                rec.line_ids.filtered(lambda l: l.line_type == "bonus").mapped("amount")
            )
            deduction = sum(
                rec.line_ids.filtered(lambda l: l.line_type == "deduction").mapped("amount")
            )
            rec.gross_bonus_total = bonus
            rec.gross_deduction_total = deduction
            rec.gross_salary = rec.base_salary + bonus - deduction

    @api.depends("base_salary", "line_ids.amount", "line_ids.line_type", "irpf_percent")
    def _compute_irpf_amount(self):
        for rec in self:
            bonus = sum(
                rec.line_ids.filtered(lambda l: l.line_type == "bonus").mapped("amount")
            )
            taxable_base = rec.base_salary + bonus
            rec.irpf_amount = taxable_base * (rec.irpf_percent / 100.0)

    @api.constrains("base_salary", "irpf_percent")
    def _check_values(self):
        for rec in self:
            if rec.base_salary < 0:
                raise ValidationError("El sueldo base no puede ser negativo.")
            if rec.irpf_percent < 0 or rec.irpf_percent > 100:
                raise ValidationError("El IRPF debe estar entre 0 y 100%.")

    def action_confirm(self):
        for rec in self:
            if rec.state != "draft":
                continue
            if rec.base_salary <= 0:
                raise ValidationError("La nómina debe tener un sueldo base mayor que 0 para confirmarse.")
            rec.state = "confirmed"

    def action_set_paid(self):
        for rec in self:
            if rec.state != "confirmed":
                raise ValidationError("Solo las nóminas confirmadas se pueden marcar como pagadas.")
            rec.state = "paid"


class PayrollLine(models.Model):
    _name = "employee.payroll.line"
    _description = "Línea de Nómina (Bonificación / Deducción)"

    payroll_id = fields.Many2one(
        "employee.payroll",
        string="Nómina",
        required=True,
        ondelete="cascade",
    )
    line_type = fields.Selection(
        [
            ("bonus", "Bonificación"),
            ("deduction", "Deducción"),
        ],
        string="Tipo",
        required=True,
        default="bonus",
    )
    amount = fields.Monetary(
        string="Importe bruto",
        required=True,
    )
    currency_id = fields.Many2one(
        "res.currency",
        related="payroll_id.currency_id",
        store=True,
        readonly=True,
    )
    concept = fields.Char(
        string="Concepto",
        required=True,
    )

    @api.constrains("amount")
    def _check_amount(self):
        for rec in self:
            if rec.amount < 0:
                raise ValidationError("El importe de una bonificación/deducción no puede ser negativo.")
