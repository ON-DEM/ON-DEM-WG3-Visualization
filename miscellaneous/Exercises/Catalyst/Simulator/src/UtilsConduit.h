/**
 * Utils file to create and update conduit objects
 */

#include <catalyst_conduit.hpp>
using conduit_node_t = conduit_cpp::Node;

#include <vector>

namespace Utils
{
bool BuildConduitDataDesc(conduit_node_t& state, double time, long timeStep);

bool BuildConduitDataStructure(conduit_node_t& mesh, std::vector<double>& pos,
  std::vector<double>& velocity, std::vector<int>& collisions);
}
