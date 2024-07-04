"""
Type annotations for timestream-influxdb service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_timestream_influxdb import TimestreamInfluxDBClient

    client: TimestreamInfluxDBClient = boto3.client("timestream-influxdb")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import DbInstanceTypeType, DbStorageTypeType, DeploymentTypeType
from .paginator import ListDbInstancesPaginator, ListDbParameterGroupsPaginator
from .type_defs import (
    CreateDbInstanceOutputTypeDef,
    CreateDbParameterGroupOutputTypeDef,
    DeleteDbInstanceOutputTypeDef,
    GetDbInstanceOutputTypeDef,
    GetDbParameterGroupOutputTypeDef,
    ListDbInstancesOutputTypeDef,
    ListDbParameterGroupsOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    LogDeliveryConfigurationTypeDef,
    ParametersTypeDef,
    UpdateDbInstanceOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("TimestreamInfluxDBClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class TimestreamInfluxDBClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TimestreamInfluxDBClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#close)
        """

    def create_db_instance(
        self,
        *,
        name: str,
        password: str,
        dbInstanceType: DbInstanceTypeType,
        vpcSubnetIds: List[str],
        vpcSecurityGroupIds: List[str],
        allocatedStorage: int,
        username: str = None,
        organization: str = None,
        bucket: str = None,
        publiclyAccessible: bool = None,
        dbStorageType: DbStorageTypeType = None,
        dbParameterGroupIdentifier: str = None,
        deploymentType: DeploymentTypeType = None,
        logDeliveryConfiguration: "LogDeliveryConfigurationTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateDbInstanceOutputTypeDef:
        """
        Creates a new Timestream for InfluxDB DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.create_db_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#create_db_instance)
        """

    def create_db_parameter_group(
        self,
        *,
        name: str,
        description: str = None,
        parameters: "ParametersTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateDbParameterGroupOutputTypeDef:
        """
        Creates a new Timestream for InfluxDB DB parameter group to associate with DB
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.create_db_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#create_db_parameter_group)
        """

    def delete_db_instance(self, *, identifier: str) -> DeleteDbInstanceOutputTypeDef:
        """
        Deletes a Timestream for InfluxDB DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.delete_db_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#delete_db_instance)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#generate_presigned_url)
        """

    def get_db_instance(self, *, identifier: str) -> GetDbInstanceOutputTypeDef:
        """
        Returns a Timestream for InfluxDB DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.get_db_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#get_db_instance)
        """

    def get_db_parameter_group(self, *, identifier: str) -> GetDbParameterGroupOutputTypeDef:
        """
        Returns a Timestream for InfluxDB DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.get_db_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#get_db_parameter_group)
        """

    def list_db_instances(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListDbInstancesOutputTypeDef:
        """
        Returns a list of Timestream for InfluxDB DB instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.list_db_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#list_db_instances)
        """

    def list_db_parameter_groups(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListDbParameterGroupsOutputTypeDef:
        """
        Returns a list of Timestream for InfluxDB DB parameter groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.list_db_parameter_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#list_db_parameter_groups)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        A list of tags applied to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        Tags are composed of a Key/Value pairs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> None:
        """
        Removes the tag from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#untag_resource)
        """

    def update_db_instance(
        self,
        *,
        identifier: str,
        logDeliveryConfiguration: "LogDeliveryConfigurationTypeDef" = None,
        dbParameterGroupIdentifier: str = None
    ) -> UpdateDbInstanceOutputTypeDef:
        """
        Updates a Timestream for InfluxDB DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client.update_db_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client.html#update_db_instance)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_db_instances"]
    ) -> ListDbInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Paginator.ListDbInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators.html#listdbinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_db_parameter_groups"]
    ) -> ListDbParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Paginator.ListDbParameterGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators.html#listdbparametergroupspaginator)
        """
