# -*- coding: utf-8 -*-
import db

# class Package():
#     def __init__(
#             self,
#             product_name,
#             tenant_id,
#             created_at,
#             resource_ref,
#             resource_name,
#             id_transaction,
#             id_admin):
#         self.product_name = product_name
#         self.tenant_id = tenant_id
#         self.created_at = created_at
#         self.resource_ref = resource_ref
#         self.resource_name = resource_name
#         self.id_transaction = id_transaction
#         self.id_admin = id_admin

class Campaign():
    def __init__(
            self,
            id,
            name,
            email,
            note):
        self.id = id
        self.name = name
        self.email=email
        self.note=note
class Brandname():
    def __init__(
        self,
        id,
        brandname,
        register,
        status
    ):
        self.id=id
        self.brandname=brandname
        self.register=register
        self.status=status
class WhiteList():
    def __init__(
        self,
        IP,
        note,
    ):
        self.IP=IP
        self.note=note
class Account():
    def __init__(
        self,
        id,
        username,
        password,
        brandname,
        info_route,
        allow_voice,
        allow_above_160,
        status,
    ):
        self.id=id
        self.username=username
        self.password=password
        self.brandname=brandname
        self.info_route=info_route
        self.allow_voice=allow_voice
        self.allow_above_160=allow_above_160
        self.status=status
class Template():
    def __init__(
        self,
        id,
        template,
        id_brandname,
    ):
        self.id=id
        self.template=template
        self.id_brandname=id_brandname