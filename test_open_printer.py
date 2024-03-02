#!/usr/bin/python# -*- coding: UTF-8 -*-import timefrom commonlib.base_lib.mylog.mylog import logimport pytestfrom src.Common_Fun.mythred import exec_threadfrom src.TestCase.RcdcCase.WEB.printer_web.common_printer_web import *class TestOpenPrinter(object):    @pytest.mark.publish    @pytest.mark.case_level_0    @pytest.mark.case_type_function    def test_open_printer_01(self):        """        用例名称:输入正确的的参数，开启打印机配置成功，并正确按返回体返回，并查询校验        接口名称:开启打印机配置        用例作者:        测试点:输入正确的的参数，开启打印机配置成功，并正确按返回体返回，并查询校验        前置步骤:        执行步骤:        校验点:        """        result1 = common_open_printer(status='true')        printer_web_common_assert(result=result1, message=None, status="SUCCESS")        result2 = common_close_printer(status='false')        printer_web_common_assert(result=result2, message=None, status="SUCCESS")    @pytest.mark.publish    @pytest.mark.case_level_0    @pytest.mark.case_type_function    def test_open_printer_02(self):        """        用例名称:反复开启打印机配置300次，并查询校验最后一次是否打开成功        接口名称:开启打印机配置        用例作者:        测试点:反复开启打印机配置300次，并查询校验最后一次是否打开成功        前置步骤:        执行步骤:        校验点:        """        import gc        for i in range(300):            print("第{}次开启打印机".format(i))            result1 = common_open_printer(status='true')            printer_web_common_assert(result=result1, message=None, status="SUCCESS")            result2 = common_close_printer(status='false')            printer_web_common_assert(result=result2, message=None, status="SUCCESS")            del result1, result2            gc.collect()    @pytest.mark.publish    @pytest.mark.case_level_0    @pytest.mark.case_type_function    def test_open_printer_03(self):        """        用例名称:在打印机配置已经开启的情况下，开启打印机配置，并查询校验，仍提示开启成功        接口名称:开启打印机配置        用例作者:        测试点:在打印机配置已经开启的情况下，开启打印机配置，并查询校验，仍提示开启成功        前置步骤:        执行步骤:        校验点:        """        result = common_open_printer(status='true')        printer_web_common_assert(result=result, message=None, status="SUCCESS")        result1 = common_open_printer(status='true')        printer_web_common_assert(result=result1, message=None, status="SUCCESS")        result2 = common_close_printer(status='false')        printer_web_common_assert(result=result2, message=None, status="SUCCESS")    @pytest.mark.publish    @pytest.mark.case_level_0    @pytest.mark.case_type_function    def test_open_printer_04(self):        """        用例名称:开启打印机配置接口返回时间超过3秒，报异常        接口名称:开启打印机配置        用例作者:        测试点:开启打印机配置接口返回时间超过3秒，报异常        前置步骤:        执行步骤:        校验点:        """        result1 = common_open_printer(status='true')        t1 = time.time()        printer_web_common_assert(result=result1, message=None, status="SUCCESS")        t2 = time.time()        assert t2 - t1 < 3, '返回时间超过3秒'    # @pytest.mark.unpublish    # @pytest.mark.case_level_0    # @pytest.mark.case_type_function    # def test_open_printer_05(self):    #     """    #     用例名称:无异常码，只返回成功和失败    #     接口名称:开启打印机配置    #     用例作者:    #     测试点:无异常码，只返回成功和失败    #     前置步骤:    #     执行步骤:    #     校验点:    #     """    #     result = common_open_printer()    #     printer_web_common_assert(result=result)    #     无异常码，无需覆盖    # @pytest.mark.unpublish    # @pytest.mark.case_level_1    # @pytest.mark.case_type_scene    # def test_open_printer_06(self):    #     """    #     用例名称:接口访问是否经过身份认证（即cookie或者证书的认证）    #     接口名称:开启打印机配置    #     用例作者:    #     测试点:接口访问是否经过身份认证（即cookie或者证书的认证）    #     前置步骤:    #     执行步骤:    #     校验点:    #     """    #     result = common_open_printer()    #     printer_web_common_assert(result=result)    # @pytest.mark.unpublish    # @pytest.mark.case_level_1    # @pytest.mark.case_type_scene    # def test_open_printer_07(self):    #     """    #     用例名称:admin用户接口访问成功    #     接口名称:开启打印机配置    #     用例作者:    #     测试点:admin用户接口访问成功    #     前置步骤:    #     执行步骤:    #     校验点:    #     """    #     result = common_open_printer()    #     printer_web_common_assert(result=result)    #     5.3未实现接口层面分级分权,不覆盖    # @pytest.mark.unpublish    # @pytest.mark.case_level_2    # @pytest.mark.case_type_performance    # def test_open_printer_08(self):    #     """    #     用例名称:接口响应时间不超过3秒    #     接口名称:开启打印机配置    #     用例作者:    #     测试点:接口响应时间不超过3秒    #     前置步骤:    #     执行步骤:    #     校验点:    #     """    #     result = common_open_printer()    #     printer_web_common_assert(result=result)    #     上述覆盖test_open_printer_04    @pytest.mark.unpublish    @pytest.mark.case_level_2    @pytest.mark.case_type_performance    def test_open_printer_09(self):        """        用例名称:并发执行200次        接口名称:开启打印机配置        用例作者:        测试点:并发执行200次        前置步骤:        执行步骤:        校验点:        """        data_list = []        for i in range(200):            data_list.append(['true'])        result_list = exec_thread(common_open_printer, data_list)        for result in result_list:            printer_web_common_assert(result=result, message=None, status="SUCCESS")