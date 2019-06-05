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

import requests

from sandbox import IDEMPIERE_URL, IDEMPIERE_SSL_URL

requests.packages.urllib3.disable_warnings()

url = IDEMPIERE_URL + '/ADInterface/services/ModelADService'
urls = IDEMPIERE_SSL_URL + '/ADInterface/services/ModelADService'
headers = {'user-agent': 'my-app/0.0.1', 'content-type': 'text/xml; charset=UTF-8'}


def test_xml():
    xml = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:_0="http://idempiere.org/ADInterface/1_0">'
    xml += '<soapenv:Header/>'
    xml += '<soapenv:Body>'
    xml += '<_0:queryData>'
    xml += '<_0:ModelCRUDRequest>'
    xml += '<_0:ModelCRUD>'
    xml += '<_0:serviceType>QueryBPartnerTest</_0:serviceType>'
    xml += '</_0:ModelCRUD>'
    xml += '<_0:ADLoginRequest>'
    xml += '<_0:user>SuperUser</_0:user>'
    xml += '<_0:pass>System</_0:pass>'
    xml += '<_0:ClientID>11</_0:ClientID>'
    xml += '<_0:RoleID>102</_0:RoleID>'
    xml += '</_0:ADLoginRequest>'
    xml += '</_0:ModelCRUDRequest>'
    xml += '</_0:queryData>'
    xml += '</soapenv:Body>'
    xml += '</soapenv:Envelope>'
    return xml


def test_xml_file():
    test_file = open('../documents/CreateBPartnerTest_request.xml', 'r')
    return test_file.read()


request = test_xml()
print('Request:' + request)

# timeout on seconds
try:
    r = requests.post(url, data=request, headers=headers, verify=False, timeout=2)
except Exception as e:
    print(e)
else:
    print('Status:' + str(r.status_code))
    print('Headers:' + str(r.headers))
    print('Response:' + str(r.text))
