# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for glacier service client

Usage::

    ```python
    import boto3
    from mypy_boto3_glacier import GlacierClient

    client: GlacierClient = boto3.client("glacier")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_glacier.paginator import (
    ListJobsPaginator,
    ListMultipartUploadsPaginator,
    ListPartsPaginator,
    ListVaultsPaginator,
)
from mypy_boto3_glacier.type_defs import (
    ArchiveCreationOutputTypeDef,
    CreateVaultOutputTypeDef,
    DataRetrievalPolicyTypeDef,
    DescribeVaultOutputTypeDef,
    GetDataRetrievalPolicyOutputTypeDef,
    GetJobOutputOutputTypeDef,
    GetVaultAccessPolicyOutputTypeDef,
    GetVaultLockOutputTypeDef,
    GetVaultNotificationsOutputTypeDef,
    GlacierJobDescriptionTypeDef,
    InitiateJobOutputTypeDef,
    InitiateMultipartUploadOutputTypeDef,
    InitiateVaultLockOutputTypeDef,
    JobParametersTypeDef,
    ListJobsOutputTypeDef,
    ListMultipartUploadsOutputTypeDef,
    ListPartsOutputTypeDef,
    ListProvisionedCapacityOutputTypeDef,
    ListTagsForVaultOutputTypeDef,
    ListVaultsOutputTypeDef,
    PurchaseProvisionedCapacityOutputTypeDef,
    UploadMultipartPartOutputTypeDef,
    VaultAccessPolicyTypeDef,
    VaultLockPolicyTypeDef,
    VaultNotificationConfigTypeDef,
)
from mypy_boto3_glacier.waiter import VaultExistsWaiter, VaultNotExistsWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlacierClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    InsufficientCapacityException: Type[Boto3ClientError]
    InvalidParameterValueException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    MissingParameterValueException: Type[Boto3ClientError]
    PolicyEnforcedException: Type[Boto3ClientError]
    RequestTimeoutException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]


class GlacierClient:
    """
    [Glacier.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client)
    """

    exceptions: Exceptions

    def abort_multipart_upload(self, accountId: str, vaultName: str, uploadId: str) -> None:
        """
        [Client.abort_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.abort_multipart_upload)
        """

    def abort_vault_lock(self, accountId: str, vaultName: str) -> None:
        """
        [Client.abort_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.abort_vault_lock)
        """

    def add_tags_to_vault(
        self, accountId: str, vaultName: str, Tags: Dict[str, str] = None
    ) -> None:
        """
        [Client.add_tags_to_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.add_tags_to_vault)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.can_paginate)
        """

    def complete_multipart_upload(
        self,
        accountId: str,
        vaultName: str,
        uploadId: str,
        archiveSize: str = None,
        checksum: str = None,
    ) -> ArchiveCreationOutputTypeDef:
        """
        [Client.complete_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.complete_multipart_upload)
        """

    def complete_vault_lock(self, accountId: str, vaultName: str, lockId: str) -> None:
        """
        [Client.complete_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.complete_vault_lock)
        """

    def create_vault(self, accountId: str, vaultName: str) -> CreateVaultOutputTypeDef:
        """
        [Client.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.create_vault)
        """

    def delete_archive(self, accountId: str, vaultName: str, archiveId: str) -> None:
        """
        [Client.delete_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.delete_archive)
        """

    def delete_vault(self, accountId: str, vaultName: str) -> None:
        """
        [Client.delete_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.delete_vault)
        """

    def delete_vault_access_policy(self, accountId: str, vaultName: str) -> None:
        """
        [Client.delete_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.delete_vault_access_policy)
        """

    def delete_vault_notifications(self, accountId: str, vaultName: str) -> None:
        """
        [Client.delete_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.delete_vault_notifications)
        """

    def describe_job(
        self, accountId: str, vaultName: str, jobId: str
    ) -> "GlacierJobDescriptionTypeDef":
        """
        [Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.describe_job)
        """

    def describe_vault(self, accountId: str, vaultName: str) -> "DescribeVaultOutputTypeDef":
        """
        [Client.describe_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.describe_vault)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.generate_presigned_url)
        """

    def get_data_retrieval_policy(self, accountId: str) -> GetDataRetrievalPolicyOutputTypeDef:
        """
        [Client.get_data_retrieval_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.get_data_retrieval_policy)
        """

    def get_job_output(
        self, accountId: str, vaultName: str, jobId: str, range: str = None
    ) -> GetJobOutputOutputTypeDef:
        """
        [Client.get_job_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.get_job_output)
        """

    def get_vault_access_policy(
        self, accountId: str, vaultName: str
    ) -> GetVaultAccessPolicyOutputTypeDef:
        """
        [Client.get_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.get_vault_access_policy)
        """

    def get_vault_lock(self, accountId: str, vaultName: str) -> GetVaultLockOutputTypeDef:
        """
        [Client.get_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.get_vault_lock)
        """

    def get_vault_notifications(
        self, accountId: str, vaultName: str
    ) -> GetVaultNotificationsOutputTypeDef:
        """
        [Client.get_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.get_vault_notifications)
        """

    def initiate_job(
        self, accountId: str, vaultName: str, jobParameters: JobParametersTypeDef = None
    ) -> InitiateJobOutputTypeDef:
        """
        [Client.initiate_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.initiate_job)
        """

    def initiate_multipart_upload(
        self, accountId: str, vaultName: str, archiveDescription: str = None, partSize: str = None
    ) -> InitiateMultipartUploadOutputTypeDef:
        """
        [Client.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.initiate_multipart_upload)
        """

    def initiate_vault_lock(
        self, accountId: str, vaultName: str, policy: VaultLockPolicyTypeDef = None
    ) -> InitiateVaultLockOutputTypeDef:
        """
        [Client.initiate_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.initiate_vault_lock)
        """

    def list_jobs(
        self,
        accountId: str,
        vaultName: str,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None,
    ) -> ListJobsOutputTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.list_jobs)
        """

    def list_multipart_uploads(
        self, accountId: str, vaultName: str, marker: str = None, limit: str = None
    ) -> ListMultipartUploadsOutputTypeDef:
        """
        [Client.list_multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.list_multipart_uploads)
        """

    def list_parts(
        self, accountId: str, vaultName: str, uploadId: str, marker: str = None, limit: str = None
    ) -> ListPartsOutputTypeDef:
        """
        [Client.list_parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.list_parts)
        """

    def list_provisioned_capacity(self, accountId: str) -> ListProvisionedCapacityOutputTypeDef:
        """
        [Client.list_provisioned_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.list_provisioned_capacity)
        """

    def list_tags_for_vault(self, accountId: str, vaultName: str) -> ListTagsForVaultOutputTypeDef:
        """
        [Client.list_tags_for_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.list_tags_for_vault)
        """

    def list_vaults(
        self, accountId: str, marker: str = None, limit: str = None
    ) -> ListVaultsOutputTypeDef:
        """
        [Client.list_vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.list_vaults)
        """

    def purchase_provisioned_capacity(
        self, accountId: str
    ) -> PurchaseProvisionedCapacityOutputTypeDef:
        """
        [Client.purchase_provisioned_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.purchase_provisioned_capacity)
        """

    def remove_tags_from_vault(
        self, accountId: str, vaultName: str, TagKeys: List[str] = None
    ) -> None:
        """
        [Client.remove_tags_from_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.remove_tags_from_vault)
        """

    def set_data_retrieval_policy(
        self, accountId: str, Policy: "DataRetrievalPolicyTypeDef" = None
    ) -> None:
        """
        [Client.set_data_retrieval_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.set_data_retrieval_policy)
        """

    def set_vault_access_policy(
        self, accountId: str, vaultName: str, policy: "VaultAccessPolicyTypeDef" = None
    ) -> None:
        """
        [Client.set_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.set_vault_access_policy)
        """

    def set_vault_notifications(
        self,
        accountId: str,
        vaultName: str,
        vaultNotificationConfig: "VaultNotificationConfigTypeDef" = None,
    ) -> None:
        """
        [Client.set_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.set_vault_notifications)
        """

    def upload_archive(
        self,
        vaultName: str,
        accountId: str,
        archiveDescription: str = None,
        checksum: str = None,
        body: Union[bytes, IO[bytes]] = None,
    ) -> ArchiveCreationOutputTypeDef:
        """
        [Client.upload_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.upload_archive)
        """

    def upload_multipart_part(
        self,
        accountId: str,
        vaultName: str,
        uploadId: str,
        checksum: str = None,
        range: str = None,
        body: Union[bytes, IO[bytes]] = None,
    ) -> UploadMultipartPartOutputTypeDef:
        """
        [Client.upload_multipart_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Client.upload_multipart_part)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Paginator.ListJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_multipart_uploads"]
    ) -> ListMultipartUploadsPaginator:
        """
        [Paginator.ListMultipartUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Paginator.ListMultipartUploads)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_parts"]) -> ListPartsPaginator:
        """
        [Paginator.ListParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Paginator.ListParts)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_vaults"]) -> ListVaultsPaginator:
        """
        [Paginator.ListVaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Paginator.ListVaults)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(self, waiter_name: Literal["vault_exists"]) -> VaultExistsWaiter:
        """
        [Waiter.VaultExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Waiter.VaultExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vault_not_exists"]) -> VaultNotExistsWaiter:
        """
        [Waiter.VaultNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Waiter.VaultNotExists)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
