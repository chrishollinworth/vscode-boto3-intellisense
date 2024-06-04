"""
Type annotations for oam service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/literals.html)

Usage::

    ```python
    from mypy_boto3_oam.literals import ListAttachedLinksPaginatorName

    data: ListAttachedLinksPaginatorName = "list_attached_links"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListAttachedLinksPaginatorName",
    "ListLinksPaginatorName",
    "ListSinksPaginatorName",
    "ResourceTypeType",
)

ListAttachedLinksPaginatorName = Literal["list_attached_links"]
ListLinksPaginatorName = Literal["list_links"]
ListSinksPaginatorName = Literal["list_sinks"]
ResourceTypeType = Literal[
    "AWS::ApplicationInsights::Application",
    "AWS::CloudWatch::Metric",
    "AWS::InternetMonitor::Monitor",
    "AWS::Logs::LogGroup",
    "AWS::XRay::Trace",
]
