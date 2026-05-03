from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFormLayout,
    QLineEdit,
    QPlainTextEdit,
)


class TodoDialog(QDialog):
    def __init__(self, parent=None, data=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Form To-Do")
        self.setModal(True)
        self.resize(420, 320)

        self.title_input = QLineEdit()

        self.category_input = QComboBox()
        self.category_input.addItems(
            ["Kuliah", "Pribadi", "Organisasi", "Kerja", "Lainnya"]
        )

        self.priority_input = QComboBox()
        self.priority_input.addItems(["Rendah", "Sedang", "Tinggi"])

        self.due_date_input = QDateEdit()
        self.due_date_input.setCalendarPopup(True)
        self.due_date_input.setDate(QDate.currentDate())

        self.status_input = QComboBox()
        self.status_input.addItems(["Belum Mulai", "Proses", "Selesai"])

        self.notes_input = QPlainTextEdit()

        form_layout = QFormLayout(self)
        form_layout.addRow("Judul", self.title_input)
        form_layout.addRow("Kategori", self.category_input)
        form_layout.addRow("Prioritas", self.priority_input)
        form_layout.addRow("Deadline", self.due_date_input)
        form_layout.addRow("Status", self.status_input)
        form_layout.addRow("Catatan", self.notes_input)

        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        form_layout.addRow(self.button_box)

        if data:
            self.set_data(data)

    def set_data(self, data) -> None:
        self.title_input.setText(data["title"])
        self.category_input.setCurrentText(data["category"])
        self.priority_input.setCurrentText(data["priority"])
        self.due_date_input.setDate(QDate.fromString(data["due_date"], "yyyy-MM-dd"))
        self.status_input.setCurrentText(data["status"])
        self.notes_input.setPlainText(data["notes"])

    def get_data(self) -> dict:
        return {
            "title": self.title_input.text().strip(),
            "category": self.category_input.currentText(),
            "priority": self.priority_input.currentText(),
            "due_date": self.due_date_input.date().toString("yyyy-MM-dd"),
            "status": self.status_input.currentText(),
            "notes": self.notes_input.toPlainText().strip(),
        }


class FinanceDialog(QDialog):
    def __init__(self, parent=None, data=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Form Keuangan")
        self.setModal(True)
        self.resize(420, 320)

        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())

        self.type_input = QComboBox()
        self.type_input.addItems(["Pemasukan", "Pengeluaran"])

        self.category_input = QComboBox()
        self.category_input.addItems(
            ["Makan", "Transportasi", "Tagihan", "Belanja", "Gaji", "Lainnya"]
        )

        self.amount_input = QDoubleSpinBox()
        self.amount_input.setMaximum(999999999)
        self.amount_input.setDecimals(2)
        self.amount_input.setPrefix("Rp ")

        self.payment_method_input = QComboBox()
        self.payment_method_input.addItems(
            ["Tunai", "Transfer", "E-Wallet", "Kartu Debit"]
        )

        self.notes_input = QPlainTextEdit()

        form_layout = QFormLayout(self)
        form_layout.addRow("Tanggal", self.date_input)
        form_layout.addRow("Jenis", self.type_input)
        form_layout.addRow("Kategori", self.category_input)
        form_layout.addRow("Nominal", self.amount_input)
        form_layout.addRow("Metode", self.payment_method_input)
        form_layout.addRow("Catatan", self.notes_input)

        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        form_layout.addRow(self.button_box)

        if data:
            self.set_data(data)

    def set_data(self, data) -> None:
        self.date_input.setDate(QDate.fromString(data["record_date"], "yyyy-MM-dd"))
        self.type_input.setCurrentText(data["record_type"])
        self.category_input.setCurrentText(data["category"])
        self.amount_input.setValue(float(data["amount"]))
        self.payment_method_input.setCurrentText(data["payment_method"])
        self.notes_input.setPlainText(data["notes"])

    def get_data(self) -> dict:
        return {
            "record_date": self.date_input.date().toString("yyyy-MM-dd"),
            "record_type": self.type_input.currentText(),
            "category": self.category_input.currentText(),
            "amount": self.amount_input.value(),
            "payment_method": self.payment_method_input.currentText(),
            "notes": self.notes_input.toPlainText().strip(),
        }
