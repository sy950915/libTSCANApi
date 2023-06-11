'''
Author: seven 865762826@qq.com
Date: 2023-06-11 14:14:06
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-06-11 15:36:01
'''
import typing

from can.message import Message
from libTSCANAPI.TSMasterDevice import *
import can
from typing import List, Optional, Tuple, Union, Deque, Any
from can.bus import LOG


class libtosunBus(can.BusABC):
    def __init__(self, channel: Any = None, *,
                configs: typing.List[dict],
                is_include_tx=False,
                can_filters: Optional[can.typechecking.CanFilters] = None,
                hwserial: bytes = b"",
                dbc:str = '',
                filters = [],
                 **kwargs: object):
        super().__init__(channel, can_filters, **kwargs)
        self.device = TSMasterDevice(configs=configs, hwserial=hwserial,is_include_tx=is_include_tx,
        dbc=dbc,filters = filters)

    def send(self, msg: can.Message, timeout: Optional[float] = 0.1, sync: bool = False,
            is_cyclic: bool = False) -> None:
        self.device.send_msg(msg, timeout, sync, is_cyclic)

    def recv(self, channel=0, timeout: Optional[float] = 0.1) -> Message or None:
        return self._recv_internal(channel = channel,timeout=timeout)
    
    def _recv_internal(self, channel=0, timeout: Optional[float] = 0.1) -> Tuple[Optional[can.Message], bool] or Tuple[None,bool]:
        return self.device.recv(channel=channel,timeout = timeout), False

    def shutdown(self) -> None:
        LOG.debug('TSMaster - shutdown.')
        super().shutdown()
        finalize_lib_tscan()
