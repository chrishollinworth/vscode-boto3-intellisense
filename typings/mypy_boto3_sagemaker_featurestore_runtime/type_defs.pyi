"""
Main interface for sagemaker-featurestore-runtime service type definitions.

Usage::

    ```python
    from mypy_boto3_sagemaker_featurestore_runtime.type_defs import FeatureValueTypeDef

    data: FeatureValueTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("FeatureValueTypeDef", "GetRecordResponseTypeDef")

FeatureValueTypeDef = TypedDict("FeatureValueTypeDef", {"FeatureName": str, "ValueAsString": str})

GetRecordResponseTypeDef = TypedDict(
    "GetRecordResponseTypeDef", {"Record": List["FeatureValueTypeDef"]}, total=False
)
