# Copyright (c) 2013 Rackspace Hosting, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Marconi Unit-ish Tests"""

from marconi.tests import base
from marconi.tests import helpers


SKIP_SLOW_TESTS = helpers.SKIP_SLOW_TESTS
RUN_SLOW_TESTS = not SKIP_SLOW_TESTS

expect = helpers.expect
is_slow = helpers.is_slow
requires_mongodb = helpers.requires_mongodb
TestBase = base.TestBase
