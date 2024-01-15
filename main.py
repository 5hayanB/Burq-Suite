import os, logging, webview

from globals import BURQ_SUITE_LOGS, windows
from frontend.exposed_functs import expose

# riscv_dv = import_module('riscv-dv.riscv_dv_interface')


if __name__ == '__main__':
    logging.basicConfig(
        filename=os.path.join(BURQ_SUITE_LOGS, 'burq_suite.log'),
        filemode='w',
        format='%(asctime)s %(levelname)-8s %(filename)s %(message)s',
        datefmt='%d %b %Y %H:%M:%S',
        level=logging.DEBUG
    )

    windows['main'] = webview.create_window(
        title='Burq Suite',
        # url='frontend/web/splash.html',
        # url='frontend/web/index.html',
        url='frontend/web/configs.html',
        width=1200,
        height=600,
        resizable=False
    )

    logging.info('Starting Burq Suite')
    webview.start(expose, [windows['main']], debug=False)