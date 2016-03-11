# -*- encoding: utf-8 -*-
"""
Copyright (c) 2016 Saúl Piña <sauljabin@gmail.com>.

This file is part of idempierewsc.

idempierewsc is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

idempierewsc is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with idempierewsc.  If not, see <http://www.gnu.org/licenses/>.
"""

import idempierewsc.base
import idempierewsc.enums
import datetime
import lxml.etree


class CompositeOperationRequest(idempierewsc.base.CompositeRequest):
    """
    iDempiere Web Service Composite
    """

    def __init__(self):
        super(CompositeOperationRequest, self).__init__()

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.CompositeResponse

    def web_service_method(self):
        return idempierewsc.enums.WebServiceMethod.compositeOperation

    def web_service_definition(self):
        return idempierewsc.enums.WebServiceDefinition.compositeInterface


class CreateDataRequest(idempierewsc.base.ModelCRUDRequest):
    """
    iDempiere Web Service CreateData
    """

    def __init__(self):
        super(CreateDataRequest, self).__init__()

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.StandardResponse

    def web_service_method(self):
        return idempierewsc.enums.WebServiceMethod.createData

    def web_service_definition(self):
        return idempierewsc.enums.WebServiceDefinition.ModelADService


class CreateUpdateDataRequest(idempierewsc.base.ModelCRUDRequest):
    """
    iDempiere Web Service CreateUpdateData
    """

    def __init__(self):
        super(CreateUpdateDataRequest, self).__init__()

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.StandardResponse

    def web_service_method(self):
        return idempierewsc.enums.WebServiceMethod.createUpdateData

    def web_service_definition(self):
        return idempierewsc.enums.WebServiceDefinition.ModelADService


class DeleteDataRequest(idempierewsc.base.ModelCRUDRequest):
    """
    iDempiere Web Service DeleteDataRequest
    """

    def __init__(self):
        super(DeleteDataRequest, self).__init__()

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.StandardResponse

    def web_service_method(self):
        return idempierewsc.enums.WebServiceMethod.deleteData

    def web_service_definition(self):
        return idempierewsc.enums.WebServiceDefinition.ModelADService


class UpdateDataRequest(idempierewsc.base.ModelCRUDRequest):
    """
    iDempiere Web Service UpdateDataRequest
    """

    def __init__(self):
        super(UpdateDataRequest, self).__init__()

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.StandardResponse

    def web_service_method(self):
        return idempierewsc.enums.WebServiceMethod.updateData

    def web_service_definition(self):
        return idempierewsc.enums.WebServiceDefinition.ModelADService


class ReadDataRequest(idempierewsc.base.ModelCRUDRequest):
    """
    iDempiere Web Service ReadDataRequest
    """

    def __init__(self):
        super(ReadDataRequest, self).__init__()

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.WindowTabDataResponse

    def web_service_method(self):
        return idempierewsc.enums.WebServiceMethod.readData

    def web_service_definition(self):
        return idempierewsc.enums.WebServiceDefinition.ModelADService


class QueryDataRequest(idempierewsc.base.ModelCRUDRequest):
    """
    iDempiere Web Service QueryDataRequest
    """

    def __init__(self):
        super(QueryDataRequest, self).__init__()

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.WindowTabDataResponse

    def web_service_method(self):
        return idempierewsc.enums.WebServiceMethod.queryData

    def web_service_definition(self):
        return idempierewsc.enums.WebServiceDefinition.ModelADService


class GetListRequest(idempierewsc.base.ModelGetListRequest):
    """
    iDempiere Web Service GetListRequest
    """

    def __init__(self):
        super(GetListRequest, self).__init__()

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.WindowTabDataResponse

    def web_service_method(self):
        return idempierewsc.enums.WebServiceMethod.getList

    def web_service_definition(self):
        return idempierewsc.enums.WebServiceDefinition.ModelADService


class RunProcessRequest(idempierewsc.base.ModelRunProcessRequest):
    """
    iDempiere Web Service RunProcessRequest
    """

    def __init__(self):
        super(RunProcessRequest, self).__init__()

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.RunProcessResponse

    def web_service_method(self):
        return idempierewsc.enums.WebServiceMethod.runProcess

    def web_service_definition(self):
        return idempierewsc.enums.WebServiceDefinition.ModelADService


