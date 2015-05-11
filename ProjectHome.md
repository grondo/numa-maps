The numa-maps program displays information about how memory for processes is laid out on a NUMA system.

numa-maps can display information about stack and heap, as well as shared library and other memory mappings. It requires the existence of the /proc/PID/numa\_maps file.

By default numa-maps displays information for the total mapped stack and heap memory only. Processes without a virtual memory map are silently ignored.