import ldfparser
ldf = ldfparser.parse_ldf(path = r"D:\IDE\libTSCANApi\DataBases\LINDemo.ldf")

Frame0 = ldf.get_frame(21)
print(Frame0)
# MessageData = Frame0.encode_raw({'SteeringLampControl': 1, 'HeadLampControl': 3, 'WiperControl': 2})
MessageData = Frame0.encode_raw({'HeadLampControl': 3, 'WiperControl': 2})
print(MessageData)
for idx in ldf.get_schedule_tables():
    print(idx)

class TSLDF():
    def __init__(self,ldfName:str) -> None:
        self.ldfName = ldfName
        self.TSLdf = ldfparser.parse_ldf(path = self.ldfName)
        self.TSLINbaudrate = self.TSLdf.baudrate
        self.TSLINFrames = {}
        for frame in self.TSLdf.frames:
            self.TSLINFrames[frame.name] = frame
        # self.TSLINFrames = self.TSLdf.frames
        self.TSSignals = {}
        for signal in self.TSLdf.signals:
            self.TSSignals[signal.name] = signal
        self.MasterName = self.TSLdf.master.name
        self.Schedules = {}
        Schedules = self.TSLdf.get_schedule_tables()
        for Schedule in Schedules:
            self.Schedules[Schedule.name] = Schedule
    def get_frame_signals_value(self,frame,data:bytearray):
        return self.TSLdf.get_frame(frame).decode_raw(data)
    def set_frame_signals_value(self,frame,valuedict):
        pass

A = TSLDF(r"D:\IDE\libTSCANApi\DataBases\LINDemo.ldf")
print(A)




# print(ldf.frames)
