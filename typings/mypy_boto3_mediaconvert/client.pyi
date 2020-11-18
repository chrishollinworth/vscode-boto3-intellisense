# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for mediaconvert service client

Usage::

    ```python
    import boto3
    from mypy_boto3_mediaconvert import MediaConvertClient

    client: MediaConvertClient = boto3.client("mediaconvert")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_mediaconvert.paginator import (
    DescribeEndpointsPaginator,
    ListJobsPaginator,
    ListJobTemplatesPaginator,
    ListPresetsPaginator,
    ListQueuesPaginator,
)
from mypy_boto3_mediaconvert.type_defs import (
    AccelerationSettingsTypeDef,
    CreateJobResponseTypeDef,
    CreateJobTemplateResponseTypeDef,
    CreatePresetResponseTypeDef,
    CreateQueueResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    GetJobResponseTypeDef,
    GetJobTemplateResponseTypeDef,
    GetPresetResponseTypeDef,
    GetQueueResponseTypeDef,
    HopDestinationTypeDef,
    JobSettingsTypeDef,
    JobTemplateSettingsTypeDef,
    ListJobsResponseTypeDef,
    ListJobTemplatesResponseTypeDef,
    ListPresetsResponseTypeDef,
    ListQueuesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PresetSettingsTypeDef,
    ReservationPlanSettingsTypeDef,
    UpdateJobTemplateResponseTypeDef,
    UpdatePresetResponseTypeDef,
    UpdateQueueResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaConvertClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class MediaConvertClient:
    """
    [MediaConvert.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_certificate(self, Arn: str) -> Dict[str, Any]:
        """
        [Client.associate_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.associate_certificate)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.can_paginate)
        """

    def cancel_job(self, Id: str) -> Dict[str, Any]:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.cancel_job)
        """

    def create_job(
        self,
        Role: str,
        Settings: "JobSettingsTypeDef",
        AccelerationSettings: "AccelerationSettingsTypeDef" = None,
        BillingTagsSource: Literal["QUEUE", "PRESET", "JOB_TEMPLATE", "JOB"] = None,
        ClientRequestToken: str = None,
        HopDestinations: List["HopDestinationTypeDef"] = None,
        JobTemplate: str = None,
        Priority: int = None,
        Queue: str = None,
        SimulateReservedQueue: Literal["DISABLED", "ENABLED"] = None,
        StatusUpdateInterval: Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_15",
            "SECONDS_20",
            "SECONDS_30",
            "SECONDS_60",
            "SECONDS_120",
            "SECONDS_180",
            "SECONDS_240",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_600",
        ] = None,
        Tags: Dict[str, str] = None,
        UserMetadata: Dict[str, str] = None,
    ) -> CreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.create_job)
        """

    def create_job_template(
        self,
        Name: str,
        Settings: "JobTemplateSettingsTypeDef",
        AccelerationSettings: "AccelerationSettingsTypeDef" = None,
        Category: str = None,
        Description: str = None,
        HopDestinations: List["HopDestinationTypeDef"] = None,
        Priority: int = None,
        Queue: str = None,
        StatusUpdateInterval: Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_15",
            "SECONDS_20",
            "SECONDS_30",
            "SECONDS_60",
            "SECONDS_120",
            "SECONDS_180",
            "SECONDS_240",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_600",
        ] = None,
        Tags: Dict[str, str] = None,
    ) -> CreateJobTemplateResponseTypeDef:
        """
        [Client.create_job_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.create_job_template)
        """

    def create_preset(
        self,
        Name: str,
        Settings: "PresetSettingsTypeDef",
        Category: str = None,
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreatePresetResponseTypeDef:
        """
        [Client.create_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.create_preset)
        """

    def create_queue(
        self,
        Name: str,
        Description: str = None,
        PricingPlan: Literal["ON_DEMAND", "RESERVED"] = None,
        ReservationPlanSettings: ReservationPlanSettingsTypeDef = None,
        Status: Literal["ACTIVE", "PAUSED"] = None,
        Tags: Dict[str, str] = None,
    ) -> CreateQueueResponseTypeDef:
        """
        [Client.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.create_queue)
        """

    def delete_job_template(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_job_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.delete_job_template)
        """

    def delete_preset(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.delete_preset)
        """

    def delete_queue(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.delete_queue)
        """

    def describe_endpoints(
        self,
        MaxResults: int = None,
        Mode: Literal["DEFAULT", "GET_ONLY"] = None,
        NextToken: str = None,
    ) -> DescribeEndpointsResponseTypeDef:
        """
        [Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.describe_endpoints)
        """

    def disassociate_certificate(self, Arn: str) -> Dict[str, Any]:
        """
        [Client.disassociate_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.disassociate_certificate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.generate_presigned_url)
        """

    def get_job(self, Id: str) -> GetJobResponseTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.get_job)
        """

    def get_job_template(self, Name: str) -> GetJobTemplateResponseTypeDef:
        """
        [Client.get_job_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.get_job_template)
        """

    def get_preset(self, Name: str) -> GetPresetResponseTypeDef:
        """
        [Client.get_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.get_preset)
        """

    def get_queue(self, Name: str) -> GetQueueResponseTypeDef:
        """
        [Client.get_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.get_queue)
        """

    def list_job_templates(
        self,
        Category: str = None,
        ListBy: Literal["NAME", "CREATION_DATE", "SYSTEM"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
    ) -> ListJobTemplatesResponseTypeDef:
        """
        [Client.list_job_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.list_job_templates)
        """

    def list_jobs(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Queue: str = None,
        Status: Literal["SUBMITTED", "PROGRESSING", "COMPLETE", "CANCELED", "ERROR"] = None,
    ) -> ListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.list_jobs)
        """

    def list_presets(
        self,
        Category: str = None,
        ListBy: Literal["NAME", "CREATION_DATE", "SYSTEM"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
    ) -> ListPresetsResponseTypeDef:
        """
        [Client.list_presets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.list_presets)
        """

    def list_queues(
        self,
        ListBy: Literal["NAME", "CREATION_DATE"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
    ) -> ListQueuesResponseTypeDef:
        """
        [Client.list_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.list_queues)
        """

    def list_tags_for_resource(self, Arn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.list_tags_for_resource)
        """

    def tag_resource(self, Arn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.tag_resource)
        """

    def untag_resource(self, Arn: str, TagKeys: List[str] = None) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.untag_resource)
        """

    def update_job_template(
        self,
        Name: str,
        AccelerationSettings: "AccelerationSettingsTypeDef" = None,
        Category: str = None,
        Description: str = None,
        HopDestinations: List["HopDestinationTypeDef"] = None,
        Priority: int = None,
        Queue: str = None,
        Settings: "JobTemplateSettingsTypeDef" = None,
        StatusUpdateInterval: Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_15",
            "SECONDS_20",
            "SECONDS_30",
            "SECONDS_60",
            "SECONDS_120",
            "SECONDS_180",
            "SECONDS_240",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_600",
        ] = None,
    ) -> UpdateJobTemplateResponseTypeDef:
        """
        [Client.update_job_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.update_job_template)
        """

    def update_preset(
        self,
        Name: str,
        Category: str = None,
        Description: str = None,
        Settings: "PresetSettingsTypeDef" = None,
    ) -> UpdatePresetResponseTypeDef:
        """
        [Client.update_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.update_preset)
        """

    def update_queue(
        self,
        Name: str,
        Description: str = None,
        ReservationPlanSettings: ReservationPlanSettingsTypeDef = None,
        Status: Literal["ACTIVE", "PAUSED"] = None,
    ) -> UpdateQueueResponseTypeDef:
        """
        [Client.update_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Client.update_queue)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoints"]
    ) -> DescribeEndpointsPaginator:
        """
        [Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Paginator.DescribeEndpoints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_job_templates"]
    ) -> ListJobTemplatesPaginator:
        """
        [Paginator.ListJobTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobTemplates)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_presets"]) -> ListPresetsPaginator:
        """
        [Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Paginator.ListPresets)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_queues"]) -> ListQueuesPaginator:
        """
        [Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediaconvert.html#MediaConvert.Paginator.ListQueues)
        """
