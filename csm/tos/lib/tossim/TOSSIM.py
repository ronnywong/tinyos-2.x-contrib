# This file was created automatically by SWIG 1.3.28.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _TOSSIM
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class MAC(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MAC, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MAC, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ MAC instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        this = _TOSSIM.new_MAC(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TOSSIM.delete_MAC
    __del__ = lambda self : None;
    def initHigh(*args): return _TOSSIM.MAC_initHigh(*args)
    def initLow(*args): return _TOSSIM.MAC_initLow(*args)
    def high(*args): return _TOSSIM.MAC_high(*args)
    def low(*args): return _TOSSIM.MAC_low(*args)
    def symbolsPerSec(*args): return _TOSSIM.MAC_symbolsPerSec(*args)
    def bitsPerSymbol(*args): return _TOSSIM.MAC_bitsPerSymbol(*args)
    def preambleLength(*args): return _TOSSIM.MAC_preambleLength(*args)
    def exponentBase(*args): return _TOSSIM.MAC_exponentBase(*args)
    def maxIterations(*args): return _TOSSIM.MAC_maxIterations(*args)
    def minFreeSamples(*args): return _TOSSIM.MAC_minFreeSamples(*args)
    def rxtxDelay(*args): return _TOSSIM.MAC_rxtxDelay(*args)
    def ackTime(*args): return _TOSSIM.MAC_ackTime(*args)
    def setInitHigh(*args): return _TOSSIM.MAC_setInitHigh(*args)
    def setInitLow(*args): return _TOSSIM.MAC_setInitLow(*args)
    def setHigh(*args): return _TOSSIM.MAC_setHigh(*args)
    def setLow(*args): return _TOSSIM.MAC_setLow(*args)
    def setSymbolsPerSec(*args): return _TOSSIM.MAC_setSymbolsPerSec(*args)
    def setBitsBerSymbol(*args): return _TOSSIM.MAC_setBitsBerSymbol(*args)
    def setPreambleLength(*args): return _TOSSIM.MAC_setPreambleLength(*args)
    def setExponentBase(*args): return _TOSSIM.MAC_setExponentBase(*args)
    def setMaxIterations(*args): return _TOSSIM.MAC_setMaxIterations(*args)
    def setMinFreeSamples(*args): return _TOSSIM.MAC_setMinFreeSamples(*args)
    def setRxtxDelay(*args): return _TOSSIM.MAC_setRxtxDelay(*args)
    def setAckTime(*args): return _TOSSIM.MAC_setAckTime(*args)
_TOSSIM.MAC_swigregister(MAC)

class Radio(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Radio, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Radio, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Radio instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        this = _TOSSIM.new_Radio(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TOSSIM.delete_Radio
    __del__ = lambda self : None;
    def add(*args): return _TOSSIM.Radio_add(*args)
    def gain(*args): return _TOSSIM.Radio_gain(*args)
    def connected(*args): return _TOSSIM.Radio_connected(*args)
    def remove(*args): return _TOSSIM.Radio_remove(*args)
    def setNoise(*args): return _TOSSIM.Radio_setNoise(*args)
    def setSensitivity(*args): return _TOSSIM.Radio_setSensitivity(*args)
_TOSSIM.Radio_swigregister(Radio)

class Packet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Packet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Packet, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Packet instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        this = _TOSSIM.new_Packet(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TOSSIM.delete_Packet
    __del__ = lambda self : None;
    def setSource(*args): return _TOSSIM.Packet_setSource(*args)
    def source(*args): return _TOSSIM.Packet_source(*args)
    def setDestination(*args): return _TOSSIM.Packet_setDestination(*args)
    def destination(*args): return _TOSSIM.Packet_destination(*args)
    def setLength(*args): return _TOSSIM.Packet_setLength(*args)
    def length(*args): return _TOSSIM.Packet_length(*args)
    def setType(*args): return _TOSSIM.Packet_setType(*args)
    def type(*args): return _TOSSIM.Packet_type(*args)
    def data(*args): return _TOSSIM.Packet_data(*args)
    def setData(*args): return _TOSSIM.Packet_setData(*args)
    def maxLength(*args): return _TOSSIM.Packet_maxLength(*args)
    def setStrength(*args): return _TOSSIM.Packet_setStrength(*args)
    def deliver(*args): return _TOSSIM.Packet_deliver(*args)
    def deliverNow(*args): return _TOSSIM.Packet_deliverNow(*args)
_TOSSIM.Packet_swigregister(Packet)

class SerialPacket(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SerialPacket, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SerialPacket, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ SerialPacket instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        this = _TOSSIM.new_SerialPacket(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TOSSIM.delete_SerialPacket
    __del__ = lambda self : None;
    def setDestination(*args): return _TOSSIM.SerialPacket_setDestination(*args)
    def destination(*args): return _TOSSIM.SerialPacket_destination(*args)
    def setLength(*args): return _TOSSIM.SerialPacket_setLength(*args)
    def length(*args): return _TOSSIM.SerialPacket_length(*args)
    def setType(*args): return _TOSSIM.SerialPacket_setType(*args)
    def type(*args): return _TOSSIM.SerialPacket_type(*args)
    def data(*args): return _TOSSIM.SerialPacket_data(*args)
    def setData(*args): return _TOSSIM.SerialPacket_setData(*args)
    def maxLength(*args): return _TOSSIM.SerialPacket_maxLength(*args)
    def deliver(*args): return _TOSSIM.SerialPacket_deliver(*args)
    def deliverNow(*args): return _TOSSIM.SerialPacket_deliverNow(*args)
_TOSSIM.SerialPacket_swigregister(SerialPacket)

class SerialForwarder(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SerialForwarder, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SerialForwarder, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ SerialForwarder instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        this = _TOSSIM.new_SerialForwarder(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TOSSIM.delete_SerialForwarder
    __del__ = lambda self : None;
    def process(*args): return _TOSSIM.SerialForwarder_process(*args)
    def dispatchPacket(*args): return _TOSSIM.SerialForwarder_dispatchPacket(*args)
    def forwardPacket(*args): return _TOSSIM.SerialForwarder_forwardPacket(*args)
_TOSSIM.SerialForwarder_swigregister(SerialForwarder)

class Throttle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Throttle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Throttle, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Throttle instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        this = _TOSSIM.new_Throttle(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TOSSIM.delete_Throttle
    __del__ = lambda self : None;
    def initialize(*args): return _TOSSIM.Throttle_initialize(*args)
    def finalize(*args): return _TOSSIM.Throttle_finalize(*args)
    def checkThrottle(*args): return _TOSSIM.Throttle_checkThrottle(*args)
    def printStatistics(*args): return _TOSSIM.Throttle_printStatistics(*args)
_TOSSIM.Throttle_swigregister(Throttle)

class variable_string_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, variable_string_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, variable_string_t, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ variable_string_t instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["type"] = _TOSSIM.variable_string_t_type_set
    __swig_getmethods__["type"] = _TOSSIM.variable_string_t_type_get
    if _newclass:type = property(_TOSSIM.variable_string_t_type_get, _TOSSIM.variable_string_t_type_set)
    __swig_setmethods__["ptr"] = _TOSSIM.variable_string_t_ptr_set
    __swig_getmethods__["ptr"] = _TOSSIM.variable_string_t_ptr_get
    if _newclass:ptr = property(_TOSSIM.variable_string_t_ptr_get, _TOSSIM.variable_string_t_ptr_set)
    __swig_setmethods__["len"] = _TOSSIM.variable_string_t_len_set
    __swig_getmethods__["len"] = _TOSSIM.variable_string_t_len_get
    if _newclass:len = property(_TOSSIM.variable_string_t_len_get, _TOSSIM.variable_string_t_len_set)
    __swig_setmethods__["isArray"] = _TOSSIM.variable_string_t_isArray_set
    __swig_getmethods__["isArray"] = _TOSSIM.variable_string_t_isArray_get
    if _newclass:isArray = property(_TOSSIM.variable_string_t_isArray_get, _TOSSIM.variable_string_t_isArray_set)
    def __init__(self, *args):
        this = _TOSSIM.new_variable_string_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TOSSIM.delete_variable_string_t
    __del__ = lambda self : None;
_TOSSIM.variable_string_t_swigregister(variable_string_t)

class nesc_app_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nesc_app_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nesc_app_t, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ nesc_app_t instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["numVariables"] = _TOSSIM.nesc_app_t_numVariables_set
    __swig_getmethods__["numVariables"] = _TOSSIM.nesc_app_t_numVariables_get
    if _newclass:numVariables = property(_TOSSIM.nesc_app_t_numVariables_get, _TOSSIM.nesc_app_t_numVariables_set)
    __swig_setmethods__["variableNames"] = _TOSSIM.nesc_app_t_variableNames_set
    __swig_getmethods__["variableNames"] = _TOSSIM.nesc_app_t_variableNames_get
    if _newclass:variableNames = property(_TOSSIM.nesc_app_t_variableNames_get, _TOSSIM.nesc_app_t_variableNames_set)
    __swig_setmethods__["variableTypes"] = _TOSSIM.nesc_app_t_variableTypes_set
    __swig_getmethods__["variableTypes"] = _TOSSIM.nesc_app_t_variableTypes_get
    if _newclass:variableTypes = property(_TOSSIM.nesc_app_t_variableTypes_get, _TOSSIM.nesc_app_t_variableTypes_set)
    __swig_setmethods__["variableArray"] = _TOSSIM.nesc_app_t_variableArray_set
    __swig_getmethods__["variableArray"] = _TOSSIM.nesc_app_t_variableArray_get
    if _newclass:variableArray = property(_TOSSIM.nesc_app_t_variableArray_get, _TOSSIM.nesc_app_t_variableArray_set)
    def __init__(self, *args):
        this = _TOSSIM.new_nesc_app_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TOSSIM.delete_nesc_app_t
    __del__ = lambda self : None;
_TOSSIM.nesc_app_t_swigregister(nesc_app_t)

class Variable(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Variable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Variable, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Variable instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        this = _TOSSIM.new_Variable(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TOSSIM.delete_Variable
    __del__ = lambda self : None;
    def getData(*args): return _TOSSIM.Variable_getData(*args)
_TOSSIM.Variable_swigregister(Variable)

class Mote(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Mote, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Mote, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Mote instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        this = _TOSSIM.new_Mote(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TOSSIM.delete_Mote
    __del__ = lambda self : None;
    def id(*args): return _TOSSIM.Mote_id(*args)
    def euid(*args): return _TOSSIM.Mote_euid(*args)
    def setEuid(*args): return _TOSSIM.Mote_setEuid(*args)
    def bootTime(*args): return _TOSSIM.Mote_bootTime(*args)
    def bootAtTime(*args): return _TOSSIM.Mote_bootAtTime(*args)
    def isOn(*args): return _TOSSIM.Mote_isOn(*args)
    def turnOff(*args): return _TOSSIM.Mote_turnOff(*args)
    def turnOn(*args): return _TOSSIM.Mote_turnOn(*args)
    def getVariable(*args): return _TOSSIM.Mote_getVariable(*args)
    def addNoiseTraceReading(*args): return _TOSSIM.Mote_addNoiseTraceReading(*args)
    def createNoiseModel(*args): return _TOSSIM.Mote_createNoiseModel(*args)
    def generateNoise(*args): return _TOSSIM.Mote_generateNoise(*args)
_TOSSIM.Mote_swigregister(Mote)

class Tossim(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tossim, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tossim, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Tossim instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        this = _TOSSIM.new_Tossim(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TOSSIM.delete_Tossim
    __del__ = lambda self : None;
    def init(*args): return _TOSSIM.Tossim_init(*args)
    def time(*args): return _TOSSIM.Tossim_time(*args)
    def ticksPerSecond(*args): return _TOSSIM.Tossim_ticksPerSecond(*args)
    def setTime(*args): return _TOSSIM.Tossim_setTime(*args)
    def timeStr(*args): return _TOSSIM.Tossim_timeStr(*args)
    def currentNode(*args): return _TOSSIM.Tossim_currentNode(*args)
    def getNode(*args): return _TOSSIM.Tossim_getNode(*args)
    def setCurrentNode(*args): return _TOSSIM.Tossim_setCurrentNode(*args)
    def addChannel(*args): return _TOSSIM.Tossim_addChannel(*args)
    def removeChannel(*args): return _TOSSIM.Tossim_removeChannel(*args)
    def randomSeed(*args): return _TOSSIM.Tossim_randomSeed(*args)
    def runNextEvent(*args): return _TOSSIM.Tossim_runNextEvent(*args)
    def mac(*args): return _TOSSIM.Tossim_mac(*args)
    def radio(*args): return _TOSSIM.Tossim_radio(*args)
    def newPacket(*args): return _TOSSIM.Tossim_newPacket(*args)
    def newSerialPacket(*args): return _TOSSIM.Tossim_newSerialPacket(*args)
_TOSSIM.Tossim_swigregister(Tossim)


