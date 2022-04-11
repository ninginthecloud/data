# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from typing import List

# TODO: Add pyi generate script
class S3Handler:
    def __init__(self, request_timeout_ms: int, region: str) -> None: ...
    def s3_read(self, url: str) -> bytes: ...
    def list_files(self, prefix: str) -> List[str]: ...
    def set_buffer_size(self, buffer_size: int) -> None: ...
    def set_multi_part_download(self, multi_part_download: bool) -> None: ...
    def clear_marker(self) -> None: ...
