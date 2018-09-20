from flask_restplus.namespace import Namespace

ns_auth = Namespace('auth', description='Auth operations')
ns_me = Namespace('me', description='Me operations')
ns_user = Namespace('users', description='User operations')
ns_service = Namespace('service', description='Service operations')

namespaces = [ns_auth, ns_me, ns_user, ns_service]
