# Sistema Experto Hamilton v2

Sistema experto para evaluación de ansiedad y depresión basado en la Escala de Hamilton.

## 🎯 Descripción

Aplicación web que permite realizar evaluaciones psicológicas mediante cuestionarios estructurados para detectar niveles de ansiedad y depresión, utilizando la reconocida Escala de Hamilton.

## 🛠️ Tecnologías

### Backend
- **Django 5.2** - Framework web
- **Django REST Framework** - API REST
- **Simple JWT** - Autenticación con tokens JWT
- **PostgreSQL** - Base de datos
- **Python 3.12**
- **CORS Headers** - Manejo de CORS

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

# Cargar roles iniciales
psql -U tu_usuario -d nombre_base_datos -f roles_iniciales.sql

# Cargar datos iniciales (opcional)
psql -U tu_usuario -d nombre_base_datos -f preguntas.sql
psql -U tu_usuario -d nombre_base_datos -f respuestas.sql

# Crear superusuario administrativo
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
│   ├── Entrenamiento/        # App de evaluaciones psicológicas
│   ├── Usuarios/             # App de autenticación y usuarios
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

### Usuarios
- **Rol**: Roles del sistema (Administrativo, Psicólogo, Paciente)
- **Usuario**: Modelo extendido de usuario con información adicional
- **DatosPaciente**: Información específica de pacientes

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
- **Entrenamiento**: Evaluaciones psicológicas de pacientes (relacionado con Usuario)

## 🌐 API Endpoints

### Autenticación
```
POST   /api/v1/auth/login/          - Iniciar sesión
POST   /api/v1/auth/logout/         - Cerrar sesión (blacklist token)
POST   /api/v1/auth/refresh/        - Refrescar token de acceso
GET    /api/v1/auth/me/             - Obtener datos del usuario autenticado
```

### Usuarios
```
GET    /api/v1/usuarios/            - Listar usuarios
POST   /api/v1/usuarios/            - Crear usuario (solo Admin)
GET    /api/v1/usuarios/{id}/       - Detalle de usuario
PUT    /api/v1/usuarios/{id}/       - Actualizar usuario
PATCH  /api/v1/usuarios/{id}/       - Actualizar parcial
DELETE /api/v1/usuarios/{id}/       - Desactivar usuario (solo Admin)
POST   /api/v1/usuarios/{id}/change_password/ - Cambiar contraseña
GET    /api/v1/usuarios/pacientes/  - Listar solo pacientes
GET    /api/v1/usuarios/psicologos/ - Listar solo psicólogos (solo Admin)
```

### Roles
```
GET    /api/v1/roles/               - Listar roles (solo Admin)
```

### Catálogos
```
/api/v1/catalogos/
  ├── categorias/
  ├── generos/
  ├── opciones/
  ├── preguntas/
  ├── sepomex/
  ├── edades/
  ├── escolaridad/
  ├── ocupacion/
  └── parentesco/
```

### Evaluaciones
```
GET    /api/v1/entrenamiento/                    - Listar evaluaciones
POST   /api/v1/entrenamiento/                    - Crear evaluación (Admin/Psicólogo)
GET    /api/v1/entrenamiento/{id}/               - Detalle de evaluación
PUT    /api/v1/entrenamiento/{id}/               - Actualizar evaluación (Admin/Psicólogo)
DELETE /api/v1/entrenamiento/{id}/               - Desactivar evaluación (solo Admin)
GET    /api/v1/entrenamiento/por_paciente/       - Evaluaciones por paciente
GET    /api/v1/entrenamiento/mis_evaluaciones/   - Mis evaluaciones (Pacientes)
GET    /api/v1/entrenamiento/estadisticas/       - Estadísticas (Admin/Psicólogo)
```

## 👥 Roles y Permisos

### Administrativo
- Acceso completo al sistema
- Gestión de usuarios (crear, editar, eliminar)
- Gestión de evaluaciones
- Acceso a estadísticas
- Gestión de catálogos

### Psicólogo
- Ver y gestionar pacientes
- Crear y editar evaluaciones
- Ver estadísticas
- Acceso a catálogos

### Paciente
- Ver solo sus propias evaluaciones
- Ver sus datos personales
- Actualizar su perfil

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
