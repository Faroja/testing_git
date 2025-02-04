import subprocess
import sys

try:
    import tabulate
    print('Tabulate Sudah Terinstall')
except ImportError:
    print("tabulate belum terinstall. Menginstall sekarang...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
    import tabulate