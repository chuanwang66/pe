from pe import PE

# list export functions
pe = PE('res/obs-aipai.dll')
print("ImageBaseAddr: 0x{0:08x}".format(pe.imagebase))
for api, addr in pe.exports.items():
    print("{0} @ 0x{1:08x}".format(api, addr))

print('\n\n')

# list import functions
pe = PE('res/notepad.exe')
print("ImageBaseAddr: 0x{0:08x}".format(pe.imagebase))
for dllname in pe.imports:
    for api, addr in pe.imports[dllname].items():
        print("{0} ({1}) @ 0x{2:08x} (IAT)".format(api, dllname, addr))