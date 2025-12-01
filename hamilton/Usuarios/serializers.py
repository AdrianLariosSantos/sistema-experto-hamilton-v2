from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Usuario, Rol, DatosPaciente


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre', 'descripcion', 'activo']


class DatosPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosPaciente
        fields = [
            'id', 'parentesco_responsable', 'nombre_responsable', 
            'telefono_responsable', 'alergias', 'medicamentos_actuales',
            'antecedentes_medicos'
        ]


class UsuarioSerializer(serializers.ModelSerializer):
    """Serializer base para Usuario"""
    rol_nombre = serializers.CharField(source='rol.get_nombre_display', read_only=True)
    genero_nombre = serializers.CharField(source='genero.descripcion', read_only=True)
    edad_nombre = serializers.CharField(source='edad.descripcion', read_only=True)
    escolaridad_nombre = serializers.CharField(source='escolaridad.descripcion', read_only=True)
    ocupacion_nombre = serializers.CharField(source='ocupacion.descripcion', read_only=True)
    
    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'telefono', 'fecha_nacimiento', 'genero', 'genero_nombre',
            'edad', 'edad_nombre', 'escolaridad', 'escolaridad_nombre',
            'ocupacion', 'ocupacion_nombre', 'rol', 'rol_nombre',
            'cedula_profesional', 'especialidad', 'activo',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class UsuarioListSerializer(serializers.ModelSerializer):
    """Serializer para listar usuarios"""
    rol_nombre = serializers.CharField(source='rol.get_nombre_display', read_only=True)
    nombre_completo = serializers.SerializerMethodField()
    
    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'nombre_completo',
            'telefono', 'rol', 'rol_nombre', 'activo'
        ]
    
    def get_nombre_completo(self, obj):
        return obj.get_full_name() or obj.username


class UsuarioDetailSerializer(serializers.ModelSerializer):
    """Serializer detallado para usuarios"""
    rol_data = RolSerializer(source='rol', read_only=True)
    datos_paciente = DatosPacienteSerializer(read_only=True)
    genero_nombre = serializers.CharField(source='genero.descripcion', read_only=True)
    edad_nombre = serializers.CharField(source='edad.descripcion', read_only=True)
    escolaridad_nombre = serializers.CharField(source='escolaridad.descripcion', read_only=True)
    ocupacion_nombre = serializers.CharField(source='ocupacion.descripcion', read_only=True)
    
    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'telefono', 'fecha_nacimiento', 'genero', 'genero_nombre',
            'edad', 'edad_nombre', 'escolaridad', 'escolaridad_nombre',
            'ocupacion', 'ocupacion_nombre', 'rol', 'rol_data',
            'cedula_profesional', 'especialidad', 'activo',
            'datos_paciente', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class UsuarioCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear usuarios"""
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)
    datos_paciente = DatosPacienteSerializer(required=False)
    
    class Meta:
        model = Usuario
        fields = [
            'username', 'email', 'password', 'password_confirm',
            'first_name', 'last_name', 'telefono', 'fecha_nacimiento',
            'genero', 'edad', 'escolaridad', 'ocupacion', 'rol',
            'cedula_profesional', 'especialidad', 'datos_paciente'
        ]
    
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden"})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        datos_paciente_data = validated_data.pop('datos_paciente', None)
        password = validated_data.pop('password')
        
        usuario = Usuario.objects.create(**validated_data)
        usuario.set_password(password)
        usuario.save()
        
        # Si es paciente, crear datos adicionales
        if usuario.is_paciente and datos_paciente_data:
            DatosPaciente.objects.create(usuario=usuario, **datos_paciente_data)
        
        return usuario


class UsuarioUpdateSerializer(serializers.ModelSerializer):
    """Serializer para actualizar usuarios"""
    datos_paciente = DatosPacienteSerializer(required=False)
    
    class Meta:
        model = Usuario
        fields = [
            'email', 'first_name', 'last_name', 'telefono',
            'fecha_nacimiento', 'genero', 'edad', 'escolaridad',
            'ocupacion', 'cedula_profesional', 'especialidad',
            'activo', 'datos_paciente'
        ]
    
    def update(self, instance, validated_data):
        datos_paciente_data = validated_data.pop('datos_paciente', None)
        
        # Actualizar usuario
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Actualizar datos de paciente si existen
        if instance.is_paciente and datos_paciente_data:
            if hasattr(instance, 'datos_paciente'):
                for attr, value in datos_paciente_data.items():
                    setattr(instance.datos_paciente, attr, value)
                instance.datos_paciente.save()
            else:
                DatosPaciente.objects.create(usuario=instance, **datos_paciente_data)
        
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer para cambiar contraseña"""
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    new_password_confirm = serializers.CharField(required=True, write_only=True)
    
    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('new_password_confirm'):
            raise serializers.ValidationError({"new_password": "Las contraseñas no coinciden"})
        return attrs
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("La contraseña actual es incorrecta")
        return value
    
    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer para login"""
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
