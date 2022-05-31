# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkcloudesl.endpoint import endpoint_data

class DescribeTemplateByModelRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2020-02-01', 'DescribeTemplateByModel')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_EslSize(self):
		return self.get_body_params().get('EslSize')

	def set_EslSize(self,EslSize):
		self.add_body_params('EslSize', EslSize)

	def get_DeviceType(self):
		return self.get_body_params().get('DeviceType')

	def set_DeviceType(self,DeviceType):
		self.add_body_params('DeviceType', DeviceType)

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_TemplateVersion(self):
		return self.get_body_params().get('TemplateVersion')

	def set_TemplateVersion(self,TemplateVersion):
		self.add_body_params('TemplateVersion', TemplateVersion)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)