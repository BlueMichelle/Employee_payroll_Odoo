# Módulo `employee_payroll` – Gestión de Nóminas y Declaraciones de la Renta

## 1. Descripción

Este módulo de Odoo 17 implementa la gestión de **nóminas de empleados** y sus **declaraciones de la renta anuales**, cumpliendo los requisitos de la práctica:

- Gestión de nóminas con:
  - Empleado
  - Sueldo base
  - Lista de bonificaciones y deducciones
  - IRPF (%) configurable
  - IRPF pagado (€) calculado automáticamente sobre *sueldo base + bonificaciones* (sin deducciones)
  - Fecha de la nómina
  - Justificante de transferencia en PDF
  - Estado de la nómina: *Redactada*, *Confirmada* o *Pagada*
- Gestión de bonificaciones/deducciones:
  - Nómina a la que pertenecen
  - Importe bruto
  - Concepto
- Declaración de la renta anual por empleado:
  - Año
  - Empleado
  - Máximo 14 nóminas del mismo año natural
  - Sueldo bruto total (automático)
  - Impuestos pagados por IRPF (automático)

El módulo utiliza vistas con listas, pestañas y barra de estado para que la información sea visualmente accesible.

---

## 2. Modelos principales

### 2.1. Modelo de Nómina (`employee.payroll`)

Campos principales:

- `employee_id`: empleado al que corresponde la nómina (`hr.employee`).
- `date`: fecha de la nómina.
- `base_salary`: sueldo base (monetario).
- `line_ids`: líneas de bonificaciones/deducciones (One2many a `employee.payroll.line`).
- `irpf_percent`: porcentaje de IRPF (%).
- `irpf_amount`: IRPF pagado (€), calculado automáticamente.
- `gross_bonus_total`: suma de bonificaciones.
- `gross_deduction_total`: suma de deducciones.
- `gross_salary`: sueldo bruto = sueldo base + bonificaciones - deducciones.
- `pdf_transfer`: justificante de transferencia en PDF (binario).
- `pdf_filename`: nombre del archivo PDF.
- `state`: estado de la nómina (`draft`, `confirmed`, `paid`) con barra de estado.

Lógica clave:

- El IRPF se calcula como:  
  **(sueldo base + bonificaciones) × IRPF% / 100**  
  Sin tener en cuenta las deducciones, tal y como pide la práctica.
- Acciones:
  - `action_confirm()`: pasa la nómina de *Redactada* a *Confirmada* (solo si el sueldo base > 0).
  - `action_set_paid()`: pasa la nómina de *Confirmada* a *Pagada*.

Restricciones:

- El sueldo base no puede ser negativo.
- El IRPF solo puede estar entre 0 y 100%.
- No se puede confirmar una nómina con sueldo base 0.
- No se puede marcar como pagada una nómina que no esté confirmada.

---

### 2.2. Modelo de Línea de Nómina (`employee.payroll.line`)

Representa una **bonificación** o **deducción**.

Campos:

- `payroll_id`: nómina a la que pertenece.
- `line_type`: tipo de línea (`bonus` = bonificación, `deduction` = deducción).
- `amount`: importe bruto (monetario).
- `concept`: concepto de la bonificación/deducción.
- `currency_id`: moneda relacionada con la nómina.

Restricciones:

- El importe no puede ser negativo.

---

### 2.3. Modelo de Declaración de la Renta (`employee.tax.declaration`)

Campos principales:

- `year`: año de la declaración.
- `employee_id`: empleado al que pertenece.
- `payroll_ids`: nóminas incluidas (Many2many a `employee.payroll`).
- `total_gross_salary`: sueldo bruto total (suma de `gross_salary` de las nóminas).
- `total_irpf_paid`: IRPF total pagado (suma de `irpf_amount` de las nóminas).
- `currency_id`: moneda.

Restricciones importantes:

- Máximo **14** nóminas por declaración.
- Todas las nóminas deben:
  - Pertenecer al **mismo empleado** que la declaración.
  - Tener fecha informada.
  - Pertenecer al **mismo año** que la declaración (`payroll.date.year == year`).

---

## 3. Vistas y menús

### 3.1. Nóminas

- Menú:  
  `Recursos Humanos -> Nóminas -> Nóminas`.

Vistas:

- **Lista (list)**:
  - Muestra: empleado, fecha, sueldo base, sueldo bruto, IRPF %, IRPF pagado y estado.
  - Decoraciones visuales según el estado (confirmada/pagada).
- **Formulario**:
  - Barra de estado (`statusbar`) para el campo `state`.
  - Pestañas:
    - *Bonificaciones / Deducciones*: lista de líneas de nómina.
    - *IRPF*: IRPF % y cantidad de IRPF pagada.
    - *Totales*: totales de bonificaciones, deducciones y sueldo bruto.
    - *Justificante*: subida del PDF con la transferencia bancaria.

### 3.2. Declaraciones de la renta

- Menú:  
  `Recursos Humanos -> Nóminas -> Declaraciones de la renta`.

Vistas:

- **Lista (list)**:
  - Año, empleado, sueldo bruto total e IRPF total pagado.
- **Formulario**:
  - Campos de año y empleado.
  - Totales de sueldo bruto e IRPF.
  - Pestaña con las nóminas (`payroll_ids`) filtradas por el empleado de la declaración.

---

## 4. Seguridad y permisos

Archivo: `security/ir.model.access.csv`

- Concede permisos a usuarios internos (`base.group_user`) para:
  - Leer/crear/modificar nóminas.
  - Leer líneas de nómina.
  - Leer/crear/modificar declaraciones de la renta.

---

## 5. Instalación del módulo

### 5.1. Copiar el módulo

Colocar la carpeta `employee_payroll` dentro de `addons/` de tu instalación de Odoo (en este caso, en el directorio `addons` del proyecto Docker).

Estructura mínima:

- `employee_payroll/__init__.py`
- `employee_payroll/__manifest__.py`
- `employee_payroll/models/__init__.py`
- `employee_payroll/models/payroll.py`
- `employee_payroll/models/tax_declaration.py`
- `employee_payroll/views/payroll_views.xml`
- `employee_payroll/views/tax_declaration_views.xml`
- `employee_payroll/security/ir.model.access.csv`

### 5.2. Reiniciar Odoo y actualizar Apps

Con Docker:

```bash path=null start=null
docker-compose restart odoo
