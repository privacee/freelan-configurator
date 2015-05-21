#!/usr/bin/env python

from __future__ import print_function

class FreelanCFGserver(object):
    """"""
    def __init__(self):

        self.defaults = {   'enabled': False,
                            'listen_on': '0.0.0.0:443',
                            'protocol': 'https',
                            'server_certificate_file': None,
                            'server_private_key_file': None,
                            'certification_authority_certificate_file': None,
                            'certification_authority_private_key_file': None,
                            'authentication_script': None   }

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

        self.defaults = {   'enabled': False,
                            'server_endpoint': '127.0.0.1:443',
                            'protocol': 'https',
                            'disable_peer_verification': False,
                            'disable_host_verification': False,
                            'username': None,
                            'password': None,
                            'public_endpoint': '0.0.0.0'   }

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

        self.defaults = {   'hostname_resolution_protocol': 'ipv4',
                            'listen_on': '0.0.0.0:12000',
                            'listen_on_device': None,
                            'hello_timeout': '3000',
                            'contact': None,
                            'accept_contact_requests': True,
                            'accept_contacts': True,
                            'dynamic_contact_file': None,
                            'never_contact': None,
                            'cipher_capability':  ['ecdhe_rsa_aes256_gcm_sha384', 'ecdhe_rsa_aes128_gcm_sha256'],
                            'elliptic_curve_capability':  ['sect571k1', 'secp384r1']   }

        self.hostname_resolution_protocol='ipv4'
        self.listen_on='0.0.0.0:12000'
        self.listen_on_device=None
        self.hello_timeout='3000'
        self.contact=None
        self.accept_contact_requests=True
        self.accept_contacts=True
        self.dynamic_contact_file=None
        self.never_contact=None
        self.cipher_capability=['ecdhe_rsa_aes256_gcm_sha384', 'ecdhe_rsa_aes128_gcm_sha256']
        self.elliptic_curve_capability=['sect571k1', 'secp384r1']

class FreelanCFGtap(object):
    """"""
    def __init__(self):

        self.defaults = {   'type': 'tap',
                            'enabled': True,
                            'name': None,
                            'mtu': 'auto',
                            'mss_override': 'auto',
                            'metric': 'auto',
                            'ipv4_address_prefix_length': '9.0.0.1/24',
                            'ipv6_address_prefix_length': '2aa1::1/8',
                            'remote_ipv4_address': '9.0.0.0',
                            'arp_proxy_enabled': False,
                            'arp_proxy_fake_ethernet_address': '00:aa:bb:cc:dd:ee',
                            'dhcp_proxy_enabled': True,
                            'dhcp_server_ipv4_address_prefix_length': '9.0.0.0/24',
                            'dhcp_server_ipv6_address_prefix_length': '2aa1::/8',
                            'up_script': None,
                            'down_script': None   }

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
        self.defaults = {   'routing_method': 'switch',
                            'relay_mode_enabled': False   }

        self.routing_method='switch'
        self.relay_mode_enabled=False

class FreelanCFGrouter(object):
    """"""
    def __init__(self):

        self.defaults = {   'local_ip_route': None,
                            'local_dns_server': None,
                            'client_routing_enabled': True,
                            'accept_routes_requests': True,
                            'internal_route_acceptance_policy': 'unicast_in_network',
                            'system_route_acceptance_policy': None,
                            'maximum_routes_limit': '1',
                            'dns_servers_acceptance_policy': 'in_network',
                            'dns_script': None   }

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

        self.defaults = {  'passphrase': None,
                           'passphrase_salt': 'freelan',
                           'passphrase_iterations_count': '2000',
                           'signature_certificate_file': None,
                           'signature_private_key_file': None,
                           'certificate_validation_method': 'default',
                           'certificate_validation_script': None,
                           'authority_certificate_file': None,
                           'certificate_revocation_validation_method': None,
                           'certificate_revocation_list_file': None   }

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
        self.tap_adapter = FreelanCFGtap()
        self.switch = FreelanCFGswitch()
        self.router = FreelanCFGrouter()
        self.security = FreelanCFGsecurity()

    def print(self, defaults=False):
        cfg = self.build(defaults=defaults)

        for cfg_line in cfg:
            print(cfg_line)

    def build(self, defaults=False):
        cfg = []

        cfg.append("[server]")
        cfg_sec = self.build_section(self.server, defaults=defaults)
        cfg.extend(cfg_sec)

        cfg.append("[client]")
        cfg_sec = self.build_section(self.client, defaults=defaults)
        cfg.extend(cfg_sec)

        cfg.append("[fscp]")
        cfg_sec = self.build_section(self.fscp, defaults=defaults)
        cfg.extend(cfg_sec)

        cfg.append("[tap]")
        cfg_sec = self.build_section(self.tap_adapter, defaults=defaults)
        cfg.extend(cfg_sec)

        cfg.append("[switch]")
        cfg_sec = self.build_section(self.switch, defaults=defaults)
        cfg.extend(cfg_sec)

        cfg.append("[router]")
        cfg_sec = self.build_section(self.router, defaults=defaults)
        cfg.extend(cfg_sec)

        # NOT recommended to do this!
        #self.security.certificate_validation_method = None

        cfg.append("[security]")
        cfg_sec = self.build_section(self.security, defaults=defaults)
        cfg.extend(cfg_sec)

        return cfg

    def build_section(self, section, defaults=False):
        cfg = []
        for k,default_v in section.defaults.iteritems():
            self_kv = getattr(section, k)

            #print ("Key: " + str(k) + " || Value: " + str(self_kv))

            if self_kv is None:
                if (not (self_kv is default_v) or defaults):
                    cfg.append(k+'=')
                continue

            if isinstance(self_kv, basestring) or isinstance(self_kv, bool) or self_kv is None:
                self_kv = [self_kv]

            if isinstance(default_v, basestring) or isinstance(default_v, bool) or default_v is None:
                default_v = [default_v]

            for kv in self_kv:
                if (not kv in default_v) or defaults:
                    cfg.append(k+'='+str(kv))

        return cfg