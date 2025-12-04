# 📦 Configuración de Productos - IT Solutions Company

## ✅ Configuración Completada

### 1. **Productos Creados** (5 total)

| ID | Producto | Código | Precio | Tipo |
|----|----------|--------|--------|------|
| 1 | Cloud Server VPS Pro | CLOUD-VPS-PRO | $299.99 | Servicio |
| 2 | Web Development Package | WEB-DEV-PKG | $4,999.00 | Servicio |
| 3 | Cybersecurity Audit | SEC-AUDIT | **$1,499.00** ⭐ | Servicio |
| 4 | IT Support Subscription | IT-SUPPORT-MONTHLY | $499.00 | Servicio |
| 5 | Dell PowerEdge Server | DELL-PE-R440 | $3,499.00 | Producto |

### 2. **Oferta Configurada** ⭐
- **Cybersecurity Audit**: Precio rebajado de $1,999.00 a **$1,499.00**

## 📋 Configuración Manual Pendiente

### 🔧 1. Añadir VARIANTES a Cloud Server VPS Pro

**Pasos:**
1. Ve a: **Ventas → Productos → Productos**
2. Busca y abre: **Cloud Server VPS Pro**
3. Haz clic en la pestaña: **Atributos y Variantes**
4. Haz clic en **Añadir una línea**
5. Crear atributo:
   - **Atributo**: RAM Size (crear nuevo si no existe)
   - **Valores**: 
     - 8 GB (+$0.00)
     - 16 GB (+$50.00)
     - 32 GB (+$100.00)
6. Guardar

**Resultado**: El cliente podrá elegir la cantidad de RAM al comprar.

---

### 🎁 2. Añadir ACCESORIO a Web Development Package

**Pasos:**
1. Ve a: **Ventas → Productos → Productos**
2. Busca y abre: **Web Development Package**
3. Haz clic en la pestaña: **Ventas**
4. Desplázate hasta la sección: **Productos Opcionales**
5. Haz clic en **Añadir una línea**
6. Selecciona: **IT Support Subscription**
7. Guardar

**Resultado**: Cuando se añada Web Development al carrito, se sugerirá IT Support Subscription como accesorio.

---

### 📦 3. Establecer Dell Server SIN STOCK

**Pasos:**
1. Ve a: **Inventario → Productos → Productos**
2. Busca y abre: **Dell PowerEdge Server**
3. Haz clic en el botón **Actualizar Cantidad**
4. Establece la cantidad a: **0**
5. Confirmar

**Resultado**: El producto mostrará "Sin stock" en el website.

---

### 🌐 4. Publicar Productos en el Website

**Pasos:**
1. Ve a: **Website → eCommerce → Productos**
2. O directamente: **Ventas → Productos → Productos**
3. Para cada producto:
   - Abre el producto
   - Haz clic en el botón **Ir al Website** (arriba a la derecha)
   - Haz clic en **Publicar** (interruptor en la parte superior)

**Alternativamente** (Rápido):
1. Ve a: **Website → eCommerce → Productos**
2. Selecciona todos los productos (checkbox)
3. Acción → **Website published: set true**

---

## 🔍 Verificación

### Ver Productos en el Website
```
http://localhost:8069/shop
```

### Ver Productos en Inventario
```
http://localhost:8069/web#action=stock.product_product_normal_action
```

### Ver Productos en Ventas
```
http://localhost:8069/web#action=product.product_template_action
```

---

## 📝 Resumen de Configuración

- [x] 5 productos creados
- [x] Cybersecurity Audit en oferta ($1,499)
- [ ] Cloud Server con variantes de RAM (manual)
- [ ] Web Development con accesorio IT Support (manual)
- [ ] Dell Server sin stock (manual)
- [ ] Todos los productos publicados (manual)

---

## 💡 Tips Adicionales

### Para añadir imágenes a los productos:
1. Abre el producto
2. Haz clic en el icono de cámara (foto del producto)
3. Sube la imagen

### Para añadir descripciones en el website:
1. Abre el producto
2. Pestaña **Ventas**
3. Campo **Descripción de Ventas** (descripción larga para eCommerce)

### Para configurar categorías:
1. **Inventario → Configuración → Categorías de Producto**
2. Crea categorías como: "Servicios", "Hardware", "Cloud", etc.
3. Asigna los productos a sus categorías

---

**¿Necesitas ayuda con alguna configuración manual?** Puedo guiarte paso a paso.
