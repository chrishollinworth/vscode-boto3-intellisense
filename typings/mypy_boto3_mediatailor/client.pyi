# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for mediatailor service client

Usage::

    ```python
    import boto3
    from mypy_boto3_mediatailor import MediaTailorClient

    client: MediaTailorClient = boto3.client("mediatailor")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_mediatailor.paginator import ListPlaybackConfigurationsPaginator
from mypy_boto3_mediatailor.type_defs import (
    AvailSuppressionTypeDef,
    BumperTypeDef,
    CdnConfigurationTypeDef,
    DashConfigurationForPutTypeDef,
    GetPlaybackConfigurationResponseTypeDef,
    ListPlaybackConfigurationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LivePreRollConfigurationTypeDef,
    ManifestProcessingRulesTypeDef,
    PutPlaybackConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaTailorClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]


class MediaTailorClient:
    """
    [MediaTailor.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Client.can_paginate)
        """

    def delete_playback_configuration(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_playback_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Client.delete_playback_configuration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Client.generate_presigned_url)
        """

    def get_playback_configuration(self, Name: str) -> GetPlaybackConfigurationResponseTypeDef:
        """
        [Client.get_playback_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Client.get_playback_configuration)
        """

    def list_playback_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListPlaybackConfigurationsResponseTypeDef:
        """
        [Client.list_playback_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Client.list_playback_configurations)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Client.list_tags_for_resource)
        """

    def put_playback_configuration(
        self,
        AdDecisionServerUrl: str = None,
        AvailSuppression: "AvailSuppressionTypeDef" = None,
        Bumper: "BumperTypeDef" = None,
        CdnConfiguration: "CdnConfigurationTypeDef" = None,
        DashConfiguration: DashConfigurationForPutTypeDef = None,
        LivePreRollConfiguration: "LivePreRollConfigurationTypeDef" = None,
        ManifestProcessingRules: "ManifestProcessingRulesTypeDef" = None,
        Name: str = None,
        PersonalizationThresholdSeconds: int = None,
        SlateAdUrl: str = None,
        Tags: Dict[str, str] = None,
        TranscodeProfileName: str = None,
        VideoContentSourceUrl: str = None,
    ) -> PutPlaybackConfigurationResponseTypeDef:
        """
        [Client.put_playback_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Client.put_playback_configuration)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Client.untag_resource)
        """

    def get_paginator(
        self, operation_name: Literal["list_playback_configurations"]
    ) -> ListPlaybackConfigurationsPaginator:
        """
        [Paginator.ListPlaybackConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations)
        """
