# 🚀 INSTRUCCIONES RÁPIDAS: App Órdenes

## ✅ Pasos para Ejecutar

### 1. Aplicar Migraciones
```bash
python manage.py makemigrations ordenes
python manage.py migrate
```

### 2. Ejecutar el Ejemplo

**Desde el shell de Django:**
```bash
python manage.py shell
```

Luego copiar y pegar el contenido del archivo `ejemplo_ordenes.py`

---

## 📊 Resultado Esperado

El script creará:
- ✅ 2 clientes (Laura Gómez, Pedro Martínez)
- ✅ 3 bicicletas (Trek Marlin 7, Giant TCR Advanced, Specialized Stumpjumper)
- ✅ 2 órdenes con múltiples productos
- ✅ 4 detalles de orden (registros en la tabla intermedia)

---

## 🎯 Diferencias con el Ejemplo Original

### Modelo Bicicleta Original vs Actual

**Ejemplo original:**
```python
Bicicleta.objects.create(nombre="Mountain Bike", precio=500)
```

**Tu modelo actual:**
```python
Bicicleta.objects.create(
    marca="Trek",        # ← Campo marca
    modelo="Marlin 7",   # ← Campo modelo
    tipo="MTB",          # ← Campo tipo
    precio=850000,       # ← Precio en pesos chilenos
    anio=2024,           # ← Campo año
    disponible=True      # ← Campo disponible
)
```

### Adaptaciones Realizadas ✅

1. **Campo `nombre`** → **Campos `marca` y `modelo`**
   - Original: `bicicleta.nombre`
   - Adaptado: `bicicleta.marca` y `bicicleta.modelo`

2. **Método `__str__`** adaptado:
   ```python
   # En DetalleOrden
   def __str__(self):
       return f"{self.cantidad} x {self.bicicleta.marca} {self.bicicleta.modelo}"
   ```

3. **Precio formateado** con método personalizado:
   ```python
   # En el modelo Bicicleta (ya existente)
   def precio_formateado(self):
       return f"{self.precio:,.0f}".replace(",", ".")
   ```

---

## 💻 Comandos Útiles

### Abrir el shell de Django
```bash
python manage.py shell
```

### Crear una orden rápida
```python
from clientes.models import Cliente
from bicicletas.models import Bicicleta
from ordenes.models import Orden, DetalleOrden

# Cliente y bicicletas
c = Cliente.objects.create(nombre="Juan", email="juan@example.com")
b = Bicicleta.objects.create(marca="Trek", modelo="X", tipo="MTB", precio=500000, anio=2024)

# Orden
o = Orden.objects.create(cliente=c)
DetalleOrden.objects.create(orden=o, bicicleta=b, cantidad=1, precio_unitario=b.precio)
o.calcular_total()
```

### Ver todas las órdenes
```python
from ordenes.models import Orden
Orden.objects.all()
```

### Ver detalles de una orden
```python
orden = Orden.objects.get(id=1)
for detalle in orden.detalles.all():
    print(f"{detalle}: ${detalle.subtotal()}")
```

---

## 🔗 Related Names (Nombres Inversos)

```python
# Cliente → Órdenes
cliente.ordenes.all()

# Orden → Detalles
orden.detalles.all()

# Orden → Bicicletas (a través de ManyToMany)
orden.bicicletas.all()

# Bicicleta → Órdenes
bicicleta.ordenes.all()
```

---

## 🏗️ Estructura de Archivos

```
ae3_bikeshop/
├── ordenes/
│   ├── models.py           # Modelos Orden y DetalleOrden
│   ├── admin.py            # Admin configurado
│   └── migrations/
│       └── 0001_initial.py # Migración inicial
├── ejemplo_ordenes.py      # ⭐ Script de ejemplo
├── ORDENES_README.md       # Documentación completa
└── INSTRUCCIONES_ORDENES.md # Este archivo
```

---

## 📚 Archivos de Documentación

1. **`ejemplo_ordenes.py`**: Script completo con ejemplos de uso
2. **`ORDENES_README.md`**: Documentación detallada
3. **`INSTRUCCIONES_ORDENES.md`**: Esta guía rápida

---

## ✨ Admin de Django

Después de aplicar las migraciones, podrás:
1. Ver y crear órdenes desde el admin
2. Agregar detalles directamente (inline)
3. Ver totales calculados automáticamente
4. Filtrar por estado y fecha

```
http://localhost:8000/admin/ordenes/orden/
```

---

## 🎯 Próximos Pasos

1. ✅ Aplicar migraciones
2. ✅ Ejecutar el script de ejemplo
3. ✅ Explorar el admin de Django
4. 💡 Crear tus propias órdenes
5. 💡 Agregar vistas y templates (opcional)

---

*Guía rápida - 9 de noviembre de 2025*
