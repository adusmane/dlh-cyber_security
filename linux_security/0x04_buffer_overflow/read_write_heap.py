
#!/usr/bin/python3
"""Search and replace an ASCII string in a process heap."""

import sys


def read_write_heap(pid, search_string, replace_string):
    """Replace a string in the heap of a running process."""
    search_bytes = search_string.encode('ascii')
    replace_bytes = replace_string.encode('ascii')

    try:
        heap_start = None
        heap_end = None

        with open('/proc/{}/maps'.format(pid), 'r') as maps:
            for line in maps:
                if '[heap]' in line:
                    address_range = line.split()[0]
                    addresses = address_range.split('-')
                    heap_start = int(addresses[0], 16)
                    heap_end = int(addresses[1], 16)
                    break

        if heap_start is None:
            print("Heap not found")
            return 1

        with open('/proc/{}/mem'.format(pid), 'rb+') as mem:
            mem.seek(heap_start)
            heap_data = mem.read(heap_end - heap_start)

            offset = heap_data.find(search_bytes)

            if offset == -1:
                print("String not found")
                return 0

            address = heap_start + offset

            if len(replace_bytes) <= len(search_bytes):
                mem.seek(address)
                mem.write(replace_bytes)
                mem.write(b'\x00' * (
                    len(search_bytes) - len(replace_bytes)))
            else:
                print("Replacement string is too long")
                return 1

            print("String replaced at {}".format(hex(address)))

    except (IOError, OSError, ValueError) as error:
        print("Error: {}".format(error))
        return 1

    return 0


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("Error: PID must be an integer")
        sys.exit(1)

    sys.exit(read_write_heap(pid, sys.argv[2], sys.argv[3]))

