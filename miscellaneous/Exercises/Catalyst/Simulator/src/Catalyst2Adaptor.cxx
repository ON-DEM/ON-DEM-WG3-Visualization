#include "InSituAdaptor.h"
#include "UtilsConduit.h"

#include <catalyst.h>
#include <catalyst_conduit.hpp>

#include <numeric>
#include <string>

namespace Adaptor
{

/**
 * In this example, we show how we can use Conduit's C++ API to
 * create Conduit nodes. This is not required. A C++ adaptor
 * can just as conveniently use the Conduit C API to setup
 * the `conduit_node`. However, this example shows that one can indeed
 * use the C++ API, if the developer so chooses.
 */

bool IsCatalystErrorCodeSuccess(catalyst_status error_code, const std::string& step_name = "")
{
  if (error_code != catalyst_status_ok)
  {
    if(!step_name.empty())
    {
      std::cerr << "[" << step_name << "]: ";
    }
    std::cerr << "Catalyst API call failed with error code: " << error_code << std::endl;
  }

  return error_code == catalyst_status_ok;
}

bool Initialize(const char* script)
{
  conduit_cpp::Node node;
  node["catalyst/scripts/script"].set_string(script);
  auto error_code = catalyst_initialize(conduit_cpp::c_node(&node));

  return IsCatalystErrorCodeSuccess(error_code, "Initialize");
}

bool CoProcess(std::vector<double>& pos, std::vector<double>& velocity,
  std::vector<int>& collisions, double time, unsigned int timeStep)
{
  conduit_cpp::Node exec_params;

  // add time/cycle information
  auto state = exec_params["catalyst/state"];
  Utils::BuildConduitDataDesc(state, time, timeStep);

  // Add channels.
  // We only have 1 channel here. Let's name it 'particles'.
  auto channel = exec_params["catalyst/channels/particles"];
  // Since this example is using Conduit Mesh Blueprint to define the mesh,
  // we set the channel's type to "mesh".
  channel["type"].set("mesh");
  // now create the mesh.
  auto mesh = channel["data"];

  Utils::BuildConduitDataStructure(mesh, pos, velocity, collisions);

  auto error_code = catalyst_execute(conduit_cpp::c_node(&exec_params));

  return IsCatalystErrorCodeSuccess(error_code, "Execute");
}

bool Finalize()
{
  conduit_cpp::Node node;
  auto error_code = catalyst_finalize(conduit_cpp::c_node(&node));

  return IsCatalystErrorCodeSuccess(error_code, "Finalize");
}
}