class SetDocActionRequest(idempierewsc.base.ModelSetDocActionRequest):
    """
    iDempiere Web Service SetDocActionRequest
    """

    def __init__(self):
        super(SetDocActionRequest, self).__init__()

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.StandardResponse

    def web_service_method(self):
        return idempierewsc.enums.WebServiceMethod.setDocAction

    def web_service_definition(self):
        return idempierewsc.enums.WebServiceDefinition.ModelADService


class RequestFactory(object):
    """
    RequestFactory. Class for build de Web Service Xml Document
    """
    PREFIX_0 = "_0"
    NAMESPACE_0 = "http://idempiere.org/ADInterface/1_0"
    PREFIX_SOAPENV = "soapenv"
    NAMESPACE_SOAPENV = "http://schemas.xmlsoap.org/soap/envelope/"
    ATTRIBUTE_XMLNS = "xmlns"
    NAMESPACE_XMLNS = "http://www.w3.org/2000/xmlns/"
    NSMAP = {PREFIX_0: NAMESPACE_0, PREFIX_SOAPENV: NAMESPACE_SOAPENV}

    def create_element_0(self, name, text=None):
        element = lxml.etree.Element('{%s}%s' % (self.NAMESPACE_0, name))
        if text:
            element.text = str(text)
        return element

    def create_element_soapenv(self, name, text=None):
        element = lxml.etree.Element('{%s}%s' % (self.NAMESPACE_SOAPENV, name))
        if text:
            element.text = str(text)
        return element

    def create_request(self, wsr):
        return self.build_document(wsr)

    def build_document(self, wsr):
        doc = lxml.etree.Element('{%s}%s' % (self.NAMESPACE_SOAPENV, 'Envelope'), nsmap=self.NSMAP)
        doc.append(self.create_element_soapenv('Header'))
        node_body = self.create_element_soapenv('Body')
        node_request = self.create_element_0(wsr.web_service_method().value)
        node_request.append(self.build_request(wsr))
        node_body.append(node_request)
        doc.append(node_body)
        return doc

    def build_request(self, wsr):
        request = self.create_element_0(wsr.web_service_request_model().value)

        if wsr.web_service_request_model() == idempierewsc.enums.WebServiceRequestModel.CompositeRequest:
            request.append(self.create_element_0('serviceType', wsr.web_service_type))

        request.append(self.build_model(wsr))

        if wsr.login:
            request.append(self.build_login(wsr.login))
        return request

    def build_login(self, log):
        login = self.create_element_0('ADLoginRequest')

        if log.user:
            login.append(self.create_element_0('user', log.user))

        if log.password:
            login.append(self.create_element_0('pass', log.password))

        if log.lang:
            if isinstance(log.lang, idempierewsc.enums.Language):
                temp_lang = log.lang.value
            else:
                temp_lang = log.lang
            login.append(self.create_element_0('lang', temp_lang))

        if log.client_id:
            login.append(self.create_element_0('ClientID', log.client_id))

        if log.role_id:
            login.append(self.create_element_0('RoleID', log.role_id))

        if log.org_id:
            login.append(self.create_element_0('OrgID', log.org_id))

        if log.warehouse_id:
            login.append(self.create_element_0('WarehouseID', log.warehouse_id))

        if log.stage:
            login.append(self.create_element_0('stage', log.stage))

        return login

    def build_model(self, wsr):
        if wsr.web_service_request_model() == idempierewsc.enums.WebServiceRequestModel.CompositeRequest:
            model = self.create_element_0('operations')
            if wsr.operations:
                for i in wsr.operations:
                    model.append(self.build_operation(i))
            return model
        elif wsr.web_service_request_model() == idempierewsc.enums.WebServiceRequestModel.ModelCRUDRequest:
            model = self.create_element_0('ModelCRUD')
            model.append(self.create_element_0('serviceType', wsr.web_service_type))

            if wsr.table_name:
                model.append(self.create_element_0('TableName', wsr.table_name))

            if wsr.record_id:
                model.append(self.create_element_0('RecordID', wsr.record_id))

            if wsr.record_id_variable:
                model.append(self.create_element_0('recordIDVariable', wsr.record_id_variable))

            if wsr.action:
                model.append(self.create_element_0('Action', wsr.action))

            if wsr.filter:
                model.append(self.create_element_0('Filter', wsr.filter))

            if wsr.limit:
                model.append(self.create_element_0('Limit', wsr.limit))

            if wsr.offset:
                model.append(self.create_element_0('Offset', wsr.offset))

            if wsr.data_row:
                model.append(self.build_data_row(wsr.data_row))

            return model
        elif wsr.web_service_request_model() == idempierewsc.enums.WebServiceRequestModel.ModelGetListRequest:
            model = self.create_element_0('ModelGetList')
            model.append(self.create_element_0('serviceType', wsr.web_service_type))

            if wsr.filter:
                model.append(self.create_element_0('Filter', wsr.filter))

            if wsr.ad_reference_id:
                model.append(self.create_element_0('AD_Reference_ID', wsr.ad_reference_id))

            return model
        elif wsr.web_service_request_model() == idempierewsc.enums.WebServiceRequestModel.ModelRunProcessRequest:
            model = self.create_element_0('ModelRunProcess')
            model.append(self.create_element_0('serviceType', wsr.web_service_type))

            if wsr.ad_process_id:
                model.set('AD_Process_ID', wsr.ad_process_id)

            if wsr.ad_menu_id:
                model.set('AD_Menu_ID', wsr.ad_menu_id)

            if wsr.ad_record_id:
                model.set('AD_Record_ID', wsr.ad_record_id)

            if wsr.doc_action:
                model.set('DocAction', wsr.doc_action)

            if wsr.param_values:
                model.append(self.build_param_values(wsr.param_values))

            return model
        elif wsr.web_service_request_model() == idempierewsc.enums.WebServiceRequestModel.ModelSetDocActionRequest:
            model = self.create_element_0('ModelSetDocAction')
            model.append(self.create_element_0('serviceType', wsr.web_service_type))

            if wsr.table_name:
                model.append(self.create_element_0('tableName', wsr.table_name))

            if wsr.record_id:
                model.append(self.create_element_0('recordID', wsr.record_id))

            if wsr.record_id_variable:
                model.append(self.create_element_0('recordIDVariable', wsr.record_id_variable))

            if wsr.doc_action:
                if isinstance(wsr.doc_action, idempierewsc.enums.DocAction):
                    model.append(self.create_element_0('docAction', str(wsr.doc_action.value)))
                else:
                    model.append(self.create_element_0('docAction', str(wsr.doc_action)))

            return model
        return self.create_element_0('NoModel')

    def build_operation(self, oper):
        operation = self.create_element_0('operation')
        operation.set('preCommit', str(oper.pre_commit).lower())
        operation.set('postCommit', str(oper.post_commit).lower())
        operation.append(self.create_element_0('TargetPort', oper.web_service.web_service_method().value))
        operation.append(self.build_model(oper.web_service))
        return operation

    def build_data_row(self, row):
        data_row = self.create_element_0('DataRow')
        for i in row:
            data_row.append(self.build_field(i))
        return data_row

    def build_param_values(self, params):
        param_values = self.create_element_0('ParamValues')
        for i in params:
            param_values.append(self.build_field(i))
        return param_values

    def build_field(self, f):
        field = self.create_element_0('field')

        if f.column:
            field.set('column', f.column)

        if f.type:
            field.set('type', f.type)

        if f.lval:
            field.set('lval', f.lval)

        if f.disp is not None:
            field.set('disp', f.disp)

        if f.edit is not None:
            field.set('edit', f.edit)

        if f.error is not None:
            field.set('error', f.error)

        if f.error_val:
            field.set('errorVal', f.error_val)

        if f.value:
            value = f.value
            temp_value = ''
            if isinstance(value, bool):
                temp_value = 'Y' if value else 'N'
            elif isinstance(value, datetime.datetime):
                temp_value = datetime.datetime.strftime(value, '%Y-%m-%d %H:%M:%S')
            elif isinstance(value, idempierewsc.enums.DocAction):
                temp_value = value.value
            elif isinstance(value, idempierewsc.enums.DocStatus):
                temp_value = value.value
            else:
                temp_value = str(value).decode('utf-8')

            field.append(self.create_element_0('val', temp_value))

        return field
