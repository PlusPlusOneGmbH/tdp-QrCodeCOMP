'''Info Header Start
Name : extTdQrCode
Author : wieland@plusplus.one
Saveorigin : Project.toe
Saveversion : 2025.32460
Info Header End'''

from qrcode import QRCode, constants
import io
from touchutilcollection.extensions import EnsureExtension, parfield, partypes
from typing import Optional


class extTdQrCode(EnsureExtension):
	"""
	extTdQrCode description
	"""
	class par:
		Fieldsize = parfield( 
			partypes.ParInt, max = 10, min = 1, 
			default = 1, page = "Settings", order = 0
			)
		Bordersize = parfield(
			partypes.ParInt, min = 1, max = 10, 
			default = 1, page = "Settings", order = 1
		)
		Version = parfield(
			partypes.ParInt, min = 1, max = 40, page = "Settings", order = 1.5
		)
		Errorcorrection = parfield(
			partypes.ParMenu, menuNames=["H", "L", "M", "Q"], menuLabels=["H", "L", "M", "Q"],
			default= "H", page = "Settings", order = 3
		)
		Text = parfield(
			partypes.ParStr, default = "Sampletext", page = "Settings", order = 4, startSection = True,
			enableExpr = "not me.op('input_text').text"
		)

	def __init__(self, ownerComp:baseCOMP):
		# The component to which this extension is attached
		super().__init__( ownerComp )
		self.ownerComp = ownerComp
		

	def Generate_QrCodeBytes(self, target_text:Optional[str] = None):

		qr_maker = QRCode(
			border		= self.par.Bordersize.eval(),
			box_size	= self.par.Fieldsize.eval(),
			version		= self.par.Version.eval(),
			error_correction = getattr( constants, f"ERROR_CORRECT_{self.par.Errorcorrection.eval()}" ),
		)
		qr_maker.add_data( target_text or self.par.Text.eval() )
		qr_maker.make(fit=True)
		qr_image = qr_maker.make_image()

		byteIO = io.BytesIO()
		qr_image.save( byteIO, format = "PNG")
		
		return bytearray( byteIO.getvalue() )
