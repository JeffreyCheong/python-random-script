import psutil

available = ['ABOVE_NORMAL_PRIORITY_CLASS', 'AF_LINK', 'AIX', 'AccessDenied', 'BELOW_NORMAL_PRIORITY_CLASS', 'BSD', 'CONN_CLOSE', 'CONN_CLOSE_WAIT', 'CONN_CLOSING', 'CONN_DELETE_TCB', 'CONN_ESTABLISHED', 'CONN_FIN_WAIT1', 'CONN_FIN_WAIT2', 'CONN_LAST_ACK', 'CONN_LISTEN', 'CONN_NONE', 'CONN_SYN_RECV', 'CONN_SYN_SENT', 'CONN_TIME_WAIT', 'Error', 'FREEBSD', 'HIGH_PRIORITY_CLASS', 'IDLE_PRIORITY_CLASS', 'IOPRIO_HIGH', 'IOPRIO_LOW', 'IOPRIO_NORMAL', 'IOPRIO_VERYLOW', 'LINUX', 'MACOS', 'NETBSD', 'NIC_DUPLEX_FULL', 'NIC_DUPLEX_HALF', 'NIC_DUPLEX_UNKNOWN', 'NORMAL_PRIORITY_CLASS', 'NoSuchProcess', 'OPENBSD', 'OSX', 'POSIX', 'POWER_TIME_UNKNOWN', 'POWER_TIME_UNLIMITED', 'PermissionError', 'Popen', 'Process', 'ProcessLookupError', 'REALTIME_PRIORITY_CLASS', 'STATUS_DEAD', 'STATUS_DISK_SLEEP', 'STATUS_IDLE', 'STATUS_LOCKED', 'STATUS_PARKED', 'STATUS_RUNNING', 'STATUS_SLEEPING', 'STATUS_STOPPED', 'STATUS_TRACING_STOP', 'STATUS_WAITING', 'STATUS_WAKING', 'STATUS_ZOMBIE', 'SUNOS', 'TimeoutExpired', 'WINDOWS', 'ZombieProcess', '_LOWEST_PID', '_PY3', '_SENTINEL', '_TOTAL_PHYMEM', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_as_dict_attrnames', '_assert_pid_not_reused', '_common', '_compat', '_cpu_busy_time', '_cpu_times_deltas', '_cpu_tot_time', '_last_cpu_times', '_last_cpu_times_2', '_last_per_cpu_times', '_last_per_cpu_times_2', '_lock', '_pmap', '_ppid_map', '_pprint_secs', '_psplatform', '_psutil_windows', '_pswindows', '_timer', '_wrap_numbers', 'boot_time', 'collections', 'contextlib', 'cpu_count', 'cpu_freq', 'cpu_percent', 'cpu_stats', 'cpu_times', 'cpu_times_percent', 'datetime', 'disk_io_counters', 'disk_partitions', 'disk_usage', 'functools', 'getloadavg', 'long', 'net_connections', 'net_if_addrs', 'net_if_stats', 'net_io_counters', 
'os', 'pid_exists', 'pids', 'process_iter', 'pwd', 'sensors_battery', 'signal', 'subprocess', 'swap_memory', 'sys', 'test', 'threading', 'time', 'users', 'version_info', 'virtual_memory', 'wait_procs', 'win_service_get', 'win_service_iter']


if __name__ == '__main__':

    battery = psutil.sensors_battery()

    print(dir(battery.secsleft))
    print(battery.secsleft.as_integer_ratio)
    print(battery.secsleft.bit_length)
    print(battery.secsleft.conjugate)
    print(battery.secsleft.denominator)
    print(battery.secsleft.from_bytes)
    print(battery.secsleft.imag)
    print(battery.secsleft.name)
    print(battery.secsleft.numerator)
    
    print(battery.secsleft.real)
    print(battery.secsleft.to_bytes)
    print(battery.secsleft.value)
    battery_status = {
        'percent': battery.percent,
        'secsLeft': battery.secsleft,
        'powerPlugged': battery.power_plugged
    }

    print(battery_status)
    print(psutil.users())

    # print(psutil.pids())
    # processIds = psutil.pids()

    # for i in processIds:
    #     p = psutil.Process(i)
        
    #     try:

    #         print(f'{i}: {p.name()} | {p.cpu_times()} | {p.cpu_percent()} | {p.create_time()} | {p.ppid()} | {p.status()}')
    #     except psutil.NoSuchProcess as identifier:

    #         print(f'{i}: {identifier.args}')