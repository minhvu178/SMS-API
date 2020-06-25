#import block
from flask import Flask, render_template, send_from_directory, request, redirect, session, flash, url_for, jsonify, g
from flask_restful import reqparse, abort, fields, marshal_with, Api, Resource, reqparse
from datetime import datetime
from datetime import timedelta
import dateutil.parser
from flask_restful_swagger import swagger
import functools
import uuid
import simplejson
import argparse
import json
from bson import ObjectId
#import block

#Input block
parser = reqparse.RequestParser()
parser.add_argument('username', required=True, type=str)
parser.add_argument('password', required=True, type=str)

#Input get info WhiteListIP
parser_white_list = reqparse.RequestParser()
parser_white_list.add_argument('username')
parser_white_list.add_argument('password')

#Input get Template SMS
parser_template = reqparse.RequestParser()
parser_template.add_argument('username')
parser_template.add_argument('password')
parser_template.add_argument('template')
parser_template.add_argument('status')

#Input get Quota
parser_quota = reqparse.RequestParser()
parser_quota.add_argument('username')
parser_quota.add_argument('password')
parser_quota.add_argument('message')
parser_quota.add_argument('brandname')
parser_quota.add_argument('recipients')

#Input get Report

@swagger.model
class request_package:
    resource_fields = {
        'username': fields.String,
        'password': fields.String
    }

@swagger.model
class response_package:
  resource_fields = {
      'status': fields.String,
      'message': fields.String
  }


class White_List(Resource):

    @swagger.operation(
        notes='Danh sách các IP được cấp quyền gửi tin nhắn',
        responseClass=response_package.__name__,
        nickname='Get White List IP',
        parameters=[
             {
              "name": "username",
              "description": "Tên người dùng",
              "required": True,
              "allowMultiple": False,
              "dataType": str,
              "paramType": "header"
            }
            {
              "name": "password",
              "description": "Mật khẩu",
              "required": True,
              "allowMultiple": False,
              "dataType": str,
              "paramType": "header"
            }
        ],
        responseMessages=[
            {
              "code": 200,
              "status": "Success",
              "message": "‘result’:[‘x.x.x.x’, ‘y.y.y.y’], ‘total’: aa"
            },
            {
              "code": 400,
              "message": "‘error’: ‘Wrong Username Or Password’"
            }
          ]
        )

        @utilities.authenticate
        # @marshal_with(packages)
        def get(self):

