from domain.qr.qr import QR

class QRController:
    def create_qr(self, req, res):
        data = req.get_param('data')
        qr = QR()
        res.add_header('Content-Disposition','attachment; filename='+ data +'.jpg')
        return qr.generate(data)
    

        