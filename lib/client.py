#!/usr/bin/env python
#encoding: utf-8
#author:zeroyu
#project:https://github.com/zer0yu/ZEROScan

import os.path
import lib.parse.parser import parseCmdOptions

def  main():
	
	try:
        paths.ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) #返回文件路径
        try:
            os.path.isdir(paths.ROOT_PATH) #判断路径是否为目录
        except UnicodeEncodeError:
            errMsg = "your system does not properly handle non-ASCII paths. "
            errMsg += "Please move the project root directory to another location"
            logger.error(errMsg)
            raise SystemExit
        setPaths()

        cmdLineOptions.update(parseCmdOptions().__dict__)
        initOptions(cmdLineOptions)

        if IS_WIN:
            winowsColorInit()
        banner()

        if conf.DEBUG:
            showDebugData()

        loadModule()
        loadPayloads()

        run()

        if conf.OPEN_BROWSER:
            openBrowser()

        systemQuit(EXIT_STATUS.SYSETM_EXIT)

    except ToolkitMissingPrivileges, e:
        logger.error(e)
        systemQuit(EXIT_STATUS.ERROR_EXIT)
    except ToolkitSystemException, e:
        logger.error(e)
        systemQuit(EXIT_STATUS.ERROR_EXIT)

    except ToolkitUserQuitException:
        systemQuit(EXIT_STATUS.USER_QUIT)
    except KeyboardInterrupt:
        systemQuit(EXIT_STATUS.USER_QUIT)


if __name__ == "__main__":
    main()