"""
Type annotations for mediastore service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediastore.client import MediaStoreClient

    session = Session()
    client: MediaStoreClient = session.client("mediastore")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListContainersPaginator
from .type_defs import (
    CreateContainerInputTypeDef,
    CreateContainerOutputTypeDef,
    DeleteContainerInputTypeDef,
    DeleteContainerPolicyInputTypeDef,
    DeleteCorsPolicyInputTypeDef,
    DeleteLifecyclePolicyInputTypeDef,
    DeleteMetricPolicyInputTypeDef,
    DescribeContainerInputTypeDef,
    DescribeContainerOutputTypeDef,
    GetContainerPolicyInputTypeDef,
    GetContainerPolicyOutputTypeDef,
    GetCorsPolicyInputTypeDef,
    GetCorsPolicyOutputTypeDef,
    GetLifecyclePolicyInputTypeDef,
    GetLifecyclePolicyOutputTypeDef,
    GetMetricPolicyInputTypeDef,
    GetMetricPolicyOutputTypeDef,
    ListContainersInputTypeDef,
    ListContainersOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PutContainerPolicyInputTypeDef,
    PutCorsPolicyInputTypeDef,
    PutLifecyclePolicyInputTypeDef,
    PutMetricPolicyInputTypeDef,
    StartAccessLoggingInputTypeDef,
    StopAccessLoggingInputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("MediaStoreClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ContainerInUseException: Type[BotocoreClientError]
    ContainerNotFoundException: Type[BotocoreClientError]
    CorsPolicyNotFoundException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PolicyNotFoundException: Type[BotocoreClientError]

class MediaStoreClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaStoreClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#generate_presigned_url)
        """

    def create_container(
        self, **kwargs: Unpack[CreateContainerInputTypeDef]
    ) -> CreateContainerOutputTypeDef:
        """
        Creates a storage container to hold objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/create_container.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#create_container)
        """

    def delete_container(self, **kwargs: Unpack[DeleteContainerInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/delete_container.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#delete_container)
        """

    def delete_container_policy(
        self, **kwargs: Unpack[DeleteContainerPolicyInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the access policy that is associated with the specified container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/delete_container_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#delete_container_policy)
        """

    def delete_cors_policy(self, **kwargs: Unpack[DeleteCorsPolicyInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the cross-origin resource sharing (CORS) configuration information that
        is set for the container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/delete_cors_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#delete_cors_policy)
        """

    def delete_lifecycle_policy(
        self, **kwargs: Unpack[DeleteLifecyclePolicyInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes an object lifecycle policy from a container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/delete_lifecycle_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#delete_lifecycle_policy)
        """

    def delete_metric_policy(
        self, **kwargs: Unpack[DeleteMetricPolicyInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the metric policy that is associated with the specified container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/delete_metric_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#delete_metric_policy)
        """

    def describe_container(
        self, **kwargs: Unpack[DescribeContainerInputTypeDef]
    ) -> DescribeContainerOutputTypeDef:
        """
        Retrieves the properties of the requested container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/describe_container.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#describe_container)
        """

    def get_container_policy(
        self, **kwargs: Unpack[GetContainerPolicyInputTypeDef]
    ) -> GetContainerPolicyOutputTypeDef:
        """
        Retrieves the access policy for the specified container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/get_container_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#get_container_policy)
        """

    def get_cors_policy(
        self, **kwargs: Unpack[GetCorsPolicyInputTypeDef]
    ) -> GetCorsPolicyOutputTypeDef:
        """
        Returns the cross-origin resource sharing (CORS) configuration information that
        is set for the container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/get_cors_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#get_cors_policy)
        """

    def get_lifecycle_policy(
        self, **kwargs: Unpack[GetLifecyclePolicyInputTypeDef]
    ) -> GetLifecyclePolicyOutputTypeDef:
        """
        Retrieves the object lifecycle policy that is assigned to a container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/get_lifecycle_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#get_lifecycle_policy)
        """

    def get_metric_policy(
        self, **kwargs: Unpack[GetMetricPolicyInputTypeDef]
    ) -> GetMetricPolicyOutputTypeDef:
        """
        Returns the metric policy for the specified container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/get_metric_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#get_metric_policy)
        """

    def list_containers(
        self, **kwargs: Unpack[ListContainersInputTypeDef]
    ) -> ListContainersOutputTypeDef:
        """
        Lists the properties of all containers in AWS Elemental MediaStore.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/list_containers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#list_containers)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Returns a list of the tags assigned to the specified container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#list_tags_for_resource)
        """

    def put_container_policy(
        self, **kwargs: Unpack[PutContainerPolicyInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates an access policy for the specified container to restrict the users and
        clients that can access it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/put_container_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#put_container_policy)
        """

    def put_cors_policy(self, **kwargs: Unpack[PutCorsPolicyInputTypeDef]) -> Dict[str, Any]:
        """
        Sets the cross-origin resource sharing (CORS) configuration on a container so
        that the container can service cross-origin requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/put_cors_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#put_cors_policy)
        """

    def put_lifecycle_policy(
        self, **kwargs: Unpack[PutLifecyclePolicyInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Writes an object lifecycle policy to a container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/put_lifecycle_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#put_lifecycle_policy)
        """

    def put_metric_policy(self, **kwargs: Unpack[PutMetricPolicyInputTypeDef]) -> Dict[str, Any]:
        """
        The metric policy that you want to add to the container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/put_metric_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#put_metric_policy)
        """

    def start_access_logging(
        self, **kwargs: Unpack[StartAccessLoggingInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Starts access logging on the specified container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/start_access_logging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#start_access_logging)
        """

    def stop_access_logging(
        self, **kwargs: Unpack[StopAccessLoggingInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops access logging on the specified container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/stop_access_logging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#stop_access_logging)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to the specified AWS Elemental MediaStore container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from the specified container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#untag_resource)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_containers"]
    ) -> ListContainersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client/#get_paginator)
        """
