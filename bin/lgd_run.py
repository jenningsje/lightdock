#!/usr/bin/env python3

"""Execution controller

Depending on the environment, executes a MPI or multiprocessing version.
"""

import traceback
from lightdock.util.logger import LoggingManager
from lightdock.util.parser import CommandLineParser


log = LoggingManager.get_logger("lgd_run")

print("in lgd_run")

if __name__ == "__main__":

    try:
        parser = CommandLineParser()
        mpi_support = parser.args.mpi
        if mpi_support:
            print("mpi_support")
            from lightdock.simulation.docking_mpi import (
                run_simulation as mpi_simulation,
            )
            print("before mpi_simulation")
            mpi_simulation(parser)
            print("after mpi_simulation")
        else:
            from lightdock.simulation.docking_multiprocessing import (
                run_simulation as multiprocessing_simulation,
            )
            print("before multiprocessing simulation")
            multiprocessing_simulation(parser)
            print("after multiprocessing simulation")

    except Exception:
        log.error("LightDock has failed, please check traceback:")
        traceback.print_exc()
