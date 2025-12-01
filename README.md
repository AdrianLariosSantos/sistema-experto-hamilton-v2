# Sistema Experto Hamilton v2

Sistema experto para evaluación de ansiedad y depresión basado en la Escala de Hamilton.

## 🎯 Descripción

Aplicación web que permite realizar evaluaciones psicológicas mediante cuestionarios estructurados para detectar niveles de ansiedad y depresión, utilizando la reconocida Escala de Hamilton.

## 🛠️ Tecnologías

### Backend
- **Django 5.2** - Framework web
- **Django REST Framework** - API REST
- **PostgreSQL** - Base de datos
- **Python 3.12**

### Frontend
- **Vue 3** - Framework JavaScript
- **Vite** - Build tool
- **Tailwind CSS** - Estilos
- **Pinia** - State management

## 📋 Requisitos Previos

- Python 3.12+
- PostgreSQL 12+
- Node.js 16+
- pipenv

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/AdrianLariosSantos/sistema-experto-hamilton-v2.git
cd sistema-experto-hamilton-v2
```

### 2. Configurar Backend

```bash
# Instalar dependencias
pipenv install

# Activar entorno virtual
pipenv shell

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales de base de datos

# Navegar a la carpeta del proyecto Django
cd hamilton

# Ejecutar migraciones
python manage.py migrate

# Cargar datos iniciales (opcional)
psql -U tu_usuario -d nombre_base_datos -f preguntas.sql
psql -U tu_usuario -d nombre_base_datos -f respuestas.sql

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

### 3. Configurar Frontend

```bash
# Navegar a la carpeta del frontend
cd frontend1.1

# Instalar dependencias
npm install

# Ejecutar servidor de desarrollo
npm run dev
```

## 📁 Estructura del Proyecto

```
sistema-experto/
├── hamilton/                  # Proyecto Django
│   ├── Catalogos/            # App de catálogos (géneros, edades, preguntas)
│   ├── Entrenamiento/        # App de datos de entrenamiento
│   ├── Apis/                 # Configuración de URLs de API
│   ├── helpers/              # Utilidades y respuestas
│   └── hamilton/             # Configuración principal
├── frontend1.1/              # Aplicación Vue.js
│   ├── src/
│   │   ├── components/       # Componentes reutilizables
│   │   ├── views/            # Vistas/páginas
│   │   ├── router/           # Configuración de rutas
│   │   ├── services/         # Servicios API
│   │   └── store/            # Store Pinia
│   └── public/
└── .env.example              # Plantilla de variables de entorno
```

## 🔧 Modelos Principales

### Catalogos
- **Categorias**: Categorías de preguntas (Ansiedad, Depresión)
- **Preguntas**: Banco de preguntas de la escala Hamilton
- **Opciones**: Opciones de respuesta
- **Generos**: Catálogo de géneros
- **Edades**: Catálogo de rangos de edad
- **Escolaridad**: Niveles educativos
- **Ocupacion**: Tipos de ocupación
- **Parentesco**: Relaciones familiares

### Entrenamiento
- **Entrenamiento**: Datos históricos para análisis y predicción

## 🌐 API Endpoints

```
/api/v1/catalogos/
  ├── catalogo-categorias/
  ├── catalogo-generos/
  ├── catalogo-opciones/
  ├── catalogo-preguntas/
  ├── catalogo-edades/
  └── catalogo-sepomex/

/api/v1/entrenamiento/
```

## 🔐 Variables de Entorno

Copiar `.env.example` a `.env` y configurar:

```env
DB_NAME=nombre_base_datos
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=tu-secret-key
DEBUG=True
```

## 👨‍💻 Desarrollo

### Backend
- El servidor Django corre en: `http://localhost:8000`
- Admin panel: `http://localhost:8000/admin`
- API: `http://localhost:8000/api/v1/`

### Frontend
- El servidor Vite corre en: `http://localhost:5173`

## 📝 Notas

- Las preguntas están basadas en la Escala de Hamilton para Ansiedad y Depresión
- El sistema incluye datos de entrenamiento para análisis predictivo
- Se recomienda usar PostgreSQL para producción

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría hacer.

## 📄 Licencia

Este proyecto es privado.

## ✅ Correcciones Realizadas (30/11/2025)

1. ✅ Corregido error ortográfico `cateogria` → `categoria` en models.py y serializers.py
2. ✅ Arreglado método `__str__` de modelo `Preguntas` (usaba `self.numero` inexistente)
3. ✅ Eliminado campo `rango` inexistente en `EdadesCreateSerializers`
4. ✅ Reescrito `viewsets.py` eliminando referencias a modelos inexistentes
5. ✅ Creado archivo `.env.example` como plantilla
6. ✅ Actualizado README con documentación completa
