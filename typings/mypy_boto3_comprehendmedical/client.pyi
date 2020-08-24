# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for comprehendmedical service client

Usage::

    ```python
    import boto3
    from mypy_boto3_comprehendmedical import ComprehendMedicalClient

    client: ComprehendMedicalClient = boto3.client("comprehendmedical")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_comprehendmedical.type_defs import (
    ComprehendMedicalAsyncJobFilterTypeDef,
    DescribeEntitiesDetectionV2JobResponseTypeDef,
    DescribeICD10CMInferenceJobResponseTypeDef,
    DescribePHIDetectionJobResponseTypeDef,
    DescribeRxNormInferenceJobResponseTypeDef,
    DetectEntitiesResponseTypeDef,
    DetectEntitiesV2ResponseTypeDef,
    DetectPHIResponseTypeDef,
    InferICD10CMResponseTypeDef,
    InferRxNormResponseTypeDef,
    InputDataConfigTypeDef,
    ListEntitiesDetectionV2JobsResponseTypeDef,
    ListICD10CMInferenceJobsResponseTypeDef,
    ListPHIDetectionJobsResponseTypeDef,
    ListRxNormInferenceJobsResponseTypeDef,
    OutputDataConfigTypeDef,
    StartEntitiesDetectionV2JobResponseTypeDef,
    StartICD10CMInferenceJobResponseTypeDef,
    StartPHIDetectionJobResponseTypeDef,
    StartRxNormInferenceJobResponseTypeDef,
    StopEntitiesDetectionV2JobResponseTypeDef,
    StopICD10CMInferenceJobResponseTypeDef,
    StopPHIDetectionJobResponseTypeDef,
    StopRxNormInferenceJobResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ComprehendMedicalClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    InternalServerException: Type[Boto3ClientError]
    InvalidEncodingException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]
    TextSizeLimitExceededException: Type[Boto3ClientError]
    TooManyRequestsException: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]


class ComprehendMedicalClient:
    """
    [ComprehendMedical.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.can_paginate)
        """

    def describe_entities_detection_v2_job(
        self, JobId: str
    ) -> DescribeEntitiesDetectionV2JobResponseTypeDef:
        """
        [Client.describe_entities_detection_v2_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_entities_detection_v2_job)
        """

    def describe_icd10_cm_inference_job(
        self, JobId: str
    ) -> DescribeICD10CMInferenceJobResponseTypeDef:
        """
        [Client.describe_icd10_cm_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_icd10_cm_inference_job)
        """

    def describe_phi_detection_job(self, JobId: str) -> DescribePHIDetectionJobResponseTypeDef:
        """
        [Client.describe_phi_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_phi_detection_job)
        """

    def describe_rx_norm_inference_job(
        self, JobId: str
    ) -> DescribeRxNormInferenceJobResponseTypeDef:
        """
        [Client.describe_rx_norm_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_rx_norm_inference_job)
        """

    def detect_entities(self, Text: str) -> DetectEntitiesResponseTypeDef:
        """
        [Client.detect_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.detect_entities)
        """

    def detect_entities_v2(self, Text: str) -> DetectEntitiesV2ResponseTypeDef:
        """
        [Client.detect_entities_v2 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.detect_entities_v2)
        """

    def detect_phi(self, Text: str) -> DetectPHIResponseTypeDef:
        """
        [Client.detect_phi documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.detect_phi)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.generate_presigned_url)
        """

    def infer_icd10_cm(self, Text: str) -> InferICD10CMResponseTypeDef:
        """
        [Client.infer_icd10_cm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.infer_icd10_cm)
        """

    def infer_rx_norm(self, Text: str) -> InferRxNormResponseTypeDef:
        """
        [Client.infer_rx_norm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.infer_rx_norm)
        """

    def list_entities_detection_v2_jobs(
        self,
        Filter: ComprehendMedicalAsyncJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListEntitiesDetectionV2JobsResponseTypeDef:
        """
        [Client.list_entities_detection_v2_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_entities_detection_v2_jobs)
        """

    def list_icd10_cm_inference_jobs(
        self,
        Filter: ComprehendMedicalAsyncJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListICD10CMInferenceJobsResponseTypeDef:
        """
        [Client.list_icd10_cm_inference_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_icd10_cm_inference_jobs)
        """

    def list_phi_detection_jobs(
        self,
        Filter: ComprehendMedicalAsyncJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListPHIDetectionJobsResponseTypeDef:
        """
        [Client.list_phi_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_phi_detection_jobs)
        """

    def list_rx_norm_inference_jobs(
        self,
        Filter: ComprehendMedicalAsyncJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListRxNormInferenceJobsResponseTypeDef:
        """
        [Client.list_rx_norm_inference_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_rx_norm_inference_jobs)
        """

    def start_entities_detection_v2_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: Literal["en"],
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None,
    ) -> StartEntitiesDetectionV2JobResponseTypeDef:
        """
        [Client.start_entities_detection_v2_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_entities_detection_v2_job)
        """

    def start_icd10_cm_inference_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: Literal["en"],
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None,
    ) -> StartICD10CMInferenceJobResponseTypeDef:
        """
        [Client.start_icd10_cm_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_icd10_cm_inference_job)
        """

    def start_phi_detection_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: Literal["en"],
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None,
    ) -> StartPHIDetectionJobResponseTypeDef:
        """
        [Client.start_phi_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_phi_detection_job)
        """

    def start_rx_norm_inference_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: Literal["en"],
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None,
    ) -> StartRxNormInferenceJobResponseTypeDef:
        """
        [Client.start_rx_norm_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_rx_norm_inference_job)
        """

    def stop_entities_detection_v2_job(
        self, JobId: str
    ) -> StopEntitiesDetectionV2JobResponseTypeDef:
        """
        [Client.stop_entities_detection_v2_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_entities_detection_v2_job)
        """

    def stop_icd10_cm_inference_job(self, JobId: str) -> StopICD10CMInferenceJobResponseTypeDef:
        """
        [Client.stop_icd10_cm_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_icd10_cm_inference_job)
        """

    def stop_phi_detection_job(self, JobId: str) -> StopPHIDetectionJobResponseTypeDef:
        """
        [Client.stop_phi_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_phi_detection_job)
        """

    def stop_rx_norm_inference_job(self, JobId: str) -> StopRxNormInferenceJobResponseTypeDef:
        """
        [Client.stop_rx_norm_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_rx_norm_inference_job)
        """
