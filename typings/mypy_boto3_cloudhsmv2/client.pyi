"""
Type annotations for cloudhsmv2 service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudhsmv2.client import CloudHSMV2Client

    session = Session()
    client: CloudHSMV2Client = session.client("cloudhsmv2")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import DescribeBackupsPaginator, DescribeClustersPaginator, ListTagsPaginator
from .type_defs import (
    CopyBackupToRegionRequestTypeDef,
    CopyBackupToRegionResponseTypeDef,
    CreateClusterRequestTypeDef,
    CreateClusterResponseTypeDef,
    CreateHsmRequestTypeDef,
    CreateHsmResponseTypeDef,
    DeleteBackupRequestTypeDef,
    DeleteBackupResponseTypeDef,
    DeleteClusterRequestTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteHsmRequestTypeDef,
    DeleteHsmResponseTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DeleteResourcePolicyResponseTypeDef,
    DescribeBackupsRequestTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeClustersRequestTypeDef,
    DescribeClustersResponseTypeDef,
    GetResourcePolicyRequestTypeDef,
    GetResourcePolicyResponseTypeDef,
    InitializeClusterRequestTypeDef,
    InitializeClusterResponseTypeDef,
    ListTagsRequestTypeDef,
    ListTagsResponseTypeDef,
    ModifyBackupAttributesRequestTypeDef,
    ModifyBackupAttributesResponseTypeDef,
    ModifyClusterRequestTypeDef,
    ModifyClusterResponseTypeDef,
    PutResourcePolicyRequestTypeDef,
    PutResourcePolicyResponseTypeDef,
    RestoreBackupRequestTypeDef,
    RestoreBackupResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
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

__all__ = ("CloudHSMV2Client",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    CloudHsmAccessDeniedException: Type[BotocoreClientError]
    CloudHsmInternalFailureException: Type[BotocoreClientError]
    CloudHsmInvalidRequestException: Type[BotocoreClientError]
    CloudHsmResourceLimitExceededException: Type[BotocoreClientError]
    CloudHsmResourceNotFoundException: Type[BotocoreClientError]
    CloudHsmServiceException: Type[BotocoreClientError]
    CloudHsmTagException: Type[BotocoreClientError]

class CloudHSMV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudHSMV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#generate_presigned_url)
        """

    def copy_backup_to_region(
        self, **kwargs: Unpack[CopyBackupToRegionRequestTypeDef]
    ) -> CopyBackupToRegionResponseTypeDef:
        """
        Copy an CloudHSM cluster backup to a different region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/copy_backup_to_region.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#copy_backup_to_region)
        """

    def create_cluster(
        self, **kwargs: Unpack[CreateClusterRequestTypeDef]
    ) -> CreateClusterResponseTypeDef:
        """
        Creates a new CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/create_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#create_cluster)
        """

    def create_hsm(self, **kwargs: Unpack[CreateHsmRequestTypeDef]) -> CreateHsmResponseTypeDef:
        """
        Creates a new hardware security module (HSM) in the specified CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/create_hsm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#create_hsm)
        """

    def delete_backup(
        self, **kwargs: Unpack[DeleteBackupRequestTypeDef]
    ) -> DeleteBackupResponseTypeDef:
        """
        Deletes a specified CloudHSM backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/delete_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#delete_backup)
        """

    def delete_cluster(
        self, **kwargs: Unpack[DeleteClusterRequestTypeDef]
    ) -> DeleteClusterResponseTypeDef:
        """
        Deletes the specified CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/delete_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#delete_cluster)
        """

    def delete_hsm(self, **kwargs: Unpack[DeleteHsmRequestTypeDef]) -> DeleteHsmResponseTypeDef:
        """
        Deletes the specified HSM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/delete_hsm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#delete_hsm)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> DeleteResourcePolicyResponseTypeDef:
        """
        Deletes an CloudHSM resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#delete_resource_policy)
        """

    def describe_backups(
        self, **kwargs: Unpack[DescribeBackupsRequestTypeDef]
    ) -> DescribeBackupsResponseTypeDef:
        """
        Gets information about backups of CloudHSM clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/describe_backups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#describe_backups)
        """

    def describe_clusters(
        self, **kwargs: Unpack[DescribeClustersRequestTypeDef]
    ) -> DescribeClustersResponseTypeDef:
        """
        Gets information about CloudHSM clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/describe_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#describe_clusters)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestTypeDef]
    ) -> GetResourcePolicyResponseTypeDef:
        """
        Retrieves the resource policy document attached to a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#get_resource_policy)
        """

    def initialize_cluster(
        self, **kwargs: Unpack[InitializeClusterRequestTypeDef]
    ) -> InitializeClusterResponseTypeDef:
        """
        Claims an CloudHSM cluster by submitting the cluster certificate issued by your
        issuing certificate authority (CA) and the CA's root certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/initialize_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#initialize_cluster)
        """

    def list_tags(self, **kwargs: Unpack[ListTagsRequestTypeDef]) -> ListTagsResponseTypeDef:
        """
        Gets a list of tags for the specified CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/list_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#list_tags)
        """

    def modify_backup_attributes(
        self, **kwargs: Unpack[ModifyBackupAttributesRequestTypeDef]
    ) -> ModifyBackupAttributesResponseTypeDef:
        """
        Modifies attributes for CloudHSM backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/modify_backup_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#modify_backup_attributes)
        """

    def modify_cluster(
        self, **kwargs: Unpack[ModifyClusterRequestTypeDef]
    ) -> ModifyClusterResponseTypeDef:
        """
        Modifies CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/modify_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#modify_cluster)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Creates or updates an CloudHSM resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#put_resource_policy)
        """

    def restore_backup(
        self, **kwargs: Unpack[RestoreBackupRequestTypeDef]
    ) -> RestoreBackupResponseTypeDef:
        """
        Restores a specified CloudHSM backup that is in the
        <code>PENDING_DELETION</code> state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/restore_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#restore_backup)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or overwrites one or more tags for the specified CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tag or tags from the specified CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_clusters"]
    ) -> DescribeClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags"]
    ) -> ListTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#get_paginator)
        """
