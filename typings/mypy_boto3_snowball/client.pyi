# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for snowball service client

Usage::

    ```python
    import boto3
    from mypy_boto3_snowball import SnowballClient

    client: SnowballClient = boto3.client("snowball")
    ```
"""
import sys
from typing import Any, Dict, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_snowball.paginator import (
    DescribeAddressesPaginator,
    ListClusterJobsPaginator,
    ListClustersPaginator,
    ListCompatibleImagesPaginator,
    ListJobsPaginator,
)
from mypy_boto3_snowball.type_defs import (
    AddressTypeDef,
    CreateAddressResultTypeDef,
    CreateClusterResultTypeDef,
    CreateJobResultTypeDef,
    CreateReturnShippingLabelResultTypeDef,
    DescribeAddressesResultTypeDef,
    DescribeAddressResultTypeDef,
    DescribeClusterResultTypeDef,
    DescribeJobResultTypeDef,
    DescribeReturnShippingLabelResultTypeDef,
    DeviceConfigurationTypeDef,
    GetJobManifestResultTypeDef,
    GetJobUnlockCodeResultTypeDef,
    GetSnowballUsageResultTypeDef,
    GetSoftwareUpdatesResultTypeDef,
    JobResourceTypeDef,
    ListClusterJobsResultTypeDef,
    ListClustersResultTypeDef,
    ListCompatibleImagesResultTypeDef,
    ListJobsResultTypeDef,
    NotificationTypeDef,
    TaxDocumentsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SnowballClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ClusterLimitExceededException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    Ec2RequestFailedException: Type[BotocoreClientError]
    InvalidAddressException: Type[BotocoreClientError]
    InvalidInputCombinationException: Type[BotocoreClientError]
    InvalidJobStateException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidResourceException: Type[BotocoreClientError]
    KMSRequestFailedException: Type[BotocoreClientError]
    ReturnShippingLabelAlreadyExistsException: Type[BotocoreClientError]
    UnsupportedAddressException: Type[BotocoreClientError]


class SnowballClient:
    """
    [Snowball.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.can_paginate)
        """

    def cancel_cluster(self, ClusterId: str) -> Dict[str, Any]:
        """
        [Client.cancel_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.cancel_cluster)
        """

    def cancel_job(self, JobId: str) -> Dict[str, Any]:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.cancel_job)
        """

    def create_address(self, Address: "AddressTypeDef") -> CreateAddressResultTypeDef:
        """
        [Client.create_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.create_address)
        """

    def create_cluster(
        self,
        JobType: Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        Resources: "JobResourceTypeDef",
        AddressId: str,
        RoleARN: str,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"],
        Description: str = None,
        KmsKeyARN: str = None,
        SnowballType: Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG", "EDGE_S", "SNC1_HDD"] = None,
        Notification: "NotificationTypeDef" = None,
        ForwardingAddressId: str = None,
        TaxDocuments: "TaxDocumentsTypeDef" = None,
    ) -> CreateClusterResultTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.create_cluster)
        """

    def create_job(
        self,
        JobType: Literal["IMPORT", "EXPORT", "LOCAL_USE"] = None,
        Resources: "JobResourceTypeDef" = None,
        Description: str = None,
        AddressId: str = None,
        KmsKeyARN: str = None,
        RoleARN: str = None,
        SnowballCapacityPreference: Literal[
            "T50", "T80", "T100", "T42", "T98", "T8", "NoPreference"
        ] = None,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"] = None,
        Notification: "NotificationTypeDef" = None,
        ClusterId: str = None,
        SnowballType: Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG", "EDGE_S", "SNC1_HDD"] = None,
        ForwardingAddressId: str = None,
        TaxDocuments: "TaxDocumentsTypeDef" = None,
        DeviceConfiguration: "DeviceConfigurationTypeDef" = None,
    ) -> CreateJobResultTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.create_job)
        """

    def create_return_shipping_label(
        self,
        JobId: str,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"] = None,
    ) -> CreateReturnShippingLabelResultTypeDef:
        """
        [Client.create_return_shipping_label documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.create_return_shipping_label)
        """

    def describe_address(self, AddressId: str) -> DescribeAddressResultTypeDef:
        """
        [Client.describe_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.describe_address)
        """

    def describe_addresses(
        self, MaxResults: int = None, NextToken: str = None
    ) -> DescribeAddressesResultTypeDef:
        """
        [Client.describe_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.describe_addresses)
        """

    def describe_cluster(self, ClusterId: str) -> DescribeClusterResultTypeDef:
        """
        [Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.describe_cluster)
        """

    def describe_job(self, JobId: str) -> DescribeJobResultTypeDef:
        """
        [Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.describe_job)
        """

    def describe_return_shipping_label(
        self, JobId: str = None
    ) -> DescribeReturnShippingLabelResultTypeDef:
        """
        [Client.describe_return_shipping_label documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.describe_return_shipping_label)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.generate_presigned_url)
        """

    def get_job_manifest(self, JobId: str) -> GetJobManifestResultTypeDef:
        """
        [Client.get_job_manifest documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.get_job_manifest)
        """

    def get_job_unlock_code(self, JobId: str) -> GetJobUnlockCodeResultTypeDef:
        """
        [Client.get_job_unlock_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.get_job_unlock_code)
        """

    def get_snowball_usage(self) -> GetSnowballUsageResultTypeDef:
        """
        [Client.get_snowball_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.get_snowball_usage)
        """

    def get_software_updates(self, JobId: str) -> GetSoftwareUpdatesResultTypeDef:
        """
        [Client.get_software_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.get_software_updates)
        """

    def list_cluster_jobs(
        self, ClusterId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListClusterJobsResultTypeDef:
        """
        [Client.list_cluster_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.list_cluster_jobs)
        """

    def list_clusters(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListClustersResultTypeDef:
        """
        [Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.list_clusters)
        """

    def list_compatible_images(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListCompatibleImagesResultTypeDef:
        """
        [Client.list_compatible_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.list_compatible_images)
        """

    def list_jobs(self, MaxResults: int = None, NextToken: str = None) -> ListJobsResultTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.list_jobs)
        """

    def update_cluster(
        self,
        ClusterId: str,
        RoleARN: str = None,
        Description: str = None,
        Resources: "JobResourceTypeDef" = None,
        AddressId: str = None,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"] = None,
        Notification: "NotificationTypeDef" = None,
        ForwardingAddressId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.update_cluster)
        """

    def update_job(
        self,
        JobId: str,
        RoleARN: str = None,
        Notification: "NotificationTypeDef" = None,
        Resources: "JobResourceTypeDef" = None,
        AddressId: str = None,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"] = None,
        Description: str = None,
        SnowballCapacityPreference: Literal[
            "T50", "T80", "T100", "T42", "T98", "T8", "NoPreference"
        ] = None,
        ForwardingAddressId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.update_job)
        """

    def update_job_shipment_state(
        self, JobId: str, ShipmentState: Literal["RECEIVED", "RETURNED"]
    ) -> Dict[str, Any]:
        """
        [Client.update_job_shipment_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Client.update_job_shipment_state)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_addresses"]
    ) -> DescribeAddressesPaginator:
        """
        [Paginator.DescribeAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cluster_jobs"]
    ) -> ListClusterJobsPaginator:
        """
        [Paginator.ListClusterJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.ListClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compatible_images"]
    ) -> ListCompatibleImagesPaginator:
        """
        [Paginator.ListCompatibleImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.ListJobs)
        """
