from .TSStructure import *
from .TSCommon import *
import ldfparser
# ldf = ldfparser.parse_ldf(path = r"D:\IDE\libTSCANApi\DataBases\LINDemo.ldf")

# Frame0 = ldf.get_frame(21)
# print(Frame0)
# # MessageData = Frame0.encode_raw({'SteeringLampControl': 1, 'HeadLampControl': 3, 'WiperControl': 2})
# MessageData = Frame0.encode_raw({'HeadLampControl': 3, 'WiperControl': 2})
# print(MessageData)
# for idx in ldf.get_schedule_tables():
#     print(idx)

class TSLDF():
    def __init__(self,ldfName:str) -> None:
        self.ldfName = ldfName
        self.TSLdf = ldfparser.parse_ldf(path = self.ldfName)
        self.TSLINbaudrate = self.TSLdf.baudrate
        self.TSLINFrames = {}
        for frame in self.TSLdf.frames:
            self.TSLINFrames[frame.name] = {}
            self.TSLINFrames[frame.name]['ID'] = frame.frame_id
            self.TSLINFrames[frame.name]['ID'] = frame.length
            self.TSLINFrames[frame.name]['Signals'] = {}
            for AFSignal in frame.signal_map:
                ASignal = TSignal(FSgnType=0,FIsIntel=False,FStartBit=AFSignal[0],FLength=AFSignal[1].width,FFactor=1.0,FOffset=0)
                for AEncode in AFSignal[1].encoding_type._converters:
                    if type(AEncode) == ldfparser.encoding.PhysicalValue:
                        ASignal.FFactor = AEncode.scale
                        ASignal.FOffset = AEncode.offset
                self.TSLINFrames[frame.name]['Signals'][AFSignal[1].name] = {}
                self.TSLINFrames[frame.name]['Signals'][AFSignal[1].name]['Signal'] = ASignal
                self.TSLINFrames[frame.name]['Signals'][AFSignal[1].name]['InitValue'] = AFSignal[1].init_value
        # self.TSLINFrames = self.TSLdf.frames
        self.TSSignals = {}
        for signal in self.TSLdf.signals:
            self.TSSignals[signal.name] = signal
        self.MasterName = self.TSLdf.master.name
        self.Schedules = {}
        Schedules = self.TSLdf.get_schedule_tables()
        for Schedule in Schedules:
            self.Schedules[Schedule.name] = Schedule
    def get_frame_signals_value(self,frame:PLIN,data:bytearray):
        return self.TSLdf.get_frame(frame.FIdentifier).decode_raw(data)
    def set_frame_signals_value(self,frame:PLIN,SignalName:str,Value:double):
        AFrame = self.TSLdf.get_frame(frame.FIdentifier)
        if AFrame.name in self.TSLINFrames and SignalName in self.TSLINFrames[AFrame.name]['Signals']:
            set_signal_value(frame.FData,self.TSLINFrames[AFrame.name]['Signals'][SignalName]['Signal'],Value)
            # tsapp_transmit_lin_async()




# print(ldf.frames)
