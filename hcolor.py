#!/usr/bin/env python
import sys

if __name__ == "__main__":
    print(sys.argv)
    hcolor = sys.argv[1]
    c = hcolor.replace("#", "")
    print(c)
    hrgb = (c[:2], c[2:4], c[4:6])
    print(hrgb)
    rgb = [int(f"0x{c}", 16) for c in hrgb]
    print(f"rgb({', '.join([str(c) for c in rgb])})")
