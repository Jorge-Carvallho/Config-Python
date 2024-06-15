class CalendarError(Exception): ...
class UnsupportedDateType(CalendarError): ...
class ISORegistryError(CalendarError): ...
class ICalExportError(CalendarError): ...
class ICalExportRangeError(ICalExportError): ...
class ICalExportTargetPathError(ICalExportError): ...
