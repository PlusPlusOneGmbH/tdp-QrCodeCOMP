'''Info Header Start
Name : __init__
Author : wieland@plusplus.one
Saveorigin : Project.toe
Saveversion : 2025.32460
Info Header End'''

from pathlib import Path
ToxFile = Path( Path(  __file__ ).parent, "TdQrcode.tox" )

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .extTdQrCode import extTdQrCode
    class Typing( baseCOMP, extTdQrCode):
        class par( extTdQrCode.par, baseCOMP._BaseCOMPPars): # pyright: ignore[reportIncompatibleVariableOverride]
            pass
    
else:
    class Typing:
        pass


DefaultGlobalOpShortcut = "QRCODECOMP"

__minimum_td_version__ = "2025.32460"

# Futureprrofing for automated search of toxfiles and imports.
_ToxFiles = {
    "QrCodeCOMP" : ToxFile
}


__all__ = ["ToxFile", "Typing"]

