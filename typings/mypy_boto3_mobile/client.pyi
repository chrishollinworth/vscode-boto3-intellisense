# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for mobile service client

Usage::

    ```python
    import boto3
    from mypy_boto3_mobile import MobileClient

    client: MobileClient = boto3.client("mobile")
    ```
"""
import sys
from typing import IO, Any, Dict, Type, Union, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_mobile.paginator import ListBundlesPaginator, ListProjectsPaginator
from mypy_boto3_mobile.type_defs import (
    CreateProjectResultTypeDef,
    DeleteProjectResultTypeDef,
    DescribeBundleResultTypeDef,
    DescribeProjectResultTypeDef,
    ExportBundleResultTypeDef,
    ExportProjectResultTypeDef,
    ListBundlesResultTypeDef,
    ListProjectsResultTypeDef,
    UpdateProjectResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MobileClient",)


class Exceptions:
    AccountActionRequiredException: Type[Boto3ClientError]
    BadRequestException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    InternalFailureException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    NotFoundException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]
    TooManyRequestsException: Type[Boto3ClientError]
    UnauthorizedException: Type[Boto3ClientError]


class MobileClient:
    """
    [Mobile.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Client.can_paginate)
        """

    def create_project(
        self,
        name: str = None,
        region: str = None,
        contents: Union[bytes, IO[bytes]] = None,
        snapshotId: str = None,
    ) -> CreateProjectResultTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Client.create_project)
        """

    def delete_project(self, projectId: str) -> DeleteProjectResultTypeDef:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Client.delete_project)
        """

    def describe_bundle(self, bundleId: str) -> DescribeBundleResultTypeDef:
        """
        [Client.describe_bundle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Client.describe_bundle)
        """

    def describe_project(
        self, projectId: str, syncFromResources: bool = None
    ) -> DescribeProjectResultTypeDef:
        """
        [Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Client.describe_project)
        """

    def export_bundle(
        self,
        bundleId: str,
        projectId: str = None,
        platform: Literal[
            "OSX", "WINDOWS", "LINUX", "OBJC", "SWIFT", "ANDROID", "JAVASCRIPT"
        ] = None,
    ) -> ExportBundleResultTypeDef:
        """
        [Client.export_bundle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Client.export_bundle)
        """

    def export_project(self, projectId: str) -> ExportProjectResultTypeDef:
        """
        [Client.export_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Client.export_project)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Client.generate_presigned_url)
        """

    def list_bundles(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListBundlesResultTypeDef:
        """
        [Client.list_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Client.list_bundles)
        """

    def list_projects(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListProjectsResultTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Client.list_projects)
        """

    def update_project(
        self, projectId: str, contents: Union[bytes, IO[bytes]] = None
    ) -> UpdateProjectResultTypeDef:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Client.update_project)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_bundles"]) -> ListBundlesPaginator:
        """
        [Paginator.ListBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Paginator.ListBundles)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/mobile.html#Mobile.Paginator.ListProjects)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
