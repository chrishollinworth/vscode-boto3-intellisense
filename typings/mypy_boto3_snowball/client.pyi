"""
Type annotations for snowball service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_snowball import SnowballClient

    client: SnowballClient = boto3.client("snowball")
    ```
"""
import sys
from typing import Any, Dict, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    JobTypeType,
    LongTermPricingTypeType,
    RemoteManagementType,
    ShipmentStateType,
    ShippingOptionType,
    SnowballCapacityType,
    SnowballTypeType,
)
from .paginator import (
    DescribeAddressesPaginator,
    ListClusterJobsPaginator,
    ListClustersPaginator,
    ListCompatibleImagesPaginator,
    ListJobsPaginator,
    ListLongTermPricingPaginator,
)
from .type_defs import (
    AddressTypeDef,
    CreateAddressResultTypeDef,
    CreateClusterResultTypeDef,
    CreateJobResultTypeDef,
    CreateLongTermPricingResultTypeDef,
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
    ListLongTermPricingResultTypeDef,
    NotificationTypeDef,
    OnDeviceServiceConfigurationTypeDef,
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

class SnowballClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SnowballClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#can_paginate)
        """
    def cancel_cluster(self, *, ClusterId: str) -> Dict[str, Any]:
        """
        Cancels a cluster job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.cancel_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#cancel_cluster)
        """
    def cancel_job(self, *, JobId: str) -> Dict[str, Any]:
        """
        Cancels the specified job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.cancel_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#cancel_job)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#close)
        """
    def create_address(self, *, Address: "AddressTypeDef") -> CreateAddressResultTypeDef:
        """
        Creates an address for a Snow device to be shipped to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.create_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#create_address)
        """
    def create_cluster(
        self,
        *,
        JobType: JobTypeType,
        Resources: "JobResourceTypeDef",
        AddressId: str,
        RoleARN: str,
        SnowballType: SnowballTypeType,
        ShippingOption: ShippingOptionType,
        OnDeviceServiceConfiguration: "OnDeviceServiceConfigurationTypeDef" = None,
        Description: str = None,
        KmsKeyARN: str = None,
        Notification: "NotificationTypeDef" = None,
        ForwardingAddressId: str = None,
        TaxDocuments: "TaxDocumentsTypeDef" = None,
        RemoteManagement: RemoteManagementType = None
    ) -> CreateClusterResultTypeDef:
        """
        Creates an empty cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.create_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#create_cluster)
        """
    def create_job(
        self,
        *,
        JobType: JobTypeType = None,
        Resources: "JobResourceTypeDef" = None,
        OnDeviceServiceConfiguration: "OnDeviceServiceConfigurationTypeDef" = None,
        Description: str = None,
        AddressId: str = None,
        KmsKeyARN: str = None,
        RoleARN: str = None,
        SnowballCapacityPreference: SnowballCapacityType = None,
        ShippingOption: ShippingOptionType = None,
        Notification: "NotificationTypeDef" = None,
        ClusterId: str = None,
        SnowballType: SnowballTypeType = None,
        ForwardingAddressId: str = None,
        TaxDocuments: "TaxDocumentsTypeDef" = None,
        DeviceConfiguration: "DeviceConfigurationTypeDef" = None,
        RemoteManagement: RemoteManagementType = None,
        LongTermPricingId: str = None
    ) -> CreateJobResultTypeDef:
        """
        Creates a job to import or export data between Amazon S3 and your on-premises
        data center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.create_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#create_job)
        """
    def create_long_term_pricing(
        self,
        *,
        LongTermPricingType: LongTermPricingTypeType,
        IsLongTermPricingAutoRenew: bool = None,
        SnowballType: SnowballTypeType = None
    ) -> CreateLongTermPricingResultTypeDef:
        """
        Creates a job with the long-term usage option for a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.create_long_term_pricing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#create_long_term_pricing)
        """
    def create_return_shipping_label(
        self, *, JobId: str, ShippingOption: ShippingOptionType = None
    ) -> CreateReturnShippingLabelResultTypeDef:
        """
        Creates a shipping label that will be used to return the Snow device to Amazon
        Web Services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.create_return_shipping_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#create_return_shipping_label)
        """
    def describe_address(self, *, AddressId: str) -> DescribeAddressResultTypeDef:
        """
        Takes an `AddressId` and returns specific details about that address in the form
        of an `Address` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.describe_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#describe_address)
        """
    def describe_addresses(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> DescribeAddressesResultTypeDef:
        """
        Returns a specified number of `ADDRESS` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.describe_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#describe_addresses)
        """
    def describe_cluster(self, *, ClusterId: str) -> DescribeClusterResultTypeDef:
        """
        Returns information about a specific cluster including shipping information,
        cluster status, and other important metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.describe_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#describe_cluster)
        """
    def describe_job(self, *, JobId: str) -> DescribeJobResultTypeDef:
        """
        Returns information about a specific job including shipping information, job
        status, and other important metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.describe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#describe_job)
        """
    def describe_return_shipping_label(
        self, *, JobId: str
    ) -> DescribeReturnShippingLabelResultTypeDef:
        """
        Information on the shipping label of a Snow device that is being returned to
        Amazon Web Services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.describe_return_shipping_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#describe_return_shipping_label)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#generate_presigned_url)
        """
    def get_job_manifest(self, *, JobId: str) -> GetJobManifestResultTypeDef:
        """
        Returns a link to an Amazon S3 presigned URL for the manifest file associated
        with the specified `JobId` value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.get_job_manifest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#get_job_manifest)
        """
    def get_job_unlock_code(self, *, JobId: str) -> GetJobUnlockCodeResultTypeDef:
        """
        Returns the `UnlockCode` code value for the specified job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.get_job_unlock_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#get_job_unlock_code)
        """
    def get_snowball_usage(self) -> GetSnowballUsageResultTypeDef:
        """
        Returns information about the Snow Family service limit for your account, and
        also the number of Snow devices your account has in use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.get_snowball_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#get_snowball_usage)
        """
    def get_software_updates(self, *, JobId: str) -> GetSoftwareUpdatesResultTypeDef:
        """
        Returns an Amazon S3 presigned URL for an update file associated with a
        specified `JobId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.get_software_updates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#get_software_updates)
        """
    def list_cluster_jobs(
        self, *, ClusterId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListClusterJobsResultTypeDef:
        """
        Returns an array of `JobListEntry` objects of the specified length.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.list_cluster_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#list_cluster_jobs)
        """
    def list_clusters(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListClustersResultTypeDef:
        """
        Returns an array of `ClusterListEntry` objects of the specified length.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.list_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#list_clusters)
        """
    def list_compatible_images(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListCompatibleImagesResultTypeDef:
        """
        This action returns a list of the different Amazon EC2 Amazon Machine Images
        (AMIs) that are owned by your Amazon Web Services accountthat would be supported
        for use on a Snow device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.list_compatible_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#list_compatible_images)
        """
    def list_jobs(self, *, MaxResults: int = None, NextToken: str = None) -> ListJobsResultTypeDef:
        """
        Returns an array of `JobListEntry` objects of the specified length.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#list_jobs)
        """
    def list_long_term_pricing(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListLongTermPricingResultTypeDef:
        """
        Lists all long-term pricing types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.list_long_term_pricing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#list_long_term_pricing)
        """
    def update_cluster(
        self,
        *,
        ClusterId: str,
        RoleARN: str = None,
        Description: str = None,
        Resources: "JobResourceTypeDef" = None,
        OnDeviceServiceConfiguration: "OnDeviceServiceConfigurationTypeDef" = None,
        AddressId: str = None,
        ShippingOption: ShippingOptionType = None,
        Notification: "NotificationTypeDef" = None,
        ForwardingAddressId: str = None
    ) -> Dict[str, Any]:
        """
        While a cluster's `ClusterState` value is in the `AwaitingQuorum` state, you can
        update some of the information associated with a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.update_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#update_cluster)
        """
    def update_job(
        self,
        *,
        JobId: str,
        RoleARN: str = None,
        Notification: "NotificationTypeDef" = None,
        Resources: "JobResourceTypeDef" = None,
        OnDeviceServiceConfiguration: "OnDeviceServiceConfigurationTypeDef" = None,
        AddressId: str = None,
        ShippingOption: ShippingOptionType = None,
        Description: str = None,
        SnowballCapacityPreference: SnowballCapacityType = None,
        ForwardingAddressId: str = None
    ) -> Dict[str, Any]:
        """
        While a job's `JobState` value is `New` , you can update some of the information
        associated with a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.update_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#update_job)
        """
    def update_job_shipment_state(
        self, *, JobId: str, ShipmentState: ShipmentStateType
    ) -> Dict[str, Any]:
        """
        Updates the state when a shipment state changes to a different state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.update_job_shipment_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#update_job_shipment_state)
        """
    def update_long_term_pricing(
        self,
        *,
        LongTermPricingId: str,
        ReplacementJob: str = None,
        IsLongTermPricingAutoRenew: bool = None
    ) -> Dict[str, Any]:
        """
        Updates the long-term pricing type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Client.update_long_term_pricing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#update_long_term_pricing)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_addresses"]
    ) -> DescribeAddressesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/paginators.html#describeaddressespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_cluster_jobs"]
    ) -> ListClusterJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/paginators.html#listclusterjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Paginator.ListClusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/paginators.html#listclusterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_compatible_images"]
    ) -> ListCompatibleImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/paginators.html#listcompatibleimagespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Paginator.ListJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/paginators.html#listjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_long_term_pricing"]
    ) -> ListLongTermPricingPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/snowball.html#Snowball.Paginator.ListLongTermPricing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/paginators.html#listlongtermpricingpaginator)
        """
