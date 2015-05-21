#!/usr/bin/env python

class FreelanCFGserver(object):
    """"""
    def __init__(self):
        self.enabled=False
        self.listen_on= '0.0.0.0:443'
        self.protocol='https'
        self.server_certificate_file=None
        self.server_private_key_file=None
        self.certification_authority_certificate_file=None
        self.certification_authority_private_key_file=None
        self.authentication_script=None


class FreelanCFGclient(object):
    """"""
    def __init__(self):
        self.enabled=False
        self.server_endpoint= '127.0.0.1:443'
        self.protocol='https'
        self.disable_peer_verification=False
        self.disable_host_verification=False
        self.username=None
        self.password=None
        self.public_endpoint='0.0.0.0'

class FreelanCFGfscp(object):
    """"""
    def __init__(self):
        self.hostname_resolution_protocol='ipv4'
        self.listen_on='0.0.0.0:12012'
        self.listen_on_device=None
        self.hello_timeout='3000'
        self.contact=None
        self.accept_contact_requests=True
        self.accept_contacts=True
        self.dynamic_contact_file=None
        self.never_contact=None
        self.cipher_capability = ['ecdhe_rsa_aes256_gcm_sha384', 'ecdhe_rsa_aes128_gcm_sha256']
        self.elliptic_curve_capability = ['sect571k1', 'secp384r1']

class FreelanCFGtap(object):
    """"""
    def __init__(self):
        self.type='tap'
        self.enabled=True
        self.name=None
        self.mtu='auto'
        self.mss_override='auto'
        self.metric='auto'
        self.ipv4_address_prefix_length='9.0.0.1/24'
        self.ipv6_address_prefix_length='2aa1::1/8'
        self.remote_ipv4_address='9.0.0.0'
        self.arp_proxy_enabled=False
        self.arp_proxy_fake_ethernet_address='00:aa:bb:cc:dd:ee'
        self.dhcp_proxy_enabled=True
        self.dhcp_server_ipv4_address_prefix_length='9.0.0.0/24'
        self.dhcp_server_ipv6_address_prefix_length='2aa1::/8'
        self.up_script=None
        self.down_script=None

class FreelanCFGswitch(object):
    """"""
    def __init__(self):
        self.routing_method='switch'
        self.relay_mode_enabled=False

class FreelanCFGrouter(object):
    """"""
    def __init__(self):
        self.local_ip_route=None
        self.local_dns_server=None
        self.client_routing_enabled=True
        self.accept_routes_requests=True
        self.internal_route_acceptance_policy='unicast_in_network'
        self.system_route_acceptance_policy=None
        self.maximum_routes_limit='1'
        self.dns_servers_acceptance_policy='in_network'
        self.dns_script=None

class FreelanCFGsecurity(object):
    """"""
    def __init__(self):
        self.passphrase=None
        self.passphrase_salt='freelan'
        self.passphrase_iterations_count='2000'
        self.signature_certificate_file=None
        self.signature_private_key_file=None
        self.certificate_validation_method='default'
        self.certificate_validation_script=None
        self.authority_certificate_file=None
        self.certificate_revocation_validation_method=None
        self.certificate_revocation_list_file=None

class FreelanCFG(object):
    """holds freelan config info"""
    def __init__(self):
        self.server = FreelanCFGserver()
        self.client = FreelanCFGclient()
        self.fscp = FreelanCFGfscp()
        self.tap = FreelanCFGtap()
        self.switch = FreelanCFGswitch()
        self.router = FreelanCFGrouter()
        self.security = FreelanCFGsecurity()
