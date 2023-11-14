"""
Type annotations for iot1click-devices service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/literals.html)

Usage::

    ```python
    from mypy_boto3_iot1click_devices.literals import ListDeviceEventsPaginatorName

    data: ListDeviceEventsPaginatorName = "list_device_events"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ListDeviceEventsPaginatorName", "ListDevicesPaginatorName")

ListDeviceEventsPaginatorName = Literal["list_device_events"]
ListDevicesPaginatorName = Literal["list_devices"]
