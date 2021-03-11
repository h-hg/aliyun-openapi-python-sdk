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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class SearchTableRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'SearchTable')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ReturnGuid(self): # Boolean
		return self.get_query_params().get('ReturnGuid')

	def set_ReturnGuid(self, ReturnGuid):  # Boolean
		self.add_query_param('ReturnGuid', ReturnGuid)
	def get_SearchKey(self): # String
		return self.get_query_params().get('SearchKey')

	def set_SearchKey(self, SearchKey):  # String
		self.add_query_param('SearchKey', SearchKey)
	def get_SearchRange(self): # String
		return self.get_query_params().get('SearchRange')

	def set_SearchRange(self, SearchRange):  # String
		self.add_query_param('SearchRange', SearchRange)
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_SearchTarget(self): # String
		return self.get_query_params().get('SearchTarget')

	def set_SearchTarget(self, SearchTarget):  # String
		self.add_query_param('SearchTarget', SearchTarget)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_EnvType(self): # String
		return self.get_query_params().get('EnvType')

	def set_EnvType(self, EnvType):  # String
		self.add_query_param('EnvType', EnvType)
	def get_DbType(self): # String
		return self.get_query_params().get('DbType')

	def set_DbType(self, DbType):  # String
		self.add_query_param('DbType', DbType)
