import subprocess, time, json

from frontend.stderr import *


def dump_configs():
    configs['testlist'] = testlist
    os.chdir(configs['proj_path'])
    config_file = os.path.join(configs['proj_path'], 'configs.json')
    logging.info(f'Dumping configs: {config_file}')
    with open(config_file, 'w', encoding='UTF-8') as f:
        json.dump(configs, f)


def run_cmd(cmd, redirect_to_file=False, stdout_f=''):
    logging.debug(f'Command: {" ".join(cmd)}')
    if redirect_to_file:
        with open(stdout_f, 'w', encoding='UTF-8') as f:
            cmd_run = subprocess.run(cmd, text=True, stdout=f)
    else:
        cmd_run = subprocess.run(cmd, capture_output=True, text=True)
    if cmd_run.returncode:
        logging.info(cmd_run.returncode)
        logging.error(cmd_run.stderr)
        stderr['error'] = cmd_run.stderr
        stderr['halt_exec'] = True
        open_stderr_window()
        while stderr['halt_exec']:
            time.sleep(0.1)
    elif cmd_run.stderr:
        logging.debug(cmd_run.stderr)
    else:
        logging.debug(cmd_run.stdout)


def gen_disasm(obj_path, dump_path):
    run_cmd(['riscv64-unknown-elf-objdump', '-d', obj_path], redirect_to_file=True, stdout_f=dump_path)
    logging.info('Generated disassembly')


def dut_run_test(obj_path, disasm_dump_path):
    gen_disasm(obj_path, disasm_dump_path)
    os.chdir(configs['dut_path'])
    run_cmd(configs['dut_cmd'].split())
