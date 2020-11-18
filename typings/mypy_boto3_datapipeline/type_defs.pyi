"""
Main interface for datapipeline service type definitions.

Usage::

    ```python
    from mypy_boto3_datapipeline.type_defs import FieldTypeDef

    data: FieldTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "FieldTypeDef",
    "OperatorTypeDef",
    "ParameterAttributeTypeDef",
    "ParameterObjectTypeDef",
    "ParameterValueTypeDef",
    "PipelineDescriptionTypeDef",
    "PipelineIdNameTypeDef",
    "PipelineObjectTypeDef",
    "ResponseMetadata",
    "SelectorTypeDef",
    "TagTypeDef",
    "TaskObjectTypeDef",
    "ValidationErrorTypeDef",
    "ValidationWarningTypeDef",
    "CreatePipelineOutputTypeDef",
    "DescribeObjectsOutputTypeDef",
    "DescribePipelinesOutputTypeDef",
    "EvaluateExpressionOutputTypeDef",
    "GetPipelineDefinitionOutputTypeDef",
    "InstanceIdentityTypeDef",
    "ListPipelinesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PollForTaskOutputTypeDef",
    "PutPipelineDefinitionOutputTypeDef",
    "QueryObjectsOutputTypeDef",
    "QueryTypeDef",
    "ReportTaskProgressOutputTypeDef",
    "ReportTaskRunnerHeartbeatOutputTypeDef",
    "ValidatePipelineDefinitionOutputTypeDef",
)

_RequiredFieldTypeDef = TypedDict("_RequiredFieldTypeDef", {"key": str})
_OptionalFieldTypeDef = TypedDict(
    "_OptionalFieldTypeDef", {"stringValue": str, "refValue": str}, total=False
)


class FieldTypeDef(_RequiredFieldTypeDef, _OptionalFieldTypeDef):
    pass


OperatorTypeDef = TypedDict(
    "OperatorTypeDef",
    {"type": Literal["EQ", "REF_EQ", "LE", "GE", "BETWEEN"], "values": List[str]},
    total=False,
)

ParameterAttributeTypeDef = TypedDict("ParameterAttributeTypeDef", {"key": str, "stringValue": str})

ParameterObjectTypeDef = TypedDict(
    "ParameterObjectTypeDef", {"id": str, "attributes": List["ParameterAttributeTypeDef"]}
)

ParameterValueTypeDef = TypedDict("ParameterValueTypeDef", {"id": str, "stringValue": str})

_RequiredPipelineDescriptionTypeDef = TypedDict(
    "_RequiredPipelineDescriptionTypeDef",
    {"pipelineId": str, "name": str, "fields": List["FieldTypeDef"]},
)
_OptionalPipelineDescriptionTypeDef = TypedDict(
    "_OptionalPipelineDescriptionTypeDef",
    {"description": str, "tags": List["TagTypeDef"]},
    total=False,
)


class PipelineDescriptionTypeDef(
    _RequiredPipelineDescriptionTypeDef, _OptionalPipelineDescriptionTypeDef
):
    pass


PipelineIdNameTypeDef = TypedDict("PipelineIdNameTypeDef", {"id": str, "name": str}, total=False)

PipelineObjectTypeDef = TypedDict(
    "PipelineObjectTypeDef", {"id": str, "name": str, "fields": List["FieldTypeDef"]}
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SelectorTypeDef = TypedDict(
    "SelectorTypeDef", {"fieldName": str, "operator": "OperatorTypeDef"}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str})

TaskObjectTypeDef = TypedDict(
    "TaskObjectTypeDef",
    {
        "taskId": str,
        "pipelineId": str,
        "attemptId": str,
        "objects": Dict[str, "PipelineObjectTypeDef"],
    },
    total=False,
)

ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef", {"id": str, "errors": List[str]}, total=False
)

ValidationWarningTypeDef = TypedDict(
    "ValidationWarningTypeDef", {"id": str, "warnings": List[str]}, total=False
)

_RequiredCreatePipelineOutputTypeDef = TypedDict(
    "_RequiredCreatePipelineOutputTypeDef", {"pipelineId": str}
)
_OptionalCreatePipelineOutputTypeDef = TypedDict(
    "_OptionalCreatePipelineOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class CreatePipelineOutputTypeDef(
    _RequiredCreatePipelineOutputTypeDef, _OptionalCreatePipelineOutputTypeDef
):
    pass


_RequiredDescribeObjectsOutputTypeDef = TypedDict(
    "_RequiredDescribeObjectsOutputTypeDef", {"pipelineObjects": List["PipelineObjectTypeDef"]}
)
_OptionalDescribeObjectsOutputTypeDef = TypedDict(
    "_OptionalDescribeObjectsOutputTypeDef",
    {"marker": str, "hasMoreResults": bool, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribeObjectsOutputTypeDef(
    _RequiredDescribeObjectsOutputTypeDef, _OptionalDescribeObjectsOutputTypeDef
):
    pass


_RequiredDescribePipelinesOutputTypeDef = TypedDict(
    "_RequiredDescribePipelinesOutputTypeDef",
    {"pipelineDescriptionList": List["PipelineDescriptionTypeDef"]},
)
_OptionalDescribePipelinesOutputTypeDef = TypedDict(
    "_OptionalDescribePipelinesOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class DescribePipelinesOutputTypeDef(
    _RequiredDescribePipelinesOutputTypeDef, _OptionalDescribePipelinesOutputTypeDef
):
    pass


_RequiredEvaluateExpressionOutputTypeDef = TypedDict(
    "_RequiredEvaluateExpressionOutputTypeDef", {"evaluatedExpression": str}
)
_OptionalEvaluateExpressionOutputTypeDef = TypedDict(
    "_OptionalEvaluateExpressionOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class EvaluateExpressionOutputTypeDef(
    _RequiredEvaluateExpressionOutputTypeDef, _OptionalEvaluateExpressionOutputTypeDef
):
    pass


GetPipelineDefinitionOutputTypeDef = TypedDict(
    "GetPipelineDefinitionOutputTypeDef",
    {
        "pipelineObjects": List["PipelineObjectTypeDef"],
        "parameterObjects": List["ParameterObjectTypeDef"],
        "parameterValues": List["ParameterValueTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

InstanceIdentityTypeDef = TypedDict(
    "InstanceIdentityTypeDef", {"document": str, "signature": str}, total=False
)

_RequiredListPipelinesOutputTypeDef = TypedDict(
    "_RequiredListPipelinesOutputTypeDef", {"pipelineIdList": List["PipelineIdNameTypeDef"]}
)
_OptionalListPipelinesOutputTypeDef = TypedDict(
    "_OptionalListPipelinesOutputTypeDef",
    {"marker": str, "hasMoreResults": bool, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListPipelinesOutputTypeDef(
    _RequiredListPipelinesOutputTypeDef, _OptionalListPipelinesOutputTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PollForTaskOutputTypeDef = TypedDict(
    "PollForTaskOutputTypeDef",
    {"taskObject": "TaskObjectTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredPutPipelineDefinitionOutputTypeDef = TypedDict(
    "_RequiredPutPipelineDefinitionOutputTypeDef", {"errored": bool}
)
_OptionalPutPipelineDefinitionOutputTypeDef = TypedDict(
    "_OptionalPutPipelineDefinitionOutputTypeDef",
    {
        "validationErrors": List["ValidationErrorTypeDef"],
        "validationWarnings": List["ValidationWarningTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class PutPipelineDefinitionOutputTypeDef(
    _RequiredPutPipelineDefinitionOutputTypeDef, _OptionalPutPipelineDefinitionOutputTypeDef
):
    pass


QueryObjectsOutputTypeDef = TypedDict(
    "QueryObjectsOutputTypeDef",
    {
        "ids": List[str],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

QueryTypeDef = TypedDict("QueryTypeDef", {"selectors": List["SelectorTypeDef"]}, total=False)

_RequiredReportTaskProgressOutputTypeDef = TypedDict(
    "_RequiredReportTaskProgressOutputTypeDef", {"canceled": bool}
)
_OptionalReportTaskProgressOutputTypeDef = TypedDict(
    "_OptionalReportTaskProgressOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ReportTaskProgressOutputTypeDef(
    _RequiredReportTaskProgressOutputTypeDef, _OptionalReportTaskProgressOutputTypeDef
):
    pass


_RequiredReportTaskRunnerHeartbeatOutputTypeDef = TypedDict(
    "_RequiredReportTaskRunnerHeartbeatOutputTypeDef", {"terminate": bool}
)
_OptionalReportTaskRunnerHeartbeatOutputTypeDef = TypedDict(
    "_OptionalReportTaskRunnerHeartbeatOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ReportTaskRunnerHeartbeatOutputTypeDef(
    _RequiredReportTaskRunnerHeartbeatOutputTypeDef, _OptionalReportTaskRunnerHeartbeatOutputTypeDef
):
    pass


_RequiredValidatePipelineDefinitionOutputTypeDef = TypedDict(
    "_RequiredValidatePipelineDefinitionOutputTypeDef", {"errored": bool}
)
_OptionalValidatePipelineDefinitionOutputTypeDef = TypedDict(
    "_OptionalValidatePipelineDefinitionOutputTypeDef",
    {
        "validationErrors": List["ValidationErrorTypeDef"],
        "validationWarnings": List["ValidationWarningTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class ValidatePipelineDefinitionOutputTypeDef(
    _RequiredValidatePipelineDefinitionOutputTypeDef,
    _OptionalValidatePipelineDefinitionOutputTypeDef,
):
    pass
