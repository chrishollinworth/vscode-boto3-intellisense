# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for glacier service ServiceResource

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

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from mypy_boto3_glacier.type_defs import (
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
    [ServiceResource.vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.vaults)
    """

    def all(self) -> "ServiceResourceVaultsCollection":
        pass

    def filter(  # type: ignore
        self, marker: str = None, limit: str = None
    ) -> "ServiceResourceVaultsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceVaultsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceVaultsCollection":
        pass

    def pages(self) -> Iterator[List["Vault"]]:
        pass

    def __iter__(self) -> Iterator["Vault"]:
        pass


class AccountVaultsCollection(ResourceCollection):
    """
    [Account.vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Account.vaults)
    """

    def all(self) -> "AccountVaultsCollection":
        pass

    def filter(  # type: ignore
        self, marker: str = None, limit: str = None
    ) -> "AccountVaultsCollection":
        pass

    def limit(self, count: int) -> "AccountVaultsCollection":
        pass

    def page_size(self, count: int) -> "AccountVaultsCollection":
        pass

    def pages(self) -> Iterator[List["Vault"]]:
        pass

    def __iter__(self) -> Iterator["Vault"]:
        pass


class VaultCompletedJobsCollection(ResourceCollection):
    """
    [Vault.completed_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.completed_jobs)
    """

    def all(self) -> "VaultCompletedJobsCollection":
        pass

    def filter(  # type: ignore
        self, limit: str = None, marker: str = None, statuscode: str = None, completed: str = None
    ) -> "VaultCompletedJobsCollection":
        pass

    def limit(self, count: int) -> "VaultCompletedJobsCollection":
        pass

    def page_size(self, count: int) -> "VaultCompletedJobsCollection":
        pass

    def pages(self) -> Iterator[List["Job"]]:
        pass

    def __iter__(self) -> Iterator["Job"]:
        pass


class VaultFailedJobsCollection(ResourceCollection):
    """
    [Vault.failed_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.failed_jobs)
    """

    def all(self) -> "VaultFailedJobsCollection":
        pass

    def filter(  # type: ignore
        self, limit: str = None, marker: str = None, statuscode: str = None, completed: str = None
    ) -> "VaultFailedJobsCollection":
        pass

    def limit(self, count: int) -> "VaultFailedJobsCollection":
        pass

    def page_size(self, count: int) -> "VaultFailedJobsCollection":
        pass

    def pages(self) -> Iterator[List["Job"]]:
        pass

    def __iter__(self) -> Iterator["Job"]:
        pass


class VaultJobsCollection(ResourceCollection):
    """
    [Vault.jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.jobs)
    """

    def all(self) -> "VaultJobsCollection":
        pass

    def filter(  # type: ignore
        self, limit: str = None, marker: str = None, statuscode: str = None, completed: str = None
    ) -> "VaultJobsCollection":
        pass

    def limit(self, count: int) -> "VaultJobsCollection":
        pass

    def page_size(self, count: int) -> "VaultJobsCollection":
        pass

    def pages(self) -> Iterator[List["Job"]]:
        pass

    def __iter__(self) -> Iterator["Job"]:
        pass


class VaultJobsInProgressCollection(ResourceCollection):
    """
    [Vault.jobs_in_progress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.jobs_in_progress)
    """

    def all(self) -> "VaultJobsInProgressCollection":
        pass

    def filter(  # type: ignore
        self, limit: str = None, marker: str = None, statuscode: str = None, completed: str = None
    ) -> "VaultJobsInProgressCollection":
        pass

    def limit(self, count: int) -> "VaultJobsInProgressCollection":
        pass

    def page_size(self, count: int) -> "VaultJobsInProgressCollection":
        pass

    def pages(self) -> Iterator[List["Job"]]:
        pass

    def __iter__(self) -> Iterator["Job"]:
        pass


class VaultMultipartUplaodsCollection(ResourceCollection):
    """
    [Vault.multipart_uplaods documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.multipart_uplaods)
    """

    def all(self) -> "VaultMultipartUplaodsCollection":
        pass

    def filter(  # type: ignore
        self, marker: str = None, limit: str = None
    ) -> "VaultMultipartUplaodsCollection":
        pass

    def limit(self, count: int) -> "VaultMultipartUplaodsCollection":
        pass

    def page_size(self, count: int) -> "VaultMultipartUplaodsCollection":
        pass

    def pages(self) -> Iterator[List["MultipartUpload"]]:
        pass

    def __iter__(self) -> Iterator["MultipartUpload"]:
        pass


class VaultMultipartUploadsCollection(ResourceCollection):
    """
    [Vault.multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.multipart_uploads)
    """

    def all(self) -> "VaultMultipartUploadsCollection":
        pass

    def filter(  # type: ignore
        self, marker: str = None, limit: str = None
    ) -> "VaultMultipartUploadsCollection":
        pass

    def limit(self, count: int) -> "VaultMultipartUploadsCollection":
        pass

    def page_size(self, count: int) -> "VaultMultipartUploadsCollection":
        pass

    def pages(self) -> Iterator[List["MultipartUpload"]]:
        pass

    def __iter__(self) -> Iterator["MultipartUpload"]:
        pass


class VaultSucceededJobsCollection(ResourceCollection):
    """
    [Vault.succeeded_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.succeeded_jobs)
    """

    def all(self) -> "VaultSucceededJobsCollection":
        pass

    def filter(  # type: ignore
        self, limit: str = None, marker: str = None, statuscode: str = None, completed: str = None
    ) -> "VaultSucceededJobsCollection":
        pass

    def limit(self, count: int) -> "VaultSucceededJobsCollection":
        pass

    def page_size(self, count: int) -> "VaultSucceededJobsCollection":
        pass

    def pages(self) -> Iterator[List["Job"]]:
        pass

    def __iter__(self) -> Iterator["Job"]:
        pass


class Job(Boto3ServiceResource):
    """
    [Job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.Job)
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
        [Job.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Job.Vault)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Job.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Job.get_available_subresources)
        """

    def get_output(self, range: str = None) -> GetJobOutputOutputTypeDef:
        """
        [Job.get_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Job.get_output)
        """

    def load(self) -> None:
        """
        [Job.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Job.load)
        """

    def reload(self) -> None:
        """
        [Job.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Job.reload)
        """


_Job = Job


class MultipartUpload(Boto3ServiceResource):
    """
    [MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.MultipartUpload)
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
        [MultipartUpload.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.MultipartUpload.Vault)
        """

    def abort(self) -> None:
        """
        [MultipartUpload.abort documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.MultipartUpload.abort)
        """

    def complete(
        self, archiveSize: str = None, checksum: str = None
    ) -> ArchiveCreationOutputTypeDef:
        """
        [MultipartUpload.complete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.MultipartUpload.complete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [MultipartUpload.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.MultipartUpload.get_available_subresources)
        """

    def parts(self, marker: str = None, limit: str = None) -> ListPartsOutputTypeDef:
        """
        [MultipartUpload.parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.MultipartUpload.parts)
        """

    def upload_part(
        self, checksum: str = None, range: str = None, body: Union[bytes, IO[bytes]] = None
    ) -> UploadMultipartPartOutputTypeDef:
        """
        [MultipartUpload.upload_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.MultipartUpload.upload_part)
        """


_MultipartUpload = MultipartUpload


class Notification(Boto3ServiceResource):
    """
    [Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.Notification)
    """

    sns_topic: str
    events: List[Any]
    account_id: str
    vault_name: str

    def Vault(self) -> "_Vault":
        """
        [Notification.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Notification.Vault)
        """

    def delete(self) -> None:
        """
        [Notification.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Notification.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Notification.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Notification.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Notification.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Notification.load)
        """

    def reload(self) -> None:
        """
        [Notification.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Notification.reload)
        """

    def set(self, vaultNotificationConfig: "VaultNotificationConfigTypeDef" = None) -> None:
        """
        [Notification.set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Notification.set)
        """


_Notification = Notification


class Account(Boto3ServiceResource):
    """
    [Account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.Account)
    """

    id: str
    vaults: AccountVaultsCollection

    def Vault(self, name: str) -> "_Vault":
        """
        [Account.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Account.Vault)
        """

    def create_vault(self, vaultName: str) -> "_Vault":
        """
        [Account.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Account.create_vault)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Account.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Account.get_available_subresources)
        """


_Account = Account


class Archive(Boto3ServiceResource):
    """
    [Archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.Archive)
    """

    account_id: str
    vault_name: str
    id: str

    def Vault(self) -> "_Vault":
        """
        [Archive.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Archive.Vault)
        """

    def delete(self) -> None:
        """
        [Archive.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Archive.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Archive.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Archive.get_available_subresources)
        """

    def initiate_archive_retrieval(self, jobParameters: JobParametersTypeDef = None) -> _Job:
        """
        [Archive.initiate_archive_retrieval documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Archive.initiate_archive_retrieval)
        """


_Archive = Archive


class Vault(Boto3ServiceResource):
    """
    [Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.Vault)
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
        [Vault.Account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.Account)
        """

    def Archive(self, id: str) -> _Archive:
        """
        [Vault.Archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.Archive)
        """

    def Job(self, id: str) -> _Job:
        """
        [Vault.Job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.Job)
        """

    def MultipartUpload(self, id: str) -> _MultipartUpload:
        """
        [Vault.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.MultipartUpload)
        """

    def Notification(self) -> _Notification:
        """
        [Vault.Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.Notification)
        """

    def create(self) -> CreateVaultOutputTypeDef:
        """
        [Vault.create documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.create)
        """

    def delete(self) -> None:
        """
        [Vault.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Vault.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.get_available_subresources)
        """

    def initiate_inventory_retrieval(self, jobParameters: JobParametersTypeDef = None) -> _Job:
        """
        [Vault.initiate_inventory_retrieval documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.initiate_inventory_retrieval)
        """

    def initiate_multipart_upload(
        self, archiveDescription: str = None, partSize: str = None
    ) -> _MultipartUpload:
        """
        [Vault.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.initiate_multipart_upload)
        """

    def load(self) -> None:
        """
        [Vault.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.load)
        """

    def reload(self) -> None:
        """
        [Vault.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.reload)
        """

    def upload_archive(
        self,
        archiveDescription: str = None,
        checksum: str = None,
        body: Union[bytes, IO[bytes]] = None,
    ) -> _Archive:
        """
        [Vault.upload_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.Vault.upload_archive)
        """


_Vault = Vault


class GlacierServiceResource(Boto3ServiceResource):
    """
    [Glacier.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource)
    """

    vaults: ServiceResourceVaultsCollection

    def Account(self, id: str) -> _Account:
        """
        [ServiceResource.Account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.Account)
        """

    def Archive(self, account_id: str, vault_name: str, id: str) -> _Archive:
        """
        [ServiceResource.Archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.Archive)
        """

    def Job(self, account_id: str, vault_name: str, id: str) -> _Job:
        """
        [ServiceResource.Job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.Job)
        """

    def MultipartUpload(self, account_id: str, vault_name: str, id: str) -> _MultipartUpload:
        """
        [ServiceResource.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.MultipartUpload)
        """

    def Notification(self, account_id: str, vault_name: str) -> _Notification:
        """
        [ServiceResource.Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.Notification)
        """

    def Vault(self, account_id: str, name: str) -> _Vault:
        """
        [ServiceResource.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.Vault)
        """

    def create_vault(self, accountId: str, vaultName: str) -> _Vault:
        """
        [ServiceResource.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.create_vault)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/glacier.html#Glacier.ServiceResource.get_available_subresources)
        """
