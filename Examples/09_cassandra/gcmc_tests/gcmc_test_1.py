from pysimm import system, cassandra
from collections import OrderedDict

# In order to run CASSANDRA GCMC one need to create the CASSANDRA object
css = cassandra.Cassandra()

# Read the some default CASSANDRA .inp parameters file
gcmcPropsRead = css.read_input('my_props_simple.inp')
gcmcPropsRead['Box_Info'] = OrderedDict([('box_count', 1), ('box_size', 45)])

# The prefix for the all files that will be created by this run
gcmcPropsRead['Run_Name'] = 'pure_co2'
gcmcPropsRead['Rcutoff_Low'] = 0.

# Set the gas (gas system) to be purged in a box
gas_sst = cassandra.McSystem(system.read_lammps('co2.lmps'), max_ins=2000, chem_pot=-27.34)

job = cassandra.GCMC(gas_sst, out_folder='gcmc_test_1', **gcmcPropsRead)
css.add_gcmc(job)
css.run()

job.tot_sst.write_lammps('hydrogens.lmps')
# job.tot_sst.system.visualize()
