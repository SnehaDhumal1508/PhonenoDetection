from phoneno import *
import phonenumbers
from phonenumbers import geocoder, is_valid_number
from phonenumbers import carrier


class PhoneNo:
    def __init__(self):
        ui.clear.clicked.connect(self.clear)
        ui.search.clicked.connect(self.search)

    def clear(self):
        ui.phonenotext.setText("")
        ui.countrytext.setText("")
        ui.servicetext.setText("")

    def search(self):
        phno = str(ui.phonenotext.text())
        no = phonenumbers.parse(phno, "CH")
        country = geocoder.description_for_number(no, "en")
        ui.countrytext.setText(str(country))
        service = phonenumbers.parse(phno, "RO")
        serviceprovider = carrier.name_for_number(service, "en")
        ui.servicetext.setText(str(serviceprovider))
        if ui.servicetext.text() == "" and ui.countrytext.text() == "":
            ui.countrytext.setText("WRONG NUMBER")
            ui.servicetext.setText("WRONG NUMBER")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    File = open("Combinear.qss", 'r')
    with File:
        qss = File.read()
        app.setStyleSheet(qss)
    Dialog = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    PhoneNo = PhoneNo()
    sys.exit(app.exec_())