class Template(Resource):
    @swagger.operation(
        notes='Lấy template dành cho SMS',
        responseClass=response_package.__name__,
        nickname='Get Template',
        parameters=[
             {
              "name": "username",
              "description": "Tên người dùng",
              "required": True,
              "allowMultiple": False,
              "dataType": str,
              "paramType": "header"
            }
            {
              "name": "password",
              "description": "Mật khẩu",
              "required": True,
              "allowMultiple": False,
              "dataType": str,
              "paramType": "header"
            }
        ],
        responseMessages=[
            {
              "code": 200,
              "status": "Success",
              "message": "‘result’:[{‘id_temp’:’xxxxx’, ‘template’:’xxxxxx’, ‘status’:’Active / Reject / Pending’}], ‘total’: ‘XX’"
            },
            {
              "code": 400,
              "message": "‘error’:’Mẫu Template không đúng định dạng hoặc chứa dấu tiếng việt’"
            }
            {
              "code": 419,
              "message": "error’: ‘Wrong Username OR Password’"
            }
          ]
        )

    @utilities.authenticate
        # @marshal_with(packages)
        def get(self):

    @swagger.operation(
        notes='Tạo template dành cho SMS',
        responseClass=response_package.__name__,
        nickname='Create Template',
        parameters=[
             {
              "name": "username",
              "description": "Tên người dùng",
              "required": True,
              "allowMultiple": False,
              "dataType": str,
              "paramType": "header"
            }
            {
              "name": "password",
              "description": "Mật khẩu",
              "required": True,
              "allowMultiple": False,
              "dataType": str,
              "paramType": "header"
            }
            {
              "name": "template",
              "description": "Template cần khai báo",
              "required": True,
              "allowMultiple": False,
              "dataType": str,
              "paramType": "header"
            }
        ],
        responseMessages=[
            {
              "code": 200,
              "status": "Success",
              "message": "‘result’: ‘Success’ , ‘status’:’Pending’, ‘template_id’: ‘xxxxxx’, ‘’"
            },
            {
              "code": 400,
              "message": "‘error’:’Mẫu Template không đúng định dạng hoặc chứa dấu tiếng việt’"
            }
            {
              "code": 419,
              "message": "error’: ‘Wrong Username OR Password’"
            }
          ]
        )

    @utilities.authenticate
        # @marshal_with(packages)
        def post(self):

    @swagger.operation(
        notes='Thay đổi template dành cho SMS',
        responseClass=response_package.__name__,
        nickname='Update Template',
        parameters=[
             {
              "name": "username",
              "description": "Tên người dùng",
              "required": True,
              "allowMultiple": False,
              "dataType": request_package.__name__,
              "paramType": "header"
            }
            {
              "name": "password",
              "description": "Mật khẩu",
              "required": True,
              "allowMultiple": False,
              "dataType": request_package.__name__,
              "paramType": "header"
            }
            {
              "name": "template",
              "description": "Template mới muốn chỉnh sửa",
              "required": False,
              "allowMultiple": False,
              "dataType": String,
              "paramType": "header"
            }
            {
              "name": "status",
              "description": "Trạng thái muốn update của template ",
              "required": False,
              "allowMultiple": False,
              "dataType": String,
              "paramType": "header"
            }
        ],
        responseMessages=[
            {
              "code": 200,
              "status": "Success",
              "message": "‘result’: ‘Success’ , ‘status’:’Pending’, ‘template_id’: ‘xxxxxx’, ‘’"
            },
            {
              "code": 400,
              "message": "‘error’:’Mẫu Template không đúng định dạng hoặc chứa dấu tiếng việt’"
            }
            {
              "code": 419,
              "message": "error’: ‘Wrong Username OR Password’"
            }
          ]
        )

    @utilities.authenticate
        # @marshal_with(packages)
        def put(self):
class Quota(Resource):
    @swagger.operation(
        notes='Lấy thông tin quota gửi tin SMS',
        responseClass=response_package.__name__,
        nickname='Get Quota',
        parameters=[
             {
              "name": "username",
              "description": "Tên người dùng",
              "required": True,
              "allowMultiple": False,
              "dataType": request_package.__name__,
              "paramType": "header"
            }
            {
              "name": "password",
              "description": "Mật khẩu",
              "required": True,
              "allowMultiple": False,
              "dataType": request_package.__name__,
              "paramType": "header"
            }
        ],
        responseMessages=[
            {
              "code": 200,
              "status": "Success",
              "message": "‘quota/day’: ’xxxx’ , ‘spend_sms’: ‘xxxx’ "
            },
            {
              "code": 419,
              "message": "error’: ‘Wrong username or Password’"
            }
          ]
        )

class SMS(Resource):
    @swagger.operation(
        notes='Gửi tin SMS',
        responseClass=response_package.__name__,
        nickname='Send SMS',
        parameters=[
             {
              "name": "username",
              "description": "Tên người dùng",
              "required": True,
              "allowMultiple": False,
              "dataType": str,
              "paramType": "header"
            }
            {
              "name": "password",
              "description": "Mật khẩu",
              "required": True,
              "allowMultiple": False,
              "dataType": str,
              "paramType": "header"
            }
            {
              "name": "message",
              "description": "Nội dung tin nhắn",
              "required": True,
              "allowMultiple": False,
              "dataType": str,
              "paramType": "header"
            }
            {
              "name": "brandname",
              "description": "Mật khẩu",
              "required": True,
              "allowMultiple": False,
              "dataType": str,
              "paramType": "header"
            }
            {
              "name": "recipients",
              "description": "Danh sách các số điện thoại , mỗi số điện thoại sẽ tự sinh message_id",
              "required": True,
              "allowMultiple": False,
              "dataType": List[{"message_id":message_id,"number":number}, {"message_id":message_id1,"number":number1}]],
              "paramType": "header"
            }
        ],
        responseMessages=[
            {
              "code": 200,
              "status": "Success",
              "message": "‘quota/day’: ’xxxx’ , ‘spend_sms’: ‘xxxx’ "
            },
          ]
        )

class Report(Resource):