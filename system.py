class OPERATING:
    operatings = (
            __import__("wmi").WMI().Win32_OperatingSystem(),
            __import__("psutil").virtual_memory(),
            __import__("wmi").WMI().Win32_ComputerSystem(),
            __import__("wmi").WMI().Win32_Processor(),
            __import__("wmi").WMI().Win32_VideoController(),
        )

class Infos(OPERATING):
    def __init__(self, operating):
        self.operating = operating

    def __ret__(self, key: str = "infos") -> __import__("typing").Dict:
        return __import__("os").linesep.join([f"[{__import__('datetime').datetime.strftime(__import__('datetime').datetime.now(), '%X')}] {k}: {v}" for k, v in globals()[key].items()])

    @property
    def __system__(self) -> __import__("typing").List:
        return self.operating[0][0].Name.split("|")[0]

    @property
    def __ram__(self, memory: str = "", result: int = 1024.0 ** 3) -> str:
        return str(round(self.operating[1].total / (result))) + 'GB'

    @property
    def __pversion__(self, os: list = []) -> __import__("typing").List:
        return " ".join([self.operating[0][0].Version, self.operating[0][0].BuildNumber])


    @property
    def __cpu__(self, key: str = "brand_raw") -> __import__("typing").Dict:
        return __import__("cpuinfo").get_cpu_info()[key][:22]

    @property
    def __ghz__(self, key: str = "hz_advertised_friendly") -> __import__("typing").List:
        return __import__("cpuinfo").get_cpu_info()[key][:4] + " " + __import__("cpuinfo").get_cpu_info()[key][7:]

    @property
    def __bit__(self, key: str = "bits") -> __import__("typing").List:
        return str(__import__("cpuinfo").get_cpu_info()[key]) + " Bit"

    @property
    def __gcard__(self) -> __import__("typing").List:
        return self.operating[4][0].Name

def __alls__(inf: classmethod = Infos(OPERATING().operatings)) -> __import__("typing").Callable:
    globals()["infos"] = {
                        "Platform":(inf.__system__),
                        "Bit":(inf.__bit__),
                        "RAM":(inf.__ram__),
                        "GHZ":(inf.__ghz__),
                        "OS Version":(inf.__pversion__),
                        "Graphic Card":(inf.__gcard__),
                        "CPU":(inf.__cpu__),
                        }

    return inf.__ret__()

print(__alls__())