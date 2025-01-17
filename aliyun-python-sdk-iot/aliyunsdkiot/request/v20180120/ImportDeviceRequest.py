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
from aliyunsdkiot.endpoint import endpoint_data

class ImportDeviceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'ImportDevice')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_Nickname(self):
		return self.get_query_params().get('Nickname')

	def set_Nickname(self,Nickname):
		self.add_query_param('Nickname',Nickname)

	def get_Sn(self):
		return self.get_query_params().get('Sn')

	def set_Sn(self,Sn):
		self.add_query_param('Sn',Sn)

	def get_DeviceSecret(self):
		return self.get_query_params().get('DeviceSecret')

	def set_DeviceSecret(self,DeviceSecret):
		self.add_query_param('DeviceSecret',DeviceSecret)

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_DeviceName(self):
		return self.get_query_params().get('DeviceName')

	def set_DeviceName(self,DeviceName):
		self.add_query_param('DeviceName',DeviceName)