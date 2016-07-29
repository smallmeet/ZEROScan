#!/usr/bin/env python
#encoding: utf-8
#author:zeroyu
#project:https://github.com/zer0yu/ZEROScan

import argparse
import sys
from lib.core.setting import VERSION


def parseCmdOptions():
    parser = argparse.ArgumentParser(description='powered by zeroyu',
                                     usage='\n  python zeroscan.py [-T|-C] [-m NAME] [-s|-f|--api VALUE] [options]'
                                           '\n  python zeroscan.py [-h|-v|--show|--update]'
                                           '\n\nexample:\n'
                                           '  python zeroscan.py -T -m Flash_sql -u http://zeroyu.xyz\n'
                                           '  python zeroscan.py -T -m test -f ./dic/ip.txt\n'
                                           '  python zeroscan.py -T -m test --api --zoom "port:21" --max-page 5\n',
                                     add_help=False)

    engine = parser.add_argument_group('engine')#并发引擎
    engine.add_argument('-T', default=False, action='store_true',
                        help='load Multi-Threaded engine')

    engine.add_argument('-C', default=False, action='store_true',
                        help='load Coroutine engine (single-threaded with asynchronous)')

    engine.add_argument('-t', metavar='NUM', type=int, default=10,
                        help='num of threads/concurrent, 10 by default')

    module = parser.add_argument_group('module')#扫描模块

    module.add_argument('-m', metavar='NAME', type=str, default='',
                        help='select Module/POC name in ./module/ (without ".py")')

    target = parser.add_argument_group('target mode')#目标

    target.add_argument('-u', metavar='TARGET', type=str, default='',
                        help="scan a single target (e.g. www.wooyun.org)")
    target.add_argument('-f', metavar='FILE', type=str, default='',
                        help='load targets from TargetFile (e.g. ./data/wooyun_domain)')
    target.add_argument('--api', default=False, action='store_true',
                        help='get targets from ZoomEye API.')

    optimization = parser.add_argument_group('optimization')

    optimization.add_argument('-o', metavar='FILE', type=str, default='',
                              help='output file path&name. default in ./output/')
    optimization.add_argument('--single', default=False, action='store_true',
                              help='exit after finding the first victim/password.')
    optimization.add_argument('--nF', default=True, action='store_false',
                              help='disable file output')
    optimization.add_argument('--nS', default=True, action='store_false',
                              help='disable screen output')
    optimization.add_argument('--show', default=False, action='store_true',
                              help='show available module/POC names and exit')
    optimization.add_argument('--browser', default=False, action='store_true',
                              help='Open notepad or web browser to view report after task finished.')
    optimization.add_argument('--debug', default=False, action='store_true',
                              help='show more details while running')
    optimization.add_argument('--update', default=False, action='store_true',
                              help='update POC-T from github')
    optimization.add_argument('-v', '--version', action='version', version=VERSION,
                              help="show program's version number and exit")
    optimization.add_argument('-h', '--help', action='help',
                              help='show this help message and exit')
    optimization.add_argument('-hc', '--helpCN', default=False, action='store_true',
                              help=u'打印中文帮助(show help message in Chinese)')

    ZoomeyeApi = parser.add_argument_group('ZoomEye API')
    ZoomeyeApi.add_argument("--dork", metavar='STRING', dest="dork", action="store", default=None,
                            help="ZoomEye dork used for search.")
    ZoomeyeApi.add_argument("--max-page", metavar='PAGE', dest="max_page", type=int, default=1,
                            help="(optional) Max page used in ZoomEye API (10 targets/Page, default:1).")
    ZoomeyeApi.add_argument("--search-type", metavar='TYPE', dest="search_type", action="store", default='host',
                            help="(optional) search type used in ZoomEye API, web or host (default:host)")

    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    return args
