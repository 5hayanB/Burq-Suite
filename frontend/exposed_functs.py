from importlib import import_module

from frontend.splash import *
from frontend.index import *
from frontend.configs import *
from frontend.test_results import *
# from frontend.project_browser import *

riscv_dv_interface = import_module('riscv-dv.riscv_dv_interface')


def expose(window):
    window.expose(
        # splash.py
        open_login,

        # index.py
        open_configs,
        select_proj_folder,
        open_proj,

        # configs.py
        get_dut_type,
        open_dut_menu,
        get_dir,
        select_target,
        set_csv_file,
        set_config,
        get_dut_name,
        get_iss,

        riscv_dv_interface.get_working_base_testlist,
        riscv_dv_interface.get_simulator_list,
        riscv_dv_interface.get_iss_list,
        riscv_dv_interface.riscv_dv_run_test
    )
