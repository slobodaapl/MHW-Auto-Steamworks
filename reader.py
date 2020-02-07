from ctypes import *
from struct import *
from subprocess import check_output
import multiprocessing


class ProcReader:

    def __init__(self):
        self.addr_start = 0x70000000
        self.addr_end = 0xF0000000
        self.fuel_addr = None
        self.cpu_count = multiprocessing.cpu_count()
        self.nat_fuel = None
        self.stor_fuel = None
        self.use_nat = True
        self.addr_list = []
        self.i = i
        self.pid = self.get_pid()
        self.PROCESS_ALL_ACCESS = 0x1F0FFF
        self.PROCESS_VM_READ = 0x0010

        self.k32 = WinDLL('kernel32', use_last_error=True)

        self.OpenProcess = self.k32.OpenProcess

        self.ReadProcessMemory = self.k32.ReadProcessMemory

        self.CloseHandle = self.k32.CloseHandle
        self.buffer = c_char_p(b"........")
        self.val = c_int()
        self.bytesRead = c_ulonglong()
        self.processHandle = self.OpenProcess(self.PROCESS_VM_READ, False, self.pid)
        self.find_address()

    def get_pid(self):
        l = check_output('tasklist /fi "Imagename eq MonsterHunterWorld.exe"').split()
        return int(l[14])

    def get_fuel(self):
        if self.ReadProcessMemory(self.processHandle, self.fuel_addr, self.buffer, 8, byref(self.bytesRead)):
            addr = unpack('II', b'........')
            return (addr[0] + addr[1])//10
        else:
            return 0

    def find_address(self, nat_fuel=None, stor_fuel=None):  # 82FA305C
        self.nat_fuel = nat_fuel
        self.stor_fuel = stor_fuel
        if self.nat_fuel // 10 < 3:
            self.use_nat = False
        pool = multiprocessing.Pool()
        pool.map(self.find_address_hidden, range(0, self.cpu_count))
        pool.close()

    def find_address_hidden(self, i):
        offset = i*4
        temp_buffer = c_int()
        while self.addr_start + offset < self.addr_end:
            if self.ReadProcessMemory(self.processHandle, self.addr_start + offset, byref(temp_buffer), 4,
                                      byref(self.bytesRead)):
                addr = temp_buffer.value
                print(addr)
                if self.use_nat:
                    if addr == self.nat_fuel:
                        self.addr_list.append(self.addr_start + offset)
                else:
                    if addr == self.stor_fuel:
                        self.addr_list.append(self.addr_start + offset)
            offset += 4*self.cpu_count

    def quit(self):
        self.CloseHandle(self.processHandle)


proc = ProcReader()
proc.find_address(680, 7777)
print(proc.addr_list)

