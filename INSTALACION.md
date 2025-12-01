# Instrucciones de Instalación - Sistema Experto Hamilton v2

## 📦 Instalación Completa del Sistema

### 1. Instalar Dependencias de Python

```bash
# Asegúrate de estar en la raíz del proyecto
cd /home/adrianls/Proyectos/sistema-experto

# Instalar dependencias con pipenv
pipenv install

# Activar el entorno virtual
pipenv shell
```

### 2. Configurar Base de Datos

```bash
# Crear la base de datos en PostgreSQL
createdb nombre_base_datos

# O desde psql:
psql -U postgres
CREATE DATABASE nombre_base_datos;
\q
```

### 3. Configurar Variables de Entorno

```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar el archivo .env con tus credenciales
nano .env
```

Contenido del .env:
```
DB_NAME=nombre_base_datos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=tu-secret-key-muy-segura
DEBUG=True
```

### 4. Ejecutar Migraciones

```bash
cd hamilton

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
```

### 5. Cargar Datos Iniciales

```bash
# Cargar roles del sistema
psql -U tu_usuario -d nombre_base_datos -f roles_iniciales.sql

# Opcional: Cargar preguntas y datos de entrenamiento
psql -U tu_usuario -d nombre_base_datos -f preguntas.sql
psql -U tu_usuario -d nombre_base_datos -f respuestas.sql
```

### 6. Crear Usuario Administrativo

```bash
python manage.py createsuperuser
```

**IMPORTANTE**: Después de crear el superusuario, debes asignarle el rol de Administrativo desde el admin de Django o desde la base de datos:

```sql
-- Obtener el ID del rol administrativo
SELECT id FROM cat_roles WHERE nombre = 'administrativo';

-- Asignar el rol al superusuario (reemplaza <usuario_id> con el ID del usuario)
UPDATE usuarios SET rol_id = (SELECT id FROM cat_roles WHERE nombre = 'administrativo') WHERE id = <usuario_id>;
```

### 7. Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: http://localhost:8000

### 8. Configurar el Frontend (Opcional)

```bash
# En otra terminal, navega a la carpeta del frontend
cd frontend1.1

# Instalar dependencias
npm install

# Ejecutar servidor de desarrollo
npm run dev
```

El frontend estará disponible en: http://localhost:5173

## 🔑 Acceso Inicial

### Admin Panel Django
- URL: http://localhost:8000/admin
- Usuario: El creado con createsuperuser
- Contraseña: La que configuraste

### API Endpoints
- Base URL: http://localhost:8000/api/v1/

## 🧪 Probar la Autenticación

### Login
```bash
curl -X POST http://localhost:8000/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "tu_usuario",
    "password": "tu_contraseña"
  }'
```

Respuesta exitosa:
```json
{
  "status": "success",
  "data": {
    "user": { ... },
    "tokens": {
      "refresh": "eyJ0eXAi...",
      "access": "eyJ0eXAi..."
    }
  }
}
```

### Usar el Token en Requests

```bash
curl -X GET http://localhost:8000/api/v1/auth/me/ \
  -H "Authorization: Bearer <tu_access_token>"
```

### Logout (Blacklist Token)

```bash
curl -X POST http://localhost:8000/api/v1/auth/logout/ \
  -H "Authorization: Bearer <tu_access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "refresh_token": "<tu_refresh_token>"
  }'
```

## 📝 Crear Usuarios con Diferentes Roles

### Desde el Admin Panel

1. Ir a http://localhost:8000/admin/Usuarios/usuario/add/
2. Llenar los datos del usuario
3. Seleccionar el rol correspondiente
4. Guardar

### Desde la API (requiere autenticación como Admin)

```bash
# Crear un Psicólogo
curl -X POST http://localhost:8000/api/v1/usuarios/ \
  -H "Authorization: Bearer <tu_access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "psicologo1",
    "email": "psicologo@example.com",
    "password": "password123",
    "password_confirm": "password123",
    "first_name": "Juan",
    "last_name": "Pérez",
    "rol": 2,
    "cedula_profesional": "12345678",
    "especialidad": "Psicología Clínica"
  }'

# Crear un Paciente
curl -X POST http://localhost:8000/api/v1/usuarios/ \
  -H "Authorization: Bearer <tu_access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "paciente1",
    "email": "paciente@example.com",
    "password": "password123",
    "password_confirm": "password123",
    "first_name": "María",
    "last_name": "González",
    "rol": 3,
    "genero": 1,
    "edad": 1,
    "datos_paciente": {
      "nombre_responsable": "Pedro González",
      "telefono_responsable": "1234567890",
      "parentesco_responsable": 1
    }
  }'
```

## 🚨 Solución de Problemas Comunes

### Error: relation "cat_roles" does not exist
```bash
# Ejecutar las migraciones nuevamente
python manage.py migrate

# Cargar los roles
psql -U tu_usuario -d nombre_base_datos -f roles_iniciales.sql
```

### Error: relation "usuarios" does not exist
```bash
# Crear las migraciones para Usuarios
python manage.py makemigrations Usuarios
python manage.py migrate Usuarios
```

### Error: AUTH_USER_MODEL not set
Verificar que en settings.py esté configurado:
```python
AUTH_USER_MODEL = 'Usuarios.Usuario'
```

### Error al hacer login: Token blacklist not available
```bash
# Ejecutar la migración para el blacklist
python manage.py migrate rest_framework_simplejwt.token_blacklist
```

## ✅ Verificación de Instalación

1. Servidor Django corriendo: ✓
2. Base de datos creada: ✓
3. Migraciones aplicadas: ✓
4. Roles cargados: ✓
5. Usuario administrativo creado: ✓
6. Login funcionando: ✓
7. Tokens JWT generados correctamente: ✓

¡El sistema está listo para usar!
