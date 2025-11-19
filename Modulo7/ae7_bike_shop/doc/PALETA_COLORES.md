# 🎨 Nueva Paleta de Colores - BikeShop

## Paleta Implementada

```css
.color1 { color: #00392d; } /* Verde oscuro */
.color2 { color: #006e8c; } /* Azul petróleo */
.color3 { color: #eb7f25; } /* Naranja */
.color4 { color: #ffcc52; } /* Amarillo dorado */
.color5 { color: #ffff8f; } /* Amarillo claro */
```

---

## 🔄 Cambios Realizados

### Paleta Anterior (Morado/Violeta)
- **Principal**: `#667eea` (Azul violeta)
- **Secundario**: `#764ba2` (Morado)
- **Acento**: `#ffc107` (Amarillo bootstrap)

### Nueva Paleta (Verde/Naranja)
- **Principal**: `#006e8c` (Azul petróleo) - Botones primarios, links
- **Oscuro**: `#00392d` (Verde oscuro) - Hover states, contraste
- **Acento**: `#eb7f25` (Naranja) - Success, totales, destacados
- **Amarillo**: `#ffcc52` (Dorado) - Carrito, warnings, estrellas
- **Claro**: `#ffff8f` (Amarillo claro) - Hover secundario

---

## 📝 Archivos Actualizados

### ✅ App Bicicletas
- `lista_bicicletas.html`
  - Navbar: Gradiente verde oscuro → azul petróleo
  - Botones primary: Azul petróleo
  - Botones success: Naranja
  - Botones warning: Amarillo dorado
  
- `crear_bicicleta.html`
  - Navbar: Gradiente verde oscuro → azul petróleo
  - Botones primary: Azul petróleo

### ✅ App Reseñas
- `detalle_bicicleta.html`
  - Navbar: Gradiente verde oscuro → azul petróleo
  - Stats box: Gradiente verde oscuro → azul petróleo
  - Review cards: Border naranja
  - Estrellas: Amarillo dorado (#ffcc52)
  - Textos success: Naranja
  - Botones primary: Azul petróleo
  - Botones success: Naranja

- `crear_resena.html`
  - Navbar: Gradiente verde oscuro → azul petróleo
  - Botones primary: Azul petróleo

- `editar_resena.html`
  - Navbar: Gradiente verde oscuro → azul petróleo
  - Botones primary: Azul petróleo

- `mis_resenas.html`
  - Navbar: Gradiente verde oscuro → azul petróleo
  - Botones primary: Azul petróleo

### ✅ App Carrito
- `carrito_detalle.html`
  - Navbar: Gradiente verde oscuro → azul petróleo
  - Card headers primary: Azul petróleo
  - Card headers success: Naranja
  - Botones success: Naranja
  - Botones warning: Amarillo dorado
  - Textos success: Naranja

- `mis_ordenes.html`
  - Navbar: Gradiente verde oscuro → azul petróleo
  - Botones primary: Azul petróleo
  - Botones success: Naranja
  - Textos success: Naranja

### ✅ App Clientes (Autenticación)
- `login.html`
  - Background: Gradiente verde oscuro → azul petróleo
  - Input focus: Azul petróleo
  - Botón: Gradiente azul petróleo → verde oscuro
  - Links: Azul petróleo / Verde oscuro (hover)

- `registro.html`
  - Background: Gradiente verde oscuro → azul petróleo
  - Input focus: Azul petróleo
  - Botón: Gradiente azul petróleo → verde oscuro
  - Links: Azul petróleo / Verde oscuro (hover)

- `perfil.html`
  - Navbar: Gradiente verde oscuro → azul petróleo
  - Input focus: Azul petróleo
  - Botón: Gradiente azul petróleo → verde oscuro

---

## 🎨 Guía de Uso de Colores

### Verde Oscuro (#00392d)
**Uso**: Fondos principales, hover states de alta jerarquía
```css
background: #00392d;
```

### Azul Petróleo (#006e8c)
**Uso**: Botones primarios, links, elementos interactivos
```css
.btn-primary {
    background-color: #006e8c;
    border-color: #006e8c;
}
```

### Naranja (#eb7f25)
**Uso**: Acciones de éxito, totales, llamadas a la acción secundarias
```css
.btn-success, .text-success {
    background-color: #eb7f25;
    color: #eb7f25;
}
```

### Amarillo Dorado (#ffcc52)
**Uso**: Carrito, advertencias suaves, elementos destacados
```css
.btn-warning {
    background-color: #ffcc52;
}
```

### Amarillo Claro (#ffff8f)
**Uso**: Hover de elementos amarillos, fondos suaves
```css
.btn-warning:hover {
    background-color: #ffff8f;
}
```

---

## 🔍 Elementos Específicos

### Gradientes de Navbar
```css
background: linear-gradient(135deg, #00392d 0%, #006e8c 100%);
```

### Gradientes de Botones
```css
/* Botón Primary */
background: linear-gradient(135deg, #006e8c 0%, #00392d 100%);

/* Botón Primary Hover */
background: linear-gradient(135deg, #00392d 0%, #006e8c 100%);
```

### Stats Box (Reseñas)
```css
background: linear-gradient(135deg, #00392d 0%, #006e8c 100%);
color: white;
```

### Review Cards
```css
border-left: 4px solid #eb7f25;
```

### Estrellas de Rating
```css
.star-rating {
    color: #ffcc52;
}
```

---

## ✨ Mejoras Visuales

1. **Mayor contraste**: Verde oscuro + azul petróleo dan mejor legibilidad
2. **Esquema cálido**: Naranja y amarillo dan sensación amigable
3. **Jerarquía clara**: 
   - Verde oscuro: Autoridad
   - Azul petróleo: Acción
   - Naranja: Éxito/Destacado
   - Amarillo: Atención/Carrito
4. **Coherencia**: Todos los templates usan la misma paleta

---

## 🚀 Próximos Pasos (Opcional)

### Crear archivo CSS global:
```css
/* bikeshop/static/css/colors.css */
:root {
    --color-primary: #006e8c;
    --color-dark: #00392d;
    --color-accent: #eb7f25;
    --color-warning: #ffcc52;
    --color-light: #ffff8f;
}

.btn-primary {
    background-color: var(--color-primary);
}
```

### Aplicar en templates:
```html
<link rel="stylesheet" href="{% static 'css/colors.css' %}">
```

---

## 📊 Comparación Visual

| Elemento | Antes | Después |
|----------|-------|---------|
| Navbar | 🟣 Morado (#764ba2) | 🟢 Verde/Azul (#00392d → #006e8c) |
| Botón Primary | 🟣 Violeta (#667eea) | 🔵 Azul petróleo (#006e8c) |
| Success/Total | 🟢 Verde Bootstrap | 🟠 Naranja (#eb7f25) |
| Carrito | 🟡 Amarillo Bootstrap | 🟡 Amarillo dorado (#ffcc52) |
| Estrellas | 🟡 #ffc107 | 🟡 #ffcc52 |

---

## ✅ Verificación

Para verificar los cambios:
1. Inicia el servidor: `python manage.py runserver`
2. Navega a: http://localhost:8000/
3. Verifica:
   - ✅ Navbar verde/azul
   - ✅ Botones azul petróleo
   - ✅ Precios y totales en naranja
   - ✅ Carrito en amarillo dorado
   - ✅ Estrellas amarillo dorado

---

**¡Paleta de colores actualizada exitosamente! 🎨✨**
