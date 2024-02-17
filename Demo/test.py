class TCANSignal:
    def __init__(self, FCANSgnType, FIsIntel, FStartBit, FLength, FFactor, FOffset):
        self.FCANSgnType = FCANSgnType
        self.FIsIntel = FIsIntel
        self.FStartBit = FStartBit
        self.FLength = FLength
        self.FFactor = FFactor
        self.FOffset = FOffset

def calc_real_startbit(startbit, bitlen):
    startbit ^= 7
    startbit += bitlen - 1
    startbit ^= 7
    return startbit

def get_signal_value(data, signal):
    AFristCount = 0
    AOtherCount = 0
    AByteIdx = 0
    AOtherByteCount = 0
    ARawValue = 0
    AMove = 0
    NowValue = 0
    AByteIdx = signal.FStartBit // 8
    AFristCount = (AByteIdx + 1) * 8 - signal.FStartBit
    AOtherCount = signal.FLength - AFristCount
    AOtherByteCount = AOtherCount // 8 if AOtherCount % 8 == 0 else AOtherCount // 8 + 1

    if not signal.FIsIntel:
        realStartbit = calc_real_startbit(signal.FStartBit, signal.FLength)
        AByteIdx = realStartbit // 8
        AFristCount = (AByteIdx + 1) * 8 - realStartbit
        AOtherCount = signal.FLength - AFristCount
        AOtherByteCount = AOtherCount // 8 if AOtherCount % 8 == 0 else AOtherCount // 8 + 1

    for i in range(AFristCount):
        NowValue = (data[AByteIdx] >> (8 - i)) & 1
        ARawValue |= (NowValue << AMove)
        AMove += 1
        if AMove == signal.FLength:
            if signal.FCANSgnType == 1 and NowValue == 1:
                ARawValue = ARawValue - ((1 << signal.FLength) - 1) - 1
            return float(ARawValue) * signal.FFactor + signal.FOffset

    for i in range(AOtherByteCount):
        for bitidx in range(8):
            if not signal.FIsIntel:
                NowValue = (data[AByteIdx - i - 1] >> bitidx) & 1
            else:
                NowValue = (data[AByteIdx + i + 1] >> bitidx) & 1
            ARawValue |= (NowValue << AMove)
            AMove += 1
            AOtherCount -= 1
            if AOtherCount == 0:
                if signal.FCANSgnType == 1 and NowValue == 1:
                    ARawValue = ARawValue - ((1 << signal.FLength) - 1) - 1
                return float(ARawValue) * signal.FFactor + signal.FOffset

def set_signal_value(data, signal, value):
    ARealValue = (value - signal.FOffset) / signal.FFactor
    RealValue = int(ARealValue)
    realStartbit = signal.FStartBit
    AByteIdx = realStartbit // 8
    AFristCount = (AByteIdx + 1) * 8 - realStartbit
    AOtherCount = signal.FLength - AFristCount
    AOtherByteCount = AOtherCount // 8 if AOtherCount % 8 == 0 else AOtherCount // 8 + 1
    AMove = 0
    NowValue = 0

    if not signal.FIsIntel:
        realStartbit = calc_real_startbit(signal.FStartBit, signal.FLength)
        AByteIdx = realStartbit // 8
        AFristCount = (AByteIdx + 1) * 8 - realStartbit
        AOtherCount = signal.FLength - AFristCount
        AOtherByteCount = AOtherCount // 8 if AOtherCount % 8 == 0 else AOtherCount // 8 + 1

    for i in range(AFristCount):
        NowValue = (RealValue >> AMove) & 1
        data[AByteIdx] &= (0xFF - (1 << (8 - i)))
        data[AByteIdx] |= (NowValue << (8 - i))
        AMove += 1
        if AMove == signal.FLength:
            return

    for i in range(AOtherByteCount):
        for bitidx in range(8):
            NowValue = (RealValue >> AMove) & 1
            valueMask = 0xFF - (1 << bitidx)
            if not signal.FIsIntel:
                data[AByteIdx - i - 1] &= valueMask
                data[AByteIdx - i - 1] |= (NowValue << bitidx)
            else:
                data[AByteIdx + i + 1] &= valueMask
                data[AByteIdx + i + 1] |= (NowValue << bitidx)
            AMove += 1
            AOtherCount -= 1
            if AOtherCount == 0:
                return

# 主程序
canData = [0, 64, 31, 0, 0, 0, 0, 0]
signal = TCANSignal(0, False, 12, 16, 0.1, 50)
value = get_signal_value(canData, signal)
print(canData)