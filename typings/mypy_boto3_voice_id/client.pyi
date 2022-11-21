"""
Type annotations for voice-id service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_voice_id import VoiceIDClient

    client: VoiceIDClient = boto3.client("voice-id")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import FraudsterRegistrationJobStatusType, SpeakerEnrollmentJobStatusType
from .paginator import (
    ListDomainsPaginator,
    ListFraudsterRegistrationJobsPaginator,
    ListSpeakerEnrollmentJobsPaginator,
    ListSpeakersPaginator,
)
from .type_defs import (
    CreateDomainResponseTypeDef,
    DescribeDomainResponseTypeDef,
    DescribeFraudsterRegistrationJobResponseTypeDef,
    DescribeFraudsterResponseTypeDef,
    DescribeSpeakerEnrollmentJobResponseTypeDef,
    DescribeSpeakerResponseTypeDef,
    EnrollmentConfigTypeDef,
    EvaluateSessionResponseTypeDef,
    InputDataConfigTypeDef,
    ListDomainsResponseTypeDef,
    ListFraudsterRegistrationJobsResponseTypeDef,
    ListSpeakerEnrollmentJobsResponseTypeDef,
    ListSpeakersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OptOutSpeakerResponseTypeDef,
    OutputDataConfigTypeDef,
    RegistrationConfigTypeDef,
    ServerSideEncryptionConfigurationTypeDef,
    StartFraudsterRegistrationJobResponseTypeDef,
    StartSpeakerEnrollmentJobResponseTypeDef,
    TagTypeDef,
    UpdateDomainResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("VoiceIDClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class VoiceIDClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        VoiceIDClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#close)
        """
    def create_domain(
        self,
        *,
        Name: str,
        ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef",
        ClientToken: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDomainResponseTypeDef:
        """
        Creates a domain that contains all Amazon Connect Voice ID data, such as
        speakers, fraudsters, customer audio, and voiceprints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.create_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#create_domain)
        """
    def delete_domain(self, *, DomainId: str) -> None:
        """
        Deletes the specified domain from Voice ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.delete_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#delete_domain)
        """
    def delete_fraudster(self, *, DomainId: str, FraudsterId: str) -> None:
        """
        Deletes the specified fraudster from Voice ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.delete_fraudster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#delete_fraudster)
        """
    def delete_speaker(self, *, DomainId: str, SpeakerId: str) -> None:
        """
        Deletes the specified speaker from Voice ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.delete_speaker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#delete_speaker)
        """
    def describe_domain(self, *, DomainId: str) -> DescribeDomainResponseTypeDef:
        """
        Describes the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.describe_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#describe_domain)
        """
    def describe_fraudster(
        self, *, DomainId: str, FraudsterId: str
    ) -> DescribeFraudsterResponseTypeDef:
        """
        Describes the specified fraudster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.describe_fraudster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#describe_fraudster)
        """
    def describe_fraudster_registration_job(
        self, *, DomainId: str, JobId: str
    ) -> DescribeFraudsterRegistrationJobResponseTypeDef:
        """
        Describes the specified fraudster registration job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.describe_fraudster_registration_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#describe_fraudster_registration_job)
        """
    def describe_speaker(self, *, DomainId: str, SpeakerId: str) -> DescribeSpeakerResponseTypeDef:
        """
        Describes the specified speaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.describe_speaker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#describe_speaker)
        """
    def describe_speaker_enrollment_job(
        self, *, DomainId: str, JobId: str
    ) -> DescribeSpeakerEnrollmentJobResponseTypeDef:
        """
        Describes the specified speaker enrollment job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.describe_speaker_enrollment_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#describe_speaker_enrollment_job)
        """
    def evaluate_session(
        self, *, DomainId: str, SessionNameOrId: str
    ) -> EvaluateSessionResponseTypeDef:
        """
        Evaluates a specified session based on audio data accumulated during a streaming
        Amazon Connect Voice ID call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.evaluate_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#evaluate_session)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#generate_presigned_url)
        """
    def list_domains(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListDomainsResponseTypeDef:
        """
        Lists all the domains in the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.list_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#list_domains)
        """
    def list_fraudster_registration_jobs(
        self,
        *,
        DomainId: str,
        JobStatus: FraudsterRegistrationJobStatusType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListFraudsterRegistrationJobsResponseTypeDef:
        """
        Lists all the fraudster registration jobs in the domain with the given
        `JobStatus`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.list_fraudster_registration_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#list_fraudster_registration_jobs)
        """
    def list_speaker_enrollment_jobs(
        self,
        *,
        DomainId: str,
        JobStatus: SpeakerEnrollmentJobStatusType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListSpeakerEnrollmentJobsResponseTypeDef:
        """
        Lists all the speaker enrollment jobs in the domain with the specified
        `JobStatus`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.list_speaker_enrollment_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#list_speaker_enrollment_jobs)
        """
    def list_speakers(
        self, *, DomainId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListSpeakersResponseTypeDef:
        """
        Lists all speakers in a specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.list_speakers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#list_speakers)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a specified Voice ID resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#list_tags_for_resource)
        """
    def opt_out_speaker(self, *, DomainId: str, SpeakerId: str) -> OptOutSpeakerResponseTypeDef:
        """
        Opts out a speaker from Voice ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.opt_out_speaker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#opt_out_speaker)
        """
    def start_fraudster_registration_job(
        self,
        *,
        DataAccessRoleArn: str,
        DomainId: str,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        ClientToken: str = None,
        JobName: str = None,
        RegistrationConfig: "RegistrationConfigTypeDef" = None
    ) -> StartFraudsterRegistrationJobResponseTypeDef:
        """
        Starts a new batch fraudster registration job using provided details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.start_fraudster_registration_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#start_fraudster_registration_job)
        """
    def start_speaker_enrollment_job(
        self,
        *,
        DataAccessRoleArn: str,
        DomainId: str,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        ClientToken: str = None,
        EnrollmentConfig: "EnrollmentConfigTypeDef" = None,
        JobName: str = None
    ) -> StartSpeakerEnrollmentJobResponseTypeDef:
        """
        Starts a new batch speaker enrollment job using specified details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.start_speaker_enrollment_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#start_speaker_enrollment_job)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Tags a Voice ID resource with the provided list of tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes specified tags from a specified Amazon Connect Voice ID resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#untag_resource)
        """
    def update_domain(
        self,
        *,
        DomainId: str,
        Name: str,
        ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef",
        Description: str = None
    ) -> UpdateDomainResponseTypeDef:
        """
        Updates the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Client.update_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/client.html#update_domain)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Paginator.ListDomains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listdomainspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_fraudster_registration_jobs"]
    ) -> ListFraudsterRegistrationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Paginator.ListFraudsterRegistrationJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listfraudsterregistrationjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_speaker_enrollment_jobs"]
    ) -> ListSpeakerEnrollmentJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Paginator.ListSpeakerEnrollmentJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listspeakerenrollmentjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_speakers"]) -> ListSpeakersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/voice-id.html#VoiceID.Paginator.ListSpeakers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listspeakerspaginator)
        """
