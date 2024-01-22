from globals import *
from frontend.exposed_functs import *


if __name__ == '__main__':
    logging.basicConfig(
        filename=os.path.join(BURQ_SUITE_LOGS, 'burq_suite.log'),
        filemode='w',
        format='%(asctime)s %(levelname)-8s %(filename)s %(message)s',
        datefmt='%d %b %Y %H:%M:%S',
        level=loglevel
    )

    windows['main'] = webview.create_window(
        title='Burq Suite',
        # url='frontend/web/splash.html',
        url='frontend/web/index.html',
        # url='frontend/web/configs.html',
        width=1200,
        height=600,
        resizable=False
    )

    logging.debug('Starting Burq Suite...')
    webview.start(expose, [windows['main']], debug=debug)
    logging.info('Burq Suite started')
