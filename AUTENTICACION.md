# Sistema de Autenticación y Usuarios - Resumen de Implementación

## ✅ Lo que se ha implementado

### 1. **App Usuarios** - Sistema completo de autenticación con Token

#### Modelos creados:
- **Rol**: 3 roles del sistema (Administrativo, Psicólogo, Paciente)
- **Usuario**: Modelo extendido de AbstractUser con:
  - Información personal (nombre, email, teléfono, fecha_nacimiento)
  - Relaciones con catálogos (género, edad, escolaridad, ocupación)
  - Campo de rol (ForeignKey a Rol)
  - Campos profesionales para psicólogos (cédula, especialidad)
  - Métodos helper: `is_administrativo`, `is_psicologo`, `is_paciente`
  
- **DatosPaciente**: Información adicional para pacientes:
  - Datos del responsable (nombre, teléfono, parentesco)
  - Información médica (alergias, medicamentos, antecedentes)

#### Serializers:
- `RolSerializer` - Para roles
- `UsuarioSerializer` - Base
- `UsuarioListSerializer` - Listado
- `UsuarioDetailSerializer` - Detalle completo
- `UsuarioCreateSerializer` - Creación con validación de contraseñas
- `UsuarioUpdateSerializer` - Actualización
- `ChangePasswordSerializer` - Cambio de contraseña
- `LoginSerializer` - Login
- `DatosPacienteSerializer` - Datos de pacientes

#### ViewSets:
- `AuthViewSet` - Autenticación:
  - `login/` - Iniciar sesión (genera o retorna token)
  - `logout/` - Cerrar sesión (**elimina el token del usuario**)
  - `me/` - Obtener datos del usuario autenticado

- `UsuarioViewSet` - Gestión de usuarios:
  - CRUD completo con permisos por rol
  - `change_password/` - Cambiar contraseña
  - `pacientes/` - Listar solo pacientes
  - `psicologos/` - Listar solo psicólogos

- `RolViewSet` - Gestión de roles (solo Admin)

#### Permisos personalizados:
- `IsAdministrativo` - Solo administrativos
- `IsPsicologo` - Solo psicólogos
- `IsPaciente` - Solo pacientes
- `IsAdministrativoOrPsicologo` - Admin o Psicólogo

### 2. **Actualización del modelo Entrenamiento**

- Agregada relación `ForeignKey` con Usuario (paciente)
- Campo `paciente` con `limit_choices_to` para solo pacientes
- Campos de control: `activo`, `created_at`, `updated_at`
- Método `__str__` mejorado con información del paciente

### 3. **Serializers y ViewSets de Entrenamiento actualizados**

#### Serializers:
- `EntrenamientoSerializer` - Con información del paciente
- `EntrenamientoListSerializer` - Listado optimizado
- `EntrenamientoCreateSerializer` - Creación
- `EntrenamientoUpdateSerializer` - Actualización

#### ViewSet con permisos:
- Administrativos y Psicólogos: ven todas las evaluaciones
- Pacientes: solo ven sus propias evaluaciones
- Solo Admin/Psicólogo pueden crear/editar evaluaciones
- Solo Admin puede eliminar evaluaciones

#### Acciones adicionales:
- `por_paciente/` - Filtrar por paciente
- `mis_evaluaciones/` - Evaluaciones del usuario autenticado
- `estadisticas/` - Estadísticas generales

### 4. **Configuración de Django**

#### Settings.py actualizado con:
- `AUTH_USER_MODEL = 'Usuarios.Usuario'`
- Configuración de CORS
- Configuración de Token Authentication (Django REST Framework)
- REST Framework configurado con:
  - Autenticación por Token
  - Paginación (10 items por página)
  - Filtros

#### Dependencias:
- `djangorestframework` - API REST con sistema de tokens
- `django-cors-headers` - CORS
- `django-filter` - Filtros

### 5. **Archivos adicionales**

- `roles_iniciales.sql` - Script para insertar los 3 roles
- `INSTALACION.md` - Guía completa de instalación
- README.md actualizado con:
  - Nuevas tecnologías
  - Endpoints de autenticación
  - Roles y permisos
  - Estructura actualizada

### 6. **URLs configuradas**

```
/api/v1/
  ├── auth/
  │   ├── login/          (POST)
  │   ├── logout/         (DELETE/POST)
  │   └── me/             (GET)
  ├── usuarios/
  ├── roles/
  ├── catalogos/
  │   ├── categorias/
  │   ├── generos/
  │   ├── opciones/
  │   ├── preguntas/
  │   ├── sepomex/
  │   ├── edades/
  │   ├── escolaridad/
  │   ├── ocupacion/
  │   └── parentesco/
  └── entrenamiento/
      ├── por_paciente/
      ├── mis_evaluaciones/
      └── estadisticas/
```

## 🔐 Flujo de Autenticación

1. **Login** → Genera Token único (no expira hasta logout)
2. **Requests** → Usar Token en header: `Authorization: Token <token>`
3. **Logout** → Elimina el token de la base de datos (token ya no es válido)

**Importante**: El token se elimina completamente al hacer logout, no se puede reusar.

## 👥 Lógica de Permisos

### Administrativo
- ✅ CRUD completo de usuarios
- ✅ CRUD completo de evaluaciones
- ✅ Ver estadísticas
- ✅ Gestión de catálogos

### Psicólogo
- ✅ Ver pacientes
- ✅ Crear/editar evaluaciones
- ✅ Ver estadísticas
- ❌ No puede crear/eliminar usuarios

### Paciente
- ✅ Ver sus propias evaluaciones
- ✅ Editar su perfil
- ❌ No puede crear evaluaciones
- ❌ No puede ver otros pacientes

## 🚀 Próximos pasos

1. Instalar dependencias: `pipenv install`
2. Ejecutar migraciones: `python manage.py makemigrations && python manage.py migrate`
3. Cargar roles: `psql -U usuario -d bd -f roles_iniciales.sql`
4. Crear superusuario: `python manage.py createsuperuser`
5. Asignar rol administrativo al superusuario (desde admin o SQL)
6. Probar login desde la API

## 📌 Notas Importantes

- Los tokens se eliminan completamente de la base de datos al hacer logout
- Un usuario solo puede tener un token activo a la vez
- Si un usuario hace login nuevamente, se reutiliza el token existente
- Los pacientes solo pueden ver sus propias evaluaciones
- Las evaluaciones están relacionadas con usuarios tipo "paciente"
- El modelo User personalizado usa email único
- Header de autenticación: `Authorization: Token <token_key>`
