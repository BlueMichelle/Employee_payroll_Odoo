# Tarea 9 – Guía rápida y README del proyecto

Este README resume la Tarea 9 y apunta a la guía detallada en `docs/Tarea9_Guia.md`.

## Qué incluye
- Módulo `addons/mi_modulo` con:
  - Modelo `modelo_de_ejemplo`
  - Vistas: lista (editable="bottom") y formulario con `oe_title`, `separator`, `group`
  - Acción `action_modelo_de_ejemplo`
  - Menús: `Ejemplos` → `Registros`
  - Seguridad: ACL para `base.group_user` (lectura), grupos `Officer`/`Administrator`
- Documentación:
  - Guía completa: `docs/Tarea9_Guia.md`
  - README del módulo: `addons/mi_modulo/README.md`

## Cómo probar
1. Levanta servicios: `docker-compose up -d`
2. En Odoo:
   - Apps → Update Apps List → Update
   - Busca "Módulo de Ejemplo" → Instalar/Actualizar
3. Navega: Ejemplos → Registros
   - Crea un registro en línea (fila al pie)
   - Abre el formulario y revisa cabecera/separator/group

## Capturas y vídeo
- Sigue los pasos y placeholders descritos en `docs/Tarea9_Guia.md`

## Subida a GitHub
- Sube este módulo al repo `BlueMichelle/M-dulos_Personalizados_III` (SSH o HTTPS con token)
- Opcional: subir todo el proyecto si lo prefieres

## Soporte
- Logs: `docker-compose logs -f odoo`
- Reinicio: `docker-compose restart odoo`