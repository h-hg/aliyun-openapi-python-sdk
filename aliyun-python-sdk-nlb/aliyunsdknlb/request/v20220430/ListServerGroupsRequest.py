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
from aliyunsdknlb.endpoint import endpoint_data

class ListServerGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Nlb', '2022-04-30', 'ListServerGroups','nlb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ServerGroupNamess(self): # RepeatList
		return self.get_body_params().get('ServerGroupNames')

	def set_ServerGroupNamess(self, ServerGroupNames):  # RepeatList
		for depth1 in range(len(ServerGroupNames)):
			self.add_body_params('ServerGroupNames.' + str(depth1 + 1), ServerGroupNames[depth1])
	def get_ResourceGroupId(self): # String
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_Tag(self): # Array
		return self.get_query_params().get('Tag')

	def set_Tag(self, Tag):  # Array
		for index1, value1 in enumerate(Tag):
			if value1.get('Key') is not None:
				self.add_query_param('Tag.' + str(index1 + 1) + '.Key', value1.get('Key'))
			if value1.get('Value') is not None:
				self.add_query_param('Tag.' + str(index1 + 1) + '.Value', value1.get('Value'))
	def get_ServerGroupIdss(self): # RepeatList
		return self.get_body_params().get('ServerGroupIds')

	def set_ServerGroupIdss(self, ServerGroupIds):  # RepeatList
		for depth1 in range(len(ServerGroupIds)):
			self.add_body_params('ServerGroupIds.' + str(depth1 + 1), ServerGroupIds[depth1])
	def get_ServerGroupType(self): # String
		return self.get_body_params().get('ServerGroupType')

	def set_ServerGroupType(self, ServerGroupType):  # String
		self.add_body_params('ServerGroupType', ServerGroupType)
	def get_VpcId(self): # String
		return self.get_body_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_body_params('VpcId', VpcId)
	def get_MaxResults(self): # Integer
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_body_params('MaxResults', MaxResults)
