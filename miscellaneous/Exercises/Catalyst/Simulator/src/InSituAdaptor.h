#pragma once

#include <vector>

namespace Adaptor
{
// Memory allocation and analysis parameters
// return true if success
bool Initialize(const char* script);
// Memory cleanup
// return true if success
bool Finalize();
// Main method to call in the loop
// return true if success
bool CoProcess(std::vector<double>& pos, std::vector<double>& velocity,
  std::vector<int>& collisions, double time, unsigned int timeStep);
}
