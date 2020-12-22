#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2020 Tier IV, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import yamale

from ament_index_python.packages import get_package_share_directory
from pathlib import Path
from re import sub
from sys import exit, stderr
from yaml import safe_load


def resolve_ros_package(pathname: str):

    def replace(match):
        return get_package_share_directory(match.group(1))

    return sub("\\$\\(find-pkg-share\\s+([^\\)]+)\\)", replace, pathname)


class Workflow():
    """
    Manages a set of scenario test items given as workflow.yaml.

    Attributes
    ----------
    path : Path
        The path to the given workflow file.

    scenarios : List[str]

    """

    def __init__(self, path: Path):

        self.path = path

        self.schema = yamale.make_schema(
            Path(get_package_share_directory('scenario_test_utility')).parent.joinpath(
                'ament_index', 'resource_index', 'packages', 'workflow_schema.yaml'))

        self.scenarios = self.read(self.path)

    def validate(self, path: Path):
        """
        Validate workflow file.

        Arguments
        ---------
        path : Path
            Path to the workflow file.

        Returns
        -------
        None

        """
        try:
            yamale.validate(self.schema, yamale.make_data(path))

        except yamale.yamale_error.YamaleError:
            exit(1)

    def read(self, workflow_path: Path):
        """
        Safely load workflow files.

        Arguments
        ---------
        workflow_path : Path
            Path to the workflow file.

        Returns
        -------
        scenarios : List[str]

        """
        self.validate(workflow_path)

        if workflow_path.exists():
            with workflow_path.open('r') as file:

                database = safe_load(file) \
                    if workflow_path.suffix == ".yaml" else file.read()

                scenarios = []

                for each in database['Scenario']:
                    each['path'] = str(Path(resolve_ros_package(each['path'])).resolve())
                    scenarios.append(each)

                return scenarios

        else:
            print("No such file or directory: " + str(workflow_path), file=stderr)
            exit(1)


if __name__ == '__main__':
    """Entrypoint."""
    pass
