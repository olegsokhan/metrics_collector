import psutil
import sys

if(sys.argv[1] == 'cpu') :
    try:cpuTimes = psutil.cpu_times()
    except AttributeError:{}
    try:print('system.cpu.idle '+str(cpuTimes.idle))
    except AttributeError:{}
    try:print('system.cpu.user '+str(cpuTimes.user))
    except AttributeError:{}
    try:print('system.cpu.guest '+str(cpuTimes.guest))
    except AttributeError:{}
    try:print('system.cpu.iowait '+str(cpuTimes.iowait))
    except AttributeError:{}
    try:print('system.cpu.stolen '+str(cpuTimes.steal))
    except AttributeError:{}
    try:print('system.cpu.system '+str(cpuTimes.system))
    except AttributeError:{}
elif (sys.argv[1] == 'mem') :
    virtualMemory = psutil.virtual_memory()
    swapMemory = psutil.swap_memory()
    try:print('virtual total '+str(virtualMemory.total))
    except AttributeError:{}
    try:print('virtual used '+str(virtualMemory.used))
    except AttributeError:{}
    try:print('virtual free '+str(virtualMemory.free))
    except AttributeError:{}
    try:print('virtual shared '+str(virtualMemory.shared))
    except AttributeError:{}
    try:print('swap total '+str(swapMemory.total))
    except AttributeError:{}
    try:print('swap used '+str(swapMemory.used))
    except AttributeError:{}
    try:print('swap free '+str(swapMemory.free))
    except AttributeError:{}