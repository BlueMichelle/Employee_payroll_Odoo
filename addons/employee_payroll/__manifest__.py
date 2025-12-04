{
    "name": "Employee Payroll",
    "summary": "Gestión de nóminas y declaraciones de renta anuales",
    "version": "1.0",
    "author": "Tu Nombre",
    "category": "Human Resources",
    "depends": ["base", "hr"],  # usamos hr.employee para los empleados
    "data": [
        "security/ir.model.access.csv",
        "views/payroll_views.xml",
        "views/tax_declaration_views.xml",
    ],
    "application": True,
}
