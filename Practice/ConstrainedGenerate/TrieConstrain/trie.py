
# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.


from typing import Dict, List

try:
    import marisa_trie
except ModuleNotFoundError:
    pass


class Trie(object):
    def __init__(self, sequences: List[List[int]] = []):