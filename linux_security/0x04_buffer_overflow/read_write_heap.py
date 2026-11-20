
#!/usr/bin/python3
"""Search and replace an ASCII string in a process heap."""

import sys


def read_write_heap(pid, search_string, replace_string):
    """Search and replace a string in the heap of a process."""
    if not search_string:
        print("Error: search string cannot be empty")
        return 1

    if len(replace_string) > len(search_string):
        print("Error: replacement cannot be longer than search string")
        return 1

    try:
        search_bytes = search_string.encode('ascii')
        replace_bytes = replace_string.encode('ascii')

        heap_start = None
        heap_end = None

        with open('/proc/{}/maps'.format(pid), 'r') as maps:
            for line in maps:
                if '[heap]' in line:
                    addresses = line.split()[0].split('-')
                    heap_start = int(addresses[0], 16)
                    heap_end = int(addresses[1], 16)
                    break

        if heap_start is None:
            print("Error: heap not found")
            return 1

        with open('/proc/{}/mem'.format(pid), 'rb+') as mem:
            mem.seek(heap_start)
            heap_data = mem.read(heap_end - heap_start)

            offset = 0
            count = 0

            while True:
                offset = heap_data.find(search_bytes, offset)

                if offset == -1:
                    break

                address = heap_start + offset

                mem.seek(address)
                mem.write(replace_bytes)
                mem.write(b'\x00' * (
                    len(search_bytes) - len(replace_bytes)))

                print("Replaced at address: {}".format(hex(address)))

                count += 1
                offset += len(search_bytes)

            print("Total replacements: {}".format(count))

    except (IOError, OSError, ValueError, UnicodeError) as error:
        print("Error: {}".format(error))
        return 1

    return 0


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    try:
        pid = int(sys.argv[1])
        if pid <= 0:
            raise ValueError
    except ValueError:
        print("Error: invalid PID")
        sys.exit(1)

    sys.exit(read_write_heap(pid, sys.argv[2], sys.argv[3]))
