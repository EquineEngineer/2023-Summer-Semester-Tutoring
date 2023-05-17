from __future__ import annotations

import socket
from pprint import pprint


def main() -> int:
    print(f"All possible address families values:")
    pprint(list(socket.AddressFamily))

    print(f"All possible socket kinds values:")
    pprint(list(socket.SocketKind))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
