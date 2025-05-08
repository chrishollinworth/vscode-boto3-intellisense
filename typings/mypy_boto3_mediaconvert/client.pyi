"""
Type annotations for mediaconvert service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediaconvert.client import MediaConvertClient

    session = Session()
    client: MediaConvertClient = session.client("mediaconvert")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeEndpointsPaginator,
    ListJobsPaginator,
    ListJobTemplatesPaginator,
    ListPresetsPaginator,
    ListQueuesPaginator,
    ListVersionsPaginator,
    SearchJobsPaginator,
)
from .type_defs import (
    AssociateCertificateRequestTypeDef,
    CancelJobRequestTypeDef,
    CreateJobRequestTypeDef,
    CreateJobResponseTypeDef,
    CreateJobTemplateRequestTypeDef,
    CreateJobTemplateResponseTypeDef,
    CreatePresetRequestTypeDef,
    CreatePresetResponseTypeDef,
    CreateQueueRequestTypeDef,
    CreateQueueResponseTypeDef,
    DeleteJobTemplateRequestTypeDef,
    DeletePresetRequestTypeDef,
    DeleteQueueRequestTypeDef,
    DescribeEndpointsRequestTypeDef,
    DescribeEndpointsResponseTypeDef,
    DisassociateCertificateRequestTypeDef,
    GetJobRequestTypeDef,
    GetJobResponseTypeDef,
    GetJobTemplateRequestTypeDef,
    GetJobTemplateResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetPresetRequestTypeDef,
    GetPresetResponseTypeDef,
    GetQueueRequestTypeDef,
    GetQueueResponseTypeDef,
    ListJobsRequestTypeDef,
    ListJobsResponseTypeDef,
    ListJobTemplatesRequestTypeDef,
    ListJobTemplatesResponseTypeDef,
    ListPresetsRequestTypeDef,
    ListPresetsResponseTypeDef,
    ListQueuesRequestTypeDef,
    ListQueuesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVersionsRequestTypeDef,
    ListVersionsResponseTypeDef,
    ProbeRequestTypeDef,
    ProbeResponseTypeDef,
    PutPolicyRequestTypeDef,
    PutPolicyResponseTypeDef,
    SearchJobsRequestTypeDef,
    SearchJobsResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateJobTemplateRequestTypeDef,
    UpdateJobTemplateResponseTypeDef,
    UpdatePresetRequestTypeDef,
    UpdatePresetResponseTypeDef,
    UpdateQueueRequestTypeDef,
    UpdateQueueResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("MediaConvertClient",)

class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class MediaConvertClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaConvertClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#generate_presigned_url)
        """

    def associate_certificate(
        self, **kwargs: Unpack[AssociateCertificateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates an AWS Certificate Manager (ACM) Amazon Resource Name (ARN) with AWS
        Elemental MediaConvert.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/associate_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#associate_certificate)
        """

    def cancel_job(self, **kwargs: Unpack[CancelJobRequestTypeDef]) -> Dict[str, Any]:
        """
        Permanently cancel a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/cancel_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#cancel_job)
        """

    def create_job(self, **kwargs: Unpack[CreateJobRequestTypeDef]) -> CreateJobResponseTypeDef:
        """
        Create a new transcoding job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/create_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#create_job)
        """

    def create_job_template(
        self, **kwargs: Unpack[CreateJobTemplateRequestTypeDef]
    ) -> CreateJobTemplateResponseTypeDef:
        """
        Create a new job template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/create_job_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#create_job_template)
        """

    def create_preset(
        self, **kwargs: Unpack[CreatePresetRequestTypeDef]
    ) -> CreatePresetResponseTypeDef:
        """
        Create a new preset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/create_preset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#create_preset)
        """

    def create_queue(
        self, **kwargs: Unpack[CreateQueueRequestTypeDef]
    ) -> CreateQueueResponseTypeDef:
        """
        Create a new transcoding queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/create_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#create_queue)
        """

    def delete_job_template(
        self, **kwargs: Unpack[DeleteJobTemplateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Permanently delete a job template you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/delete_job_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#delete_job_template)
        """

    def delete_policy(self) -> Dict[str, Any]:
        """
        Permanently delete a policy that you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/delete_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#delete_policy)
        """

    def delete_preset(self, **kwargs: Unpack[DeletePresetRequestTypeDef]) -> Dict[str, Any]:
        """
        Permanently delete a preset you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/delete_preset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#delete_preset)
        """

    def delete_queue(self, **kwargs: Unpack[DeleteQueueRequestTypeDef]) -> Dict[str, Any]:
        """
        Permanently delete a queue you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/delete_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#delete_queue)
        """

    def describe_endpoints(
        self, **kwargs: Unpack[DescribeEndpointsRequestTypeDef]
    ) -> DescribeEndpointsResponseTypeDef:
        """
        Send a request with an empty body to the regional API endpoint to get your
        account API endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/describe_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#describe_endpoints)
        """

    def disassociate_certificate(
        self, **kwargs: Unpack[DisassociateCertificateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes an association between the Amazon Resource Name (ARN) of an AWS
        Certificate Manager (ACM) certificate and an AWS Elemental MediaConvert
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/disassociate_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#disassociate_certificate)
        """

    def get_job(self, **kwargs: Unpack[GetJobRequestTypeDef]) -> GetJobResponseTypeDef:
        """
        Retrieve the JSON for a specific transcoding job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/get_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#get_job)
        """

    def get_job_template(
        self, **kwargs: Unpack[GetJobTemplateRequestTypeDef]
    ) -> GetJobTemplateResponseTypeDef:
        """
        Retrieve the JSON for a specific job template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/get_job_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#get_job_template)
        """

    def get_policy(self) -> GetPolicyResponseTypeDef:
        """
        Retrieve the JSON for your policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/get_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#get_policy)
        """

    def get_preset(self, **kwargs: Unpack[GetPresetRequestTypeDef]) -> GetPresetResponseTypeDef:
        """
        Retrieve the JSON for a specific preset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/get_preset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#get_preset)
        """

    def get_queue(self, **kwargs: Unpack[GetQueueRequestTypeDef]) -> GetQueueResponseTypeDef:
        """
        Retrieve the JSON for a specific queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/get_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#get_queue)
        """

    def list_job_templates(
        self, **kwargs: Unpack[ListJobTemplatesRequestTypeDef]
    ) -> ListJobTemplatesResponseTypeDef:
        """
        Retrieve a JSON array of up to twenty of your job templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/list_job_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#list_job_templates)
        """

    def list_jobs(self, **kwargs: Unpack[ListJobsRequestTypeDef]) -> ListJobsResponseTypeDef:
        """
        Retrieve a JSON array of up to twenty of your most recently created jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/list_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#list_jobs)
        """

    def list_presets(
        self, **kwargs: Unpack[ListPresetsRequestTypeDef]
    ) -> ListPresetsResponseTypeDef:
        """
        Retrieve a JSON array of up to twenty of your presets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/list_presets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#list_presets)
        """

    def list_queues(self, **kwargs: Unpack[ListQueuesRequestTypeDef]) -> ListQueuesResponseTypeDef:
        """
        Retrieve a JSON array of up to twenty of your queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/list_queues.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#list_queues)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieve the tags for a MediaConvert resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#list_tags_for_resource)
        """

    def list_versions(
        self, **kwargs: Unpack[ListVersionsRequestTypeDef]
    ) -> ListVersionsResponseTypeDef:
        """
        Retrieve a JSON array of all available Job engine versions and the date they
        expire.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/list_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#list_versions)
        """

    def probe(self, **kwargs: Unpack[ProbeRequestTypeDef]) -> ProbeResponseTypeDef:
        """
        Use Probe to obtain detailed information about your input media files.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/probe.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#probe)
        """

    def put_policy(self, **kwargs: Unpack[PutPolicyRequestTypeDef]) -> PutPolicyResponseTypeDef:
        """
        Create or change your policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/put_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#put_policy)
        """

    def search_jobs(self, **kwargs: Unpack[SearchJobsRequestTypeDef]) -> SearchJobsResponseTypeDef:
        """
        Retrieve a JSON array that includes job details for up to twenty of your most
        recent jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/search_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#search_jobs)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Add tags to a MediaConvert queue, preset, or job template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Remove tags from a MediaConvert queue, preset, or job template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#untag_resource)
        """

    def update_job_template(
        self, **kwargs: Unpack[UpdateJobTemplateRequestTypeDef]
    ) -> UpdateJobTemplateResponseTypeDef:
        """
        Modify one of your existing job templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/update_job_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#update_job_template)
        """

    def update_preset(
        self, **kwargs: Unpack[UpdatePresetRequestTypeDef]
    ) -> UpdatePresetResponseTypeDef:
        """
        Modify one of your existing presets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/update_preset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#update_preset)
        """

    def update_queue(
        self, **kwargs: Unpack[UpdateQueueRequestTypeDef]
    ) -> UpdateQueueResponseTypeDef:
        """
        Modify one of your existing queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/update_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#update_queue)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_endpoints"]
    ) -> DescribeEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_job_templates"]
    ) -> ListJobTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_jobs"]
    ) -> ListJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_presets"]
    ) -> ListPresetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_queues"]
    ) -> ListQueuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_versions"]
    ) -> ListVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_jobs"]
    ) -> SearchJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/client/#get_paginator)
        """
