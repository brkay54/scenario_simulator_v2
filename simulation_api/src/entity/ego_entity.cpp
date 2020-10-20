// Copyright 2015-2020 Autoware Foundation. All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <simulation_api/entity/ego_entity.hpp>

#include <string>

namespace simulation_api
{
namespace entity
{
EgoEntity::EgoEntity(
  std::string name, const EntityStatus & initial_state,
  const pugi::xml_node & xml)
: VehicleEntity(name, initial_state, xml) {}
EgoEntity::EgoEntity(
  std::string name, const EntityStatus & initial_state,
  VehicleParameters parameters)
: VehicleEntity(name, initial_state, parameters) {}
EgoEntity::EgoEntity(std::string name, const pugi::xml_node & xml)
: VehicleEntity(name, xml) {}
EgoEntity::EgoEntity(std::string name, VehicleParameters parameters)
: VehicleEntity(name, parameters) {}
}  // namespace entity
}  // namespace simulation_api