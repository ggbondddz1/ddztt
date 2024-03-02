#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

import pytest

from src.Api_Lib.RcdcApi.WEB.printer_web import Printerweb
from src.TestCase.RcdcCase.WEB.printer_web.common_printer_web import common_open_printer, add_printer, \
    common_detail_printer, common_delete_printer, common_close_printer
from src.TestData.RcdcData.web_erreor_msg.print_error_msg import ERROER_MSG_01
from src.TestData.RcdcData.web_erreor_msg.printer_test_data import SHARE_MOE_SQL, data_name


@pytest.fixture()
def open_printer_testdata_SHARE():
   common_open_printer(status='true')
   print_id = add_printer(printer_info=SHARE_MOE_SQL.format(str(uuid.uuid4())))
   yield print_id
   common_delete_printer(idarr=[print_id], describe='成功', wait_time=10)


@pytest.fixture()
def open_printer_testdata1(request):
    """
    打开打印机并插入数据，结束后删除插入的数据
    :param request:
    :return:
    """
    param = request.param
    common_open_printer(status='true')
    print_id = add_printer(printer_info=SHARE_MOE_SQL.format(param[0]))
    yield print_id
    common_delete_printer(idarr=[print_id], describe='删除打印机配置[{}]成功'.format(data_name), wait_time=10)

@pytest.fixture()
def open_printer_testdata3(request):
    """
    打开打印机并插入数据，编辑打印机配置名，结束后删除插入的数据
    :param request:
    :return:
    """
    param = request.param
    common_open_printer(status='true')
    print_id = add_printer(printer_info=SHARE_MOE_SQL.format(param[0]))
    yield print_id
    common_delete_printer(idarr=[print_id], describe='删除打印机配置[修改后配置名]成功', wait_time=10)

@pytest.fixture()
def open_printer_testdata4(request):
    """
    打开打印机并插入数据，编辑打印机配置名，结束后删除插入的数据
    :param request:
    :return:
    """
    param = request.param
    common_open_printer(status='true')
    print_id = add_printer(printer_info=SHARE_MOE_SQL.format(param[0]))
    yield print_id
    common_delete_printer(idarr=[print_id], describe='删除打印机配置[修改后配置名10]成功', wait_time=10)

@pytest.fixture()
def open_printer_testdata5(request):
    """
    打开打印机并插入数据，结束后删除两个打印机的数据
    :param request:
    :return:
    """
    param = request.param
    common_open_printer(status='true')
    print_id = add_printer(printer_info=SHARE_MOE_SQL.format(param[0]))
    yield print_id
    common_delete_printer(idarr=[print_id], describe='删除打印机配置[{}]成功'.format(data_name), wait_time=10)
    common_delete_printer(idarr=['8c122bcb-bba8-4638-9cc7-854496d80d04'], describe='删除打印机配置[默认配置名1]成功', wait_time=10)
@pytest.fixture()
def open_printer_testdata2(request):
    """
    打开打印机并插入数据，结束后不删除插入到数据
    :param request:
    :return:
    """
    param = request.param
    common_open_printer(status='true')
    print_id = add_printer(printer_info=SHARE_MOE_SQL.format(param[0]))
    yield print_id




@pytest.fixture()
def close_printer_testdata():
    """
    结束后删除一个打印机数据
    :return:
    """
    yield
    common_delete_printer(idarr=['8c122bcb-bba8-4638-9cc7-854496d80d03'], describe=ERROER_MSG_01.format(1, 0),
                          wait_time=10)
    common_close_printer()


@pytest.fixture()
def close_printer_testdata1():
    """
    结束后删除两个打印机数据
    :return:
    """
    yield
    common_delete_printer(idarr=['8c122bcb-bba8-4638-9cc7-854496d80d03'], describe=ERROER_MSG_01.format(1, 0),
                          wait_time=10)
    common_delete_printer(idarr=['8c122bcb-bba8-4638-9cc7-854496d80d04'], describe=ERROER_MSG_01.format(1, 0),
                          wait_time=10)
    common_close_printer()


if __name__ == "__main__":
    pass
