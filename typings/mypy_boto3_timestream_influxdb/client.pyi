"""
Type annotations for timestream-influxdb service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_timestream_influxdb.client import TimestreamInfluxDBClient

    session = Session()
    client: TimestreamInfluxDBClient = session.client("timestream-influxdb")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListDbClustersPaginator,
    ListDbInstancesForClusterPaginator,
    ListDbInstancesPaginator,
    ListDbParameterGroupsPaginator,
)
from .type_defs import (
    CreateDbClusterInputTypeDef,
    CreateDbClusterOutputTypeDef,
    CreateDbInstanceInputTypeDef,
    CreateDbInstanceOutputTypeDef,
    CreateDbParameterGroupInputTypeDef,
    CreateDbParameterGroupOutputTypeDef,
    DeleteDbClusterInputTypeDef,
    DeleteDbClusterOutputTypeDef,
    DeleteDbInstanceInputTypeDef,
    DeleteDbInstanceOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    GetDbClusterInputTypeDef,
    GetDbClusterOutputTypeDef,
    GetDbInstanceInputTypeDef,
    GetDbInstanceOutputTypeDef,
    GetDbParameterGroupInputTypeDef,
    GetDbParameterGroupOutputTypeDef,
    ListDbClustersInputTypeDef,
    ListDbClustersOutputTypeDef,
    ListDbInstancesForClusterInputTypeDef,
    ListDbInstancesForClusterOutputTypeDef,
    ListDbInstancesInputTypeDef,
    ListDbInstancesOutputTypeDef,
    ListDbParameterGroupsInputTypeDef,
    ListDbParameterGroupsOutputTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateDbClusterInputTypeDef,
    UpdateDbClusterOutputTypeDef,
    UpdateDbInstanceInputTypeDef,
    UpdateDbInstanceOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("TimestreamInfluxDBClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TimestreamInfluxDBClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#generate_presigned_url)
        """

    def create_db_cluster(
        self, **kwargs: Unpack[CreateDbClusterInputTypeDef]
    ) -> CreateDbClusterOutputTypeDef:
        """
        Creates a new Timestream for InfluxDB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/create_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#create_db_cluster)
        """

    def create_db_instance(
        self, **kwargs: Unpack[CreateDbInstanceInputTypeDef]
    ) -> CreateDbInstanceOutputTypeDef:
        """
        Creates a new Timestream for InfluxDB DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/create_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#create_db_instance)
        """

    def create_db_parameter_group(
        self, **kwargs: Unpack[CreateDbParameterGroupInputTypeDef]
    ) -> CreateDbParameterGroupOutputTypeDef:
        """
        Creates a new Timestream for InfluxDB DB parameter group to associate with DB
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/create_db_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#create_db_parameter_group)
        """

    def delete_db_cluster(
        self, **kwargs: Unpack[DeleteDbClusterInputTypeDef]
    ) -> DeleteDbClusterOutputTypeDef:
        """
        Deletes a Timestream for InfluxDB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/delete_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#delete_db_cluster)
        """

    def delete_db_instance(
        self, **kwargs: Unpack[DeleteDbInstanceInputTypeDef]
    ) -> DeleteDbInstanceOutputTypeDef:
        """
        Deletes a Timestream for InfluxDB DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/delete_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#delete_db_instance)
        """

    def get_db_cluster(
        self, **kwargs: Unpack[GetDbClusterInputTypeDef]
    ) -> GetDbClusterOutputTypeDef:
        """
        Retrieves information about a Timestream for InfluxDB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/get_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#get_db_cluster)
        """

    def get_db_instance(
        self, **kwargs: Unpack[GetDbInstanceInputTypeDef]
    ) -> GetDbInstanceOutputTypeDef:
        """
        Returns a Timestream for InfluxDB DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/get_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#get_db_instance)
        """

    def get_db_parameter_group(
        self, **kwargs: Unpack[GetDbParameterGroupInputTypeDef]
    ) -> GetDbParameterGroupOutputTypeDef:
        """
        Returns a Timestream for InfluxDB DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/get_db_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#get_db_parameter_group)
        """

    def list_db_clusters(
        self, **kwargs: Unpack[ListDbClustersInputTypeDef]
    ) -> ListDbClustersOutputTypeDef:
        """
        Returns a list of Timestream for InfluxDB DB clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/list_db_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#list_db_clusters)
        """

    def list_db_instances(
        self, **kwargs: Unpack[ListDbInstancesInputTypeDef]
    ) -> ListDbInstancesOutputTypeDef:
        """
        Returns a list of Timestream for InfluxDB DB instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/list_db_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#list_db_instances)
        """

    def list_db_instances_for_cluster(
        self, **kwargs: Unpack[ListDbInstancesForClusterInputTypeDef]
    ) -> ListDbInstancesForClusterOutputTypeDef:
        """
        Returns a list of Timestream for InfluxDB clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/list_db_instances_for_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#list_db_instances_for_cluster)
        """

    def list_db_parameter_groups(
        self, **kwargs: Unpack[ListDbParameterGroupsInputTypeDef]
    ) -> ListDbParameterGroupsOutputTypeDef:
        """
        Returns a list of Timestream for InfluxDB DB parameter groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/list_db_parameter_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#list_db_parameter_groups)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        A list of tags applied to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#list_tags_for_resource)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Tags are composed of a Key/Value pairs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the tag from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#untag_resource)
        """

    def update_db_cluster(
        self, **kwargs: Unpack[UpdateDbClusterInputTypeDef]
    ) -> UpdateDbClusterOutputTypeDef:
        """
        Updates a Timestream for InfluxDB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/update_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#update_db_cluster)
        """

    def update_db_instance(
        self, **kwargs: Unpack[UpdateDbInstanceInputTypeDef]
    ) -> UpdateDbInstanceOutputTypeDef:
        """
        Updates a Timestream for InfluxDB DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/update_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#update_db_instance)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_db_clusters"]
    ) -> ListDbClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_db_instances_for_cluster"]
    ) -> ListDbInstancesForClusterPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_db_instances"]
    ) -> ListDbInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_db_parameter_groups"]
    ) -> ListDbParameterGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-influxdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/client/#get_paginator)
        """
