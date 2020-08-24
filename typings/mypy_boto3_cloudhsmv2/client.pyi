# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for cloudhsmv2 service client

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudhsmv2 import CloudHSMV2Client

    client: CloudHSMV2Client = boto3.client("cloudhsmv2")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_cloudhsmv2.paginator import (
    DescribeBackupsPaginator,
    DescribeClustersPaginator,
    ListTagsPaginator,
)
from mypy_boto3_cloudhsmv2.type_defs import (
    CopyBackupToRegionResponseTypeDef,
    CreateClusterResponseTypeDef,
    CreateHsmResponseTypeDef,
    DeleteBackupResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteHsmResponseTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeClustersResponseTypeDef,
    InitializeClusterResponseTypeDef,
    ListTagsResponseTypeDef,
    RestoreBackupResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudHSMV2Client",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    CloudHsmAccessDeniedException: Type[Boto3ClientError]
    CloudHsmInternalFailureException: Type[Boto3ClientError]
    CloudHsmInvalidRequestException: Type[Boto3ClientError]
    CloudHsmResourceNotFoundException: Type[Boto3ClientError]
    CloudHsmServiceException: Type[Boto3ClientError]
    CloudHsmTagException: Type[Boto3ClientError]


class CloudHSMV2Client:
    """
    [CloudHSMV2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.can_paginate)
        """

    def copy_backup_to_region(
        self, DestinationRegion: str, BackupId: str, TagList: List["TagTypeDef"] = None
    ) -> CopyBackupToRegionResponseTypeDef:
        """
        [Client.copy_backup_to_region documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.copy_backup_to_region)
        """

    def create_cluster(
        self,
        SubnetIds: List[str],
        HsmType: str,
        SourceBackupId: str = None,
        TagList: List["TagTypeDef"] = None,
    ) -> CreateClusterResponseTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.create_cluster)
        """

    def create_hsm(
        self, ClusterId: str, AvailabilityZone: str, IpAddress: str = None
    ) -> CreateHsmResponseTypeDef:
        """
        [Client.create_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.create_hsm)
        """

    def delete_backup(self, BackupId: str) -> DeleteBackupResponseTypeDef:
        """
        [Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_backup)
        """

    def delete_cluster(self, ClusterId: str) -> DeleteClusterResponseTypeDef:
        """
        [Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_cluster)
        """

    def delete_hsm(
        self, ClusterId: str, HsmId: str = None, EniId: str = None, EniIp: str = None
    ) -> DeleteHsmResponseTypeDef:
        """
        [Client.delete_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_hsm)
        """

    def describe_backups(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: Dict[str, List[str]] = None,
        SortAscending: bool = None,
    ) -> DescribeBackupsResponseTypeDef:
        """
        [Client.describe_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.describe_backups)
        """

    def describe_clusters(
        self, Filters: Dict[str, List[str]] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeClustersResponseTypeDef:
        """
        [Client.describe_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.describe_clusters)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.generate_presigned_url)
        """

    def initialize_cluster(
        self, ClusterId: str, SignedCert: str, TrustAnchor: str
    ) -> InitializeClusterResponseTypeDef:
        """
        [Client.initialize_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.initialize_cluster)
        """

    def list_tags(
        self, ResourceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.list_tags)
        """

    def restore_backup(self, BackupId: str) -> RestoreBackupResponseTypeDef:
        """
        [Client.restore_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.restore_backup)
        """

    def tag_resource(self, ResourceId: str, TagList: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.tag_resource)
        """

    def untag_resource(self, ResourceId: str, TagKeyList: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeBackups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_clusters"]
    ) -> DescribeClustersPaginator:
        """
        [Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeClusters)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.ListTags)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
