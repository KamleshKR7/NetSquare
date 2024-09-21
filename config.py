port="5000"
deployment_folder="/opt/example"
WHEEL_FILE="Example-1.1.2-py3-none-any.whl"
INSTANCE_PATH="/opt/example/instance"
SECRET_KEY="AVerySafeExampleKey123!"
DB_PATH="postgresql://example_user:myVerySecretDatabasePassword@localhost:5432/example_db"
ADMIN_GROUPS = {
    'read_only': {
        'description': 'Read-only access',
        'permissions': ['read']
    },
    'read_write': {
        'description': 'Read and write access',
        'permissions': ['read', 'write']
    },
    'super': {
        'description': 'Superuser access with all permissions',
        'permissions': ['read', 'write', 'delete', 'admin']
    }
}