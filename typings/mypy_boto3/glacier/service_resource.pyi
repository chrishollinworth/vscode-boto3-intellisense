"""
Type annotations for glacier service ServiceResource

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_glacier import GlacierServiceResource
    import mypy_boto3_glacier.service_resource as glacier_resources

    resource: GlacierServiceResource = boto3.resource("glacier")

    my_account: glacier_resources.Account = resource.Account(...)
    my_archive: glacier_resources.Archive = resource.Archive(...)
    my_job: glacier_resources.Job = resource.Job(...)
    my_multipart_upload: glacier_resources.MultipartUpload = resource.MultipartUpload(...)
    my_notification: glacier_resources.Notification = resource.Notification(...)
    my_vault: glacier_resources.Vault = resource.Vault(...)
```
"""
from typing import IO, Any, Dict, Iterator, List, Union

from boto3.resources.base import ResourceMeta
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from botocore.response import StreamingBody

from .client import GlacierClient
from .type_defs import (
    ArchiveCreationOutputTypeDef,
    CreateVaultOutputTypeDef,
    GetJobOutputOutputTypeDef,
    JobParametersTypeDef,
    ListPartsOutputTypeDef,
    UploadMultipartPartOutputTypeDef,
    VaultNotificationConfigTypeDef,
)

__all__ = (
    "GlacierServiceResource",
    "Account",
    "Archive",
    "Job",
    "MultipartUpload",
    "Notification",
    "Vault",
    "ServiceResourceVaultsCollection",
    "AccountVaultsCollection",
    "VaultCompletedJobsCollection",
    "VaultFailedJobsCollection",
    "VaultJobsCollection",
    "VaultJobsInProgressCollection",
    "VaultMultipartUplaodsCollection",
    "VaultMultipartUploadsCollection",
    "VaultSucceededJobsCollection",
)

class ServiceResourceVaultsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.vaults)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#serviceresourcevaultscollection)
    """

    def all(self) -> "ServiceResourceVaultsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self, *, marker: str = None, limit: str = None
    ) -> "ServiceResourceVaultsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "ServiceResourceVaultsCollection":
        """
        Return at most this many Vaults.
        """
    def page_size(self, count: int) -> "ServiceResourceVaultsCollection":
        """
        Fetch at most this many Vaults per service request.
        """
    def pages(self) -> Iterator[List["Vault"]]:
        """
        A generator which yields pages of Vaults.
        """
    def __iter__(self) -> Iterator["Vault"]:
        """
        A generator which yields Vaults.
        """

class AccountVaultsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Account.vaults)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#accountvaultscollection)
    """

    def all(self) -> "AccountVaultsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self, *, marker: str = None, limit: str = None
    ) -> "AccountVaultsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "AccountVaultsCollection":
        """
        Return at most this many Vaults.
        """
    def page_size(self, count: int) -> "AccountVaultsCollection":
        """
        Fetch at most this many Vaults per service request.
        """
    def pages(self) -> Iterator[List["Vault"]]:
        """
        A generator which yields pages of Vaults.
        """
    def __iter__(self) -> Iterator["Vault"]:
        """
        A generator which yields Vaults.
        """

class VaultCompletedJobsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.completed_jobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultcompletedjobscollection)
    """

    def all(self) -> "VaultCompletedJobsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self,
        *,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None
    ) -> "VaultCompletedJobsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "VaultCompletedJobsCollection":
        """
        Return at most this many Jobs.
        """
    def page_size(self, count: int) -> "VaultCompletedJobsCollection":
        """
        Fetch at most this many Jobs per service request.
        """
    def pages(self) -> Iterator[List["Job"]]:
        """
        A generator which yields pages of Jobs.
        """
    def __iter__(self) -> Iterator["Job"]:
        """
        A generator which yields Jobs.
        """

class VaultFailedJobsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.failed_jobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultfailedjobscollection)
    """

    def all(self) -> "VaultFailedJobsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self,
        *,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None
    ) -> "VaultFailedJobsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "VaultFailedJobsCollection":
        """
        Return at most this many Jobs.
        """
    def page_size(self, count: int) -> "VaultFailedJobsCollection":
        """
        Fetch at most this many Jobs per service request.
        """
    def pages(self) -> Iterator[List["Job"]]:
        """
        A generator which yields pages of Jobs.
        """
    def __iter__(self) -> Iterator["Job"]:
        """
        A generator which yields Jobs.
        """

class VaultJobsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.jobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultjobscollection)
    """

    def all(self) -> "VaultJobsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self,
        *,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None
    ) -> "VaultJobsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "VaultJobsCollection":
        """
        Return at most this many Jobs.
        """
    def page_size(self, count: int) -> "VaultJobsCollection":
        """
        Fetch at most this many Jobs per service request.
        """
    def pages(self) -> Iterator[List["Job"]]:
        """
        A generator which yields pages of Jobs.
        """
    def __iter__(self) -> Iterator["Job"]:
        """
        A generator which yields Jobs.
        """

class VaultJobsInProgressCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.jobs_in_progress)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultjobsinprogresscollection)
    """

    def all(self) -> "VaultJobsInProgressCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self,
        *,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None
    ) -> "VaultJobsInProgressCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "VaultJobsInProgressCollection":
        """
        Return at most this many Jobs.
        """
    def page_size(self, count: int) -> "VaultJobsInProgressCollection":
        """
        Fetch at most this many Jobs per service request.
        """
    def pages(self) -> Iterator[List["Job"]]:
        """
        A generator which yields pages of Jobs.
        """
    def __iter__(self) -> Iterator["Job"]:
        """
        A generator which yields Jobs.
        """

class VaultMultipartUplaodsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.multipart_uplaods)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultmultipartuplaodscollection)
    """

    def all(self) -> "VaultMultipartUplaodsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self, *, marker: str = None, limit: str = None
    ) -> "VaultMultipartUplaodsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "VaultMultipartUplaodsCollection":
        """
        Return at most this many MultipartUploads.
        """
    def page_size(self, count: int) -> "VaultMultipartUplaodsCollection":
        """
        Fetch at most this many MultipartUploads per service request.
        """
    def pages(self) -> Iterator[List["MultipartUpload"]]:
        """
        A generator which yields pages of MultipartUploads.
        """
    def __iter__(self) -> Iterator["MultipartUpload"]:
        """
        A generator which yields MultipartUploads.
        """

class VaultMultipartUploadsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.multipart_uploads)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultmultipartuploadscollection)
    """

    def all(self) -> "VaultMultipartUploadsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self, *, marker: str = None, limit: str = None
    ) -> "VaultMultipartUploadsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "VaultMultipartUploadsCollection":
        """
        Return at most this many MultipartUploads.
        """
    def page_size(self, count: int) -> "VaultMultipartUploadsCollection":
        """
        Fetch at most this many MultipartUploads per service request.
        """
    def pages(self) -> Iterator[List["MultipartUpload"]]:
        """
        A generator which yields pages of MultipartUploads.
        """
    def __iter__(self) -> Iterator["MultipartUpload"]:
        """
        A generator which yields MultipartUploads.
        """

class VaultSucceededJobsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.succeeded_jobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultsucceededjobscollection)
    """

    def all(self) -> "VaultSucceededJobsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self,
        *,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None
    ) -> "VaultSucceededJobsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "VaultSucceededJobsCollection":
        """
        Return at most this many Jobs.
        """
    def page_size(self, count: int) -> "VaultSucceededJobsCollection":
        """
        Fetch at most this many Jobs per service request.
        """
    def pages(self) -> Iterator[List["Job"]]:
        """
        A generator which yields pages of Jobs.
        """
    def __iter__(self) -> Iterator["Job"]:
        """
        A generator which yields Jobs.
        """

class Job(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.Job)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#job)
    """

    job_id: str
    job_description: str
    action: str
    archive_id: str
    vault_arn: str
    creation_date: str
    completed: bool
    status_code: str
    status_message: str
    archive_size_in_bytes: int
    inventory_size_in_bytes: int
    sns_topic: str
    completion_date: str
    sha256_tree_hash: str
    archive_sha256_tree_hash: str
    retrieval_byte_range: str
    tier: str
    inventory_retrieval_parameters: Dict[str, Any]
    job_output_path: str
    select_parameters: Dict[str, Any]
    output_location: Dict[str, Any]
    account_id: str
    vault_name: str
    id: str

    def Vault(self) -> "_Vault":
        """
        Creates a Vault resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Job.Vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#jobvault-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Job.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#jobget_available_subresources-method)
        """
    def get_output(self, *, range: str = None) -> GetJobOutputOutputTypeDef:
        """
        This operation downloads the output of the job you initiated using  InitiateJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Job.get_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#jobget_output-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`Glacier.Client.describe_job` to update the attributes of the Job
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Job.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#jobload-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`Glacier.Client.describe_job` to update the attributes of the Job
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Job.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#jobreload-method)
        """

_Job = Job

class MultipartUpload(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.MultipartUpload)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#multipartupload)
    """

    multipart_upload_id: str
    vault_arn: str
    archive_description: str
    part_size_in_bytes: int
    creation_date: str
    account_id: str
    vault_name: str
    id: str

    def Vault(self) -> "_Vault":
        """
        Creates a Vault resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.MultipartUpload.Vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#multipartuploadvault-method)
        """
    def abort(self) -> None:
        """
        This operation aborts a multipart upload identified by the upload ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.MultipartUpload.abort)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#multipartuploadabort-method)
        """
    def complete(
        self, *, archiveSize: str = None, checksum: str = None
    ) -> ArchiveCreationOutputTypeDef:
        """
        You call this operation to inform Amazon S3 Glacier (Glacier) that all the
        archive parts have been uploaded and that Glacier can now assemble the archive
        from the uploaded parts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.MultipartUpload.complete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#multipartuploadcomplete-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.MultipartUpload.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#multipartuploadget_available_subresources-method)
        """
    def parts(self, *, marker: str = None, limit: str = None) -> ListPartsOutputTypeDef:
        """
        This operation lists the parts of an archive that have been uploaded in a
        specific multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.MultipartUpload.parts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#multipartuploadparts-method)
        """
    def upload_part(
        self,
        *,
        checksum: str = None,
        range: str = None,
        body: Union[bytes, IO[bytes], StreamingBody] = None
    ) -> UploadMultipartPartOutputTypeDef:
        """
        This operation uploads a part of an archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.MultipartUpload.upload_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#multipartuploadupload_part-method)
        """

_MultipartUpload = MultipartUpload

class Notification(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.Notification)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#notification)
    """

    sns_topic: str
    events: List[Any]
    account_id: str
    vault_name: str

    def Vault(self) -> "_Vault":
        """
        Creates a Vault resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Notification.Vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#notificationvault-method)
        """
    def delete(self) -> None:
        """
        This operation deletes the notification configuration set for a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Notification.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#notificationdelete-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Notification.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#notificationget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`Glacier.Client.get_vault_notifications` to update the attributes
        of the Notification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Notification.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#notificationload-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`Glacier.Client.get_vault_notifications` to update the attributes
        of the Notification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Notification.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#notificationreload-method)
        """
    def set(self, *, vaultNotificationConfig: "VaultNotificationConfigTypeDef" = None) -> None:
        """
        This operation configures notifications that will be sent when specific events
        happen to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Notification.set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#notificationset-method)
        """

_Notification = Notification

class Account(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.Account)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#account)
    """

    id: str
    vaults: AccountVaultsCollection

    def Vault(self, name: str) -> "_Vault":
        """
        Creates a Vault resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Account.Vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#accountvault-method)
        """
    def create_vault(self, *, vaultName: str) -> "_Vault":
        """
        This operation creates a new vault with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Account.create_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#accountcreate_vault-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Account.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#accountget_available_subresources-method)
        """

_Account = Account

class Archive(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.Archive)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#archive)
    """

    account_id: str
    vault_name: str
    id: str

    def Vault(self) -> "_Vault":
        """
        Creates a Vault resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Archive.Vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#archivevault-method)
        """
    def delete(self) -> None:
        """
        This operation deletes an archive from a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Archive.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#archivedelete-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Archive.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#archiveget_available_subresources-method)
        """
    def initiate_archive_retrieval(self, *, jobParameters: "JobParametersTypeDef" = None) -> _Job:
        """
        This operation initiates a job of the specified type, which can be a select, an
        archival retrieval, or a vault retrieval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Archive.initiate_archive_retrieval)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#archiveinitiate_archive_retrieval-method)
        """

_Archive = Archive

class Vault(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.Vault)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vault)
    """

    vault_arn: str
    vault_name: str
    creation_date: str
    last_inventory_date: str
    number_of_archives: int
    size_in_bytes: int
    account_id: str
    name: str
    completed_jobs: VaultCompletedJobsCollection
    failed_jobs: VaultFailedJobsCollection
    jobs: VaultJobsCollection
    jobs_in_progress: VaultJobsInProgressCollection
    multipart_uplaods: VaultMultipartUplaodsCollection
    multipart_uploads: VaultMultipartUploadsCollection
    succeeded_jobs: VaultSucceededJobsCollection

    def Account(self) -> _Account:
        """
        Creates a Account resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.Account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultaccount-method)
        """
    def Archive(self, id: str) -> _Archive:
        """
        Creates a Archive resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.Archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultarchive-method)
        """
    def Job(self, id: str) -> _Job:
        """
        Creates a Job resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.Job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultjob-method)
        """
    def MultipartUpload(self, id: str) -> _MultipartUpload:
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.MultipartUpload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultmultipartupload-method)
        """
    def Notification(self) -> _Notification:
        """
        Creates a Notification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.Notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultnotification-method)
        """
    def create(self) -> CreateVaultOutputTypeDef:
        """
        This operation creates a new vault with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.create)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultcreate-method)
        """
    def delete(self) -> None:
        """
        This operation deletes a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultdelete-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultget_available_subresources-method)
        """
    def initiate_inventory_retrieval(self, *, jobParameters: "JobParametersTypeDef" = None) -> _Job:
        """
        This operation initiates a job of the specified type, which can be a select, an
        archival retrieval, or a vault retrieval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.initiate_inventory_retrieval)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultinitiate_inventory_retrieval-method)
        """
    def initiate_multipart_upload(
        self, *, archiveDescription: str = None, partSize: str = None
    ) -> _MultipartUpload:
        """
        This operation initiates a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.initiate_multipart_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultinitiate_multipart_upload-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`Glacier.Client.describe_vault` to update the attributes of the
        Vault resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultload-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`Glacier.Client.describe_vault` to update the attributes of the
        Vault resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultreload-method)
        """
    def upload_archive(
        self,
        *,
        archiveDescription: str = None,
        checksum: str = None,
        body: Union[bytes, IO[bytes], StreamingBody] = None
    ) -> _Archive:
        """
        This operation adds an archive to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.Vault.upload_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#vaultupload_archive-method)
        """

_Vault = Vault

class GlacierResourceMeta(ResourceMeta):
    client: GlacierClient

class GlacierServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html)
    """

    meta: "GlacierResourceMeta"
    vaults: ServiceResourceVaultsCollection

    def Account(self, id: str) -> _Account:
        """
        Creates a Account resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.Account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#glacierserviceresourceaccount-method)
        """
    def Archive(self, account_id: str, vault_name: str, id: str) -> _Archive:
        """
        Creates a Archive resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.Archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#glacierserviceresourcearchive-method)
        """
    def Job(self, account_id: str, vault_name: str, id: str) -> _Job:
        """
        Creates a Job resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.Job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#glacierserviceresourcejob-method)
        """
    def MultipartUpload(self, account_id: str, vault_name: str, id: str) -> _MultipartUpload:
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.MultipartUpload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#glacierserviceresourcemultipartupload-method)
        """
    def Notification(self, account_id: str, vault_name: str) -> _Notification:
        """
        Creates a Notification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.Notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#glacierserviceresourcenotification-method)
        """
    def Vault(self, account_id: str, name: str) -> _Vault:
        """
        Creates a Vault resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.Vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#glacierserviceresourcevault-method)
        """
    def create_vault(self, *, accountId: str, vaultName: str) -> _Vault:
        """
        This operation creates a new vault with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.create_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#glacierserviceresourcecreate_vault-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/glacier.html#Glacier.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/service_resource.html#glacierserviceresourceget_available_subresources-method)
        """
