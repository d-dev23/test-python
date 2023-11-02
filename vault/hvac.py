import hvac

client = hvac.Client(
    url='http://10.0.1.54:8200',
    token='myroot',
)

#client.sys.enable_auth_method(
#    method_type='jwt',)

role_name = 'hvac7'
allowed_redirect_uris = ['http://10.0.1.54:8200/v1/auth/jwt/role/{role_name}']
user_claim = 'https://vault/user'

# JWT
client.auth.jwt.create_role(
    name=role_name,
    role_type='jwt',
    allowed_redirect_uris=allowed_redirect_uris,
    user_claim='sub',
    bound_audiences=['12345'],
    token_policies = ['secret-writer']
)

policy = '''
    path "sys" {
        capabilities = ["deny"]
    }
    path "secret" {
        capabilities = ["create", "read", "update", "delete", "list"]
    }
'''
client.sys.create_or_update_policy(
    name='secret-writer',
    policy=policy,
)
