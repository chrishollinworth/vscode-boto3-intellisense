"""
Type annotations for glacier service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_glacier import GlacierClient

    client: GlacierClient = boto3.client("glacier")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .paginator import (
    ListJobsPaginator,
    ListMultipartUploadsPaginator,
    ListPartsPaginator,
    ListVaultsPaginator,
)
from .type_defs import (
    ArchiveCreationOutputTypeDef,
    CreateVaultOutputTypeDef,
    DataRetrievalPolicyTypeDef,
    DescribeVaultOutputResponseMetadataTypeDef,
    GetDataRetrievalPolicyOutputTypeDef,
    GetJobOutputOutputTypeDef,
    GetVaultAccessPolicyOutputTypeDef,
    GetVaultLockOutputTypeDef,
    GetVaultNotificationsOutputTypeDef,
    GlacierJobDescriptionResponseMetadataTypeDef,
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
from .waiter import VaultExistsWaiter, VaultNotExistsWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("GlacierClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InsufficientCapacityException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MissingParameterValueException: Type[BotocoreClientError]
    PolicyEnforcedException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]

class GlacierClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        GlacierClient exceptions.
        """
    def abort_multipart_upload(self, *, accountId: str, vaultName: str, uploadId: str) -> None:
        """
        This operation aborts a multipart upload identified by the upload ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.abort_multipart_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#abort_multipart_upload)
        """
    def abort_vault_lock(self, *, accountId: str, vaultName: str) -> None:
        """
        This operation aborts the vault locking process if the vault lock is not in the
        `Locked` state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.abort_vault_lock)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#abort_vault_lock)
        """
    def add_tags_to_vault(
        self, *, accountId: str, vaultName: str, Tags: Dict[str, str] = None
    ) -> None:
        """
        This operation adds the specified tags to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.add_tags_to_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#add_tags_to_vault)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#can_paginate)
        """
    def complete_multipart_upload(
        self,
        *,
        accountId: str,
        vaultName: str,
        uploadId: str,
        archiveSize: str = None,
        checksum: str = None
    ) -> ArchiveCreationOutputTypeDef:
        """
        You call this operation to inform Amazon S3 Glacier (Glacier) that all the
        archive parts have been uploaded and that Glacier can now assemble the archive
        from the uploaded parts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.complete_multipart_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#complete_multipart_upload)
        """
    def complete_vault_lock(self, *, accountId: str, vaultName: str, lockId: str) -> None:
        """
        This operation completes the vault locking process by transitioning the vault
        lock from the `InProgress` state to the `Locked` state, which causes the vault
        lock policy to become unchangeable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.complete_vault_lock)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#complete_vault_lock)
        """
    def create_vault(self, *, accountId: str, vaultName: str) -> CreateVaultOutputTypeDef:
        """
        This operation creates a new vault with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.create_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#create_vault)
        """
    def delete_archive(self, *, accountId: str, vaultName: str, archiveId: str) -> None:
        """
        This operation deletes an archive from a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.delete_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#delete_archive)
        """
    def delete_vault(self, *, accountId: str, vaultName: str) -> None:
        """
        This operation deletes a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.delete_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#delete_vault)
        """
    def delete_vault_access_policy(self, *, accountId: str, vaultName: str) -> None:
        """
        This operation deletes the access policy associated with the specified vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.delete_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#delete_vault_access_policy)
        """
    def delete_vault_notifications(self, *, accountId: str, vaultName: str) -> None:
        """
        This operation deletes the notification configuration set for a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.delete_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#delete_vault_notifications)
        """
    def describe_job(
        self, *, accountId: str, vaultName: str, jobId: str
    ) -> GlacierJobDescriptionResponseMetadataTypeDef:
        """
        This operation returns information about a job you previously initiated,
        including the job initiation date, the user who initiated the job, the job
        status code/message and the Amazon SNS topic to notify after Amazon S3 Glacier
        (Glacier) completes the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.describe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#describe_job)
        """
    def describe_vault(
        self, *, accountId: str, vaultName: str
    ) -> DescribeVaultOutputResponseMetadataTypeDef:
        """
        This operation returns information about a vault, including the vault's Amazon
        Resource Name (ARN), the date the vault was created, the number of archives it
        contains, and the total size of all the archives in the vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.describe_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#describe_vault)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#generate_presigned_url)
        """
    def get_data_retrieval_policy(self, *, accountId: str) -> GetDataRetrievalPolicyOutputTypeDef:
        """
        This operation returns the current data retrieval policy for the account and
        region specified in the GET request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.get_data_retrieval_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#get_data_retrieval_policy)
        """
    def get_job_output(
        self, *, accountId: str, vaultName: str, jobId: str, range: str = None
    ) -> GetJobOutputOutputTypeDef:
        """
        This operation downloads the output of the job you initiated using  InitiateJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.get_job_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#get_job_output)
        """
    def get_vault_access_policy(
        self, *, accountId: str, vaultName: str
    ) -> GetVaultAccessPolicyOutputTypeDef:
        """
        This operation retrieves the `access-policy` subresource set on the vault; for
        more information on setting this subresource, see `Set Vault Access Policy (PUT
        access-policy) <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-
        SetVaultAccessPolicy.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.get_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#get_vault_access_policy)
        """
    def get_vault_lock(self, *, accountId: str, vaultName: str) -> GetVaultLockOutputTypeDef:
        """
        This operation retrieves the following attributes from the `lock-policy`
        subresource set on the specified vault * The vault lock policy set on the vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.get_vault_lock)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#get_vault_lock)
        """
    def get_vault_notifications(
        self, *, accountId: str, vaultName: str
    ) -> GetVaultNotificationsOutputTypeDef:
        """
        This operation retrieves the `notification-configuration` subresource of the
        specified vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.get_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#get_vault_notifications)
        """
    def initiate_job(
        self, *, accountId: str, vaultName: str, jobParameters: "JobParametersTypeDef" = None
    ) -> InitiateJobOutputTypeDef:
        """
        This operation initiates a job of the specified type, which can be a select, an
        archival retrieval, or a vault retrieval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.initiate_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#initiate_job)
        """
    def initiate_multipart_upload(
        self,
        *,
        accountId: str,
        vaultName: str,
        archiveDescription: str = None,
        partSize: str = None
    ) -> InitiateMultipartUploadOutputTypeDef:
        """
        This operation initiates a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.initiate_multipart_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#initiate_multipart_upload)
        """
    def initiate_vault_lock(
        self, *, accountId: str, vaultName: str, policy: "VaultLockPolicyTypeDef" = None
    ) -> InitiateVaultLockOutputTypeDef:
        """
        This operation initiates the vault locking process by doing the following *
        Installing a vault lock policy on the specified vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.initiate_vault_lock)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#initiate_vault_lock)
        """
    def list_jobs(
        self,
        *,
        accountId: str,
        vaultName: str,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None
    ) -> ListJobsOutputTypeDef:
        """
        This operation lists jobs for a vault, including jobs that are in-progress and
        jobs that have recently finished.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#list_jobs)
        """
    def list_multipart_uploads(
        self, *, accountId: str, vaultName: str, marker: str = None, limit: str = None
    ) -> ListMultipartUploadsOutputTypeDef:
        """
        This operation lists in-progress multipart uploads for the specified vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.list_multipart_uploads)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#list_multipart_uploads)
        """
    def list_parts(
        self,
        *,
        accountId: str,
        vaultName: str,
        uploadId: str,
        marker: str = None,
        limit: str = None
    ) -> ListPartsOutputTypeDef:
        """
        This operation lists the parts of an archive that have been uploaded in a
        specific multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.list_parts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#list_parts)
        """
    def list_provisioned_capacity(self, *, accountId: str) -> ListProvisionedCapacityOutputTypeDef:
        """
        This operation lists the provisioned capacity units for the specified AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.list_provisioned_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#list_provisioned_capacity)
        """
    def list_tags_for_vault(
        self, *, accountId: str, vaultName: str
    ) -> ListTagsForVaultOutputTypeDef:
        """
        This operation lists all the tags attached to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.list_tags_for_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#list_tags_for_vault)
        """
    def list_vaults(
        self, *, accountId: str, marker: str = None, limit: str = None
    ) -> ListVaultsOutputTypeDef:
        """
        This operation lists all vaults owned by the calling user's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.list_vaults)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#list_vaults)
        """
    def purchase_provisioned_capacity(
        self, *, accountId: str
    ) -> PurchaseProvisionedCapacityOutputTypeDef:
        """
        This operation purchases a provisioned capacity unit for an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.purchase_provisioned_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#purchase_provisioned_capacity)
        """
    def remove_tags_from_vault(
        self, *, accountId: str, vaultName: str, TagKeys: List[str] = None
    ) -> None:
        """
        This operation removes one or more tags from the set of tags attached to a
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.remove_tags_from_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#remove_tags_from_vault)
        """
    def set_data_retrieval_policy(
        self, *, accountId: str, Policy: "DataRetrievalPolicyTypeDef" = None
    ) -> None:
        """
        This operation sets and then enacts a data retrieval policy in the region
        specified in the PUT request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.set_data_retrieval_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#set_data_retrieval_policy)
        """
    def set_vault_access_policy(
        self, *, accountId: str, vaultName: str, policy: "VaultAccessPolicyTypeDef" = None
    ) -> None:
        """
        This operation configures an access policy for a vault and will overwrite an
        existing policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.set_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#set_vault_access_policy)
        """
    def set_vault_notifications(
        self,
        *,
        accountId: str,
        vaultName: str,
        vaultNotificationConfig: "VaultNotificationConfigTypeDef" = None
    ) -> None:
        """
        This operation configures notifications that will be sent when specific events
        happen to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.set_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#set_vault_notifications)
        """
    def upload_archive(
        self,
        *,
        vaultName: str,
        accountId: str,
        archiveDescription: str = None,
        checksum: str = None,
        body: Union[bytes, IO[bytes], StreamingBody] = None
    ) -> ArchiveCreationOutputTypeDef:
        """
        This operation adds an archive to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.upload_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#upload_archive)
        """
    def upload_multipart_part(
        self,
        *,
        accountId: str,
        vaultName: str,
        uploadId: str,
        checksum: str = None,
        range: str = None,
        body: Union[bytes, IO[bytes], StreamingBody] = None
    ) -> UploadMultipartPartOutputTypeDef:
        """
        This operation uploads a part of an archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Client.upload_multipart_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#upload_multipart_part)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Paginator.ListJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/paginators.html#listjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_multipart_uploads"]
    ) -> ListMultipartUploadsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Paginator.ListMultipartUploads)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/paginators.html#listmultipartuploadspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_parts"]) -> ListPartsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Paginator.ListParts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/paginators.html#listpartspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_vaults"]) -> ListVaultsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Paginator.ListVaults)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/paginators.html#listvaultspaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["vault_exists"]) -> VaultExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Waiter.VaultExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/waiters.html#vaultexistswaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["vault_not_exists"]) -> VaultNotExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/glacier.html#Glacier.Waiter.VaultNotExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/waiters.html#vaultnotexistswaiter)
        """
