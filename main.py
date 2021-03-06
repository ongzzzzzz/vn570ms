from pefile import PE

pe = PE('Vn-570MS.exe')

rich_header = pe.RICH_HEADER

print(rich_header is not None)


# hunch: a C or C# or C++ file made in MSVC 

print('HI')