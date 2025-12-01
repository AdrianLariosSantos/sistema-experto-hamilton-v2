-- Insertar roles iniciales del sistema
INSERT INTO cat_roles (nombre, descripcion, activo, created_at, updated_at) 
VALUES 
    ('administrativo', 'Usuario con permisos completos de administración del sistema', true, NOW(), NOW()),
    ('psicologo', 'Profesional de psicología que puede gestionar pacientes y evaluaciones', true, NOW(), NOW()),
    ('paciente', 'Usuario que recibe evaluaciones psicológicas', true, NOW(), NOW())
ON CONFLICT (nombre) DO NOTHING;
