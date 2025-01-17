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
from aliyunsdksas.endpoint import endpoint_data

class ListInstanceCatalogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ListInstanceCatalog')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Typess(self): # RepeatList
		return self.get_query_params().get('Types')

	def set_Typess(self, Types):  # RepeatList
		for depth1 in range(len(Types)):
			self.add_query_param('Types.' + str(depth1 + 1), Types[depth1])
	def get_StandardIdss(self): # RepeatList
		return self.get_query_params().get('StandardIds')

	def set_StandardIdss(self, StandardIds):  # RepeatList
		for depth1 in range(len(StandardIds)):
			self.add_query_param('StandardIds.' + str(depth1 + 1), StandardIds[depth1])
	def get_RequirementIdss(self): # RepeatList
		return self.get_query_params().get('RequirementIds')

	def set_RequirementIdss(self, RequirementIds):  # RepeatList
		for depth1 in range(len(RequirementIds)):
			self.add_query_param('RequirementIds.' + str(depth1 + 1), RequirementIds[depth1])
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
