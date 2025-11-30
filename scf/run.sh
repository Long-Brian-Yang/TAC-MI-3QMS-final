#!/bin/sh
#$ -cwd
#$ -l cpu_160=1
#$ -l h_rt=24:00:00
#$ -N BaZrO3_scf

# Path to the VASP executable
PRG=/gs/fs/tga-ishikawalab/vasp/vasp.6.4.3/bin/vasp_std

# Load modules
. /etc/profile.d/modules.sh
module load cuda
module load intel
module load intel-mpi

# Run VASP with 160 MPI processes
mpiexec.hydra -ppn 160 -n 160 ${PRG} > vasp.out

