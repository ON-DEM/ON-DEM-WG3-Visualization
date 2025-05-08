
#include <chrono>
#include <iostream>

#ifdef USE_MPI
#include <mpi.h>
#endif

#include <random>
#include <thread>
#include <vector>

#include "InSituAdaptor.h"

//----------------------------------------------------------------------------
void doStep(std::vector<double>& p, std::vector<double>& v, std::vector<int>& c, double deltaT)
{
  const double gravity[3] = { 0.0, 0.0, -9.81 };
  const double dampingCoeff = 0.99;
  for (size_t i = 0; i < p.size(); i++)
  {
    // apply gravity and damping on velocity
    v[i] = dampingCoeff * v[i] + deltaT * gravity[i % 3];

    // modify position according velocity
    p[i] += deltaT * v[i];

    // collision with bounding box
    if (p[i] < -1.0)
    {
      c[i / 3]++;
      p[i] = -2 - p[i];
      v[i] = -v[i] * 0.8;
    }
    if (p[i] > 1.0)
    {
      c[i / 3]++;
      p[i] = 2.0 - p[i];
      v[i] = -v[i] * 0.8;
    }
  }
}

bool initializeInSitu(int rank, const std::string& script)
{
  if (rank == 0 && script.empty())
  {
    std::cerr << "no script specified !" << std::endl;
    return false;
  }
  Adaptor::Initialize(script.c_str());

  if (rank == 0)
  {
    std::cout << "initialize catalyst with script: " << script.c_str() << std::endl;
  }
  return true;
}

void executeInSitu(std::vector<double> positions, std::vector<double> velocities,
  std::vector<int> collisions, double time, unsigned int timeStep)
{
  Adaptor::CoProcess(positions, velocities, collisions, time, timeStep);

}

void finalizeInSitu()
{
  Adaptor::Finalize();
}

//----------------------------------------------------------------------------
int main(int argc, char** argv)
{
  int size = 1;
  int rank = 0;

#ifdef USE_MPI
  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &size);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
#endif

  std::string particlesOption = "-p";
  int nbParticles = 1000;
  std::string delayOption = "-d";
  int delay = 0;
  std::string timestepsOption = "-t";
  unsigned int nbTimesteps = 100;
  std::string verboseOption = "-v";
  bool verbose = false;
  std::string helpOption = "-h";
  std::string script("");

  for (int i = 1; i < argc; i++)
  {
    if (particlesOption.compare(argv[i]) == 0 && i + 1 < argc)
    {
      i++;
      nbParticles = atoi(argv[i]);
    }
    else if (delayOption.compare(argv[i]) == 0 && i + 1 < argc)
    {
      i++;
      delay = atoi(argv[i]);
    }
    else if (timestepsOption.compare(argv[i]) == 0 && i + 1 < argc)
    {
      i++;
      nbTimesteps = atoi(argv[i]);
    }
    else if (verboseOption.compare(argv[i]) == 0)
    {
      verbose = true;
    }
    else if (helpOption.compare(argv[i]) == 0)
    {
      std::cout << "usage : " << argv[0] << " [options] <script>" << std::endl;
      const char* usage = R"(
        -d N : the delay to wait between each timesteps, in milliseconds. Default 0.
        -h : show this help.
        -p N : the number of particles. Default 1000.
        -t N : the number of timesteps to process.
        -v : active verbose mode.
        <script> : mandatory with catalyst, the python script to use for data processing.
        )";
      std::cout << usage << std::endl;

      return 1;
    }
    else
    {
      script = argv[i];
    }
  }

  if (!initializeInSitu(rank, script))
  {
    return EXIT_FAILURE;
  }

  std::vector<double> positions(3 * nbParticles);
  std::vector<double> velocities(3 * nbParticles);
  std::vector<int> collisions(nbParticles, 0);

  const double deltaTime = 0.01;
  double time = 0.0;

  std::random_device rd;
  std::mt19937 mt(rd());
  std::uniform_real_distribution<double> dist(-1.0, 1.0);

  // init
  for (int i = 0; i < nbParticles / size; i++)
  {
    positions[3 * i] = dist(mt) * 0.2;
    positions[3 * i + 1] = dist(mt) * 0.2;
    positions[3 * i + 2] = dist(mt) * 0.2;
    velocities[3 * i] = dist(mt) * 4;
    velocities[3 * i + 1] = dist(mt) * 4;
    velocities[3 * i + 2] = dist(mt) * 4;
  }

  // simulation loop
  for (unsigned int timeStep = 0; timeStep < nbTimesteps; timeStep++)
  {
    time = deltaTime * timeStep;
    doStep(positions, velocities, collisions, deltaTime);

    executeInSitu(positions, velocities, collisions, time, timeStep);

    if (verbose && rank == 0 && timeStep % (nbTimesteps / 10) == 0)
    {
      std::cout << "timeStep : " << timeStep << std::endl;
    }

    std::this_thread::sleep_for(std::chrono::milliseconds(delay));
  }

  if (verbose && rank == 0)
  {
    std::cout << "simulation ended !" << std::endl;
  }

  finalizeInSitu();

#ifdef USE_MPI
  MPI_Finalize();
#endif
  return 0;
}
