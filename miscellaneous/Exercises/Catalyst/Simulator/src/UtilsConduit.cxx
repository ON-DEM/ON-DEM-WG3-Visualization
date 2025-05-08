#include "UtilsConduit.h"

#include <numeric>

namespace Utils
{

bool BuildConduitDataDesc(conduit_node_t& state, double time, long timeStep)
{
  state["timestep"].set(timeStep);
  state["time"].set(time);
  return true;
}

bool BuildConduitDataStructure(conduit_node_t& mesh, std::vector<double>& pos,
  std::vector<double>& velocity, std::vector<int>& collisions)
{
  mesh["coordsets/my_coords/type"].set("explicit");

  size_t nb_of_points = pos.size() / 3;
  mesh["coordsets/my_coords/values/x"].set_external(
    pos.data(), nb_of_points, /*offset=*/0, /*stride=*/3 * sizeof(double));
  mesh["coordsets/my_coords/values/y"].set_external(
    pos.data(), nb_of_points, /*offset=*/sizeof(double), /*stride=*/3 * sizeof(double));
  mesh["coordsets/my_coords/values/z"].set_external(
    pos.data(), nb_of_points, /*offset=*/2 * sizeof(double), /*stride=*/3 * sizeof(double));

  mesh["topologies/my_mesh/type"].set("unstructured");
  mesh["topologies/my_mesh/coordset"].set("my_coords");
  mesh["topologies/my_mesh/elements/shape"].set("point");
  std::vector<int> vertices(nb_of_points);
  std::iota(std::begin(vertices), std::end(vertices), 0);
  // take ownership of temporary vector
  mesh["topologies/my_mesh/elements/connectivity"].set(vertices.data(), vertices.size());

  // Finally, add fields.
  auto fields = mesh["fields"];
  fields["velocity/association"].set("vertex");
  fields["velocity/topology"].set("my_mesh");
  fields["velocity/volume_dependent"].set("false");

  // velocity is stored in non-interlaced form (unlike points).
  fields["velocity/values/x"].set_external(
    velocity.data(), nb_of_points, /*offset=*/0, /*stride=*/3 * sizeof(double));
  fields["velocity/values/y"].set_external(
    velocity.data(), nb_of_points, /*offset=*/sizeof(double), /*stride*/ 3 * sizeof(double));
  fields["velocity/values/z"].set_external(
    velocity.data(), nb_of_points, /*offset=*/2 * sizeof(double), /*stride*/ 3 * sizeof(double));

  // pressure is cell-data.
  fields["collisions/association"].set("element");
  fields["collisions/topology"].set("my_mesh");
  fields["collisions/volume_dependent"].set("false");
  fields["collisions/values"].set_external(collisions.data(), nb_of_points);
  return true;
}

} // end namespace Utils
