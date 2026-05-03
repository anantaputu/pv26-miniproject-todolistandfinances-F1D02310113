from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from app.config import APP_NAME, STUDENT_ID, STUDENT_NAME


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.resize(1180, 720)
        self._build_ui()

    def _build_ui(self) -> None:
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)

        header_layout = QHBoxLayout()
        title_label = QLabel("TaskCash Manager")
        title_label.setObjectName("pageTitle")
        info_layout = QFormLayout()
        info_layout.setContentsMargins(0, 0, 0, 0)
        self.name_input = QLineEdit(STUDENT_NAME)
        self.name_input.setReadOnly(True)
        self.nim_input = QLineEdit(STUDENT_ID)
        self.nim_input.setReadOnly(True)
        info_layout.addRow("Nama", self.name_input)
        info_layout.addRow("NIM", self.nim_input)

        info_widget = QWidget()
        info_widget.setLayout(info_layout)

        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(info_widget)
        main_layout.addLayout(header_layout)

        self.tabs = QTabWidget()
        self.tabs.addTab(self._build_todo_tab(), "To-Do List")
        self.tabs.addTab(self._build_finance_tab(), "Pencatatan Keuangan")
        main_layout.addWidget(self.tabs)

        self.setCentralWidget(central_widget)
        self._build_menu_bar()

    def _build_menu_bar(self) -> None:
        menu_bar = self.menuBar()
        about_menu = QMenu("Tentang", self)
        self.about_action = about_menu.addAction("Tentang Aplikasi")
        menu_bar.addMenu(about_menu)

    def _build_todo_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(10)

        button_layout = QHBoxLayout()
        self.add_todo_button = QPushButton("Tambah To-Do")
        self.edit_todo_button = QPushButton("Edit To-Do")
        self.delete_todo_button = QPushButton("Hapus To-Do")
        button_layout.addWidget(self.add_todo_button)
        button_layout.addWidget(self.edit_todo_button)
        button_layout.addWidget(self.delete_todo_button)
        button_layout.addStretch()

        self.todo_table = QTableWidget(0, 7)
        self.todo_table.setHorizontalHeaderLabels(
            ["ID", "Judul", "Kategori", "Prioritas", "Deadline", "Status", "Catatan"]
        )
        self.todo_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.todo_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.todo_table.verticalHeader().setVisible(False)
        self.todo_table.horizontalHeader().setStretchLastSection(True)
        self.todo_table.setAlternatingRowColors(True)

        layout.addLayout(button_layout)
        layout.addWidget(self.todo_table)
        return tab

    def _build_finance_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(10)

        summary_layout = QHBoxLayout()
        self.income_label = QLabel("Total Pemasukan: Rp 0")
        self.income_label.setObjectName("summaryLabel")
        self.expense_label = QLabel("Total Pengeluaran: Rp 0")
        self.expense_label.setObjectName("summaryLabel")
        self.balance_label = QLabel("Saldo: Rp 0")
        self.balance_label.setObjectName("summaryLabel")
        summary_layout.addWidget(self.income_label)
        summary_layout.addWidget(self.expense_label)
        summary_layout.addWidget(self.balance_label)
        summary_layout.addStretch()

        button_layout = QHBoxLayout()
        self.add_finance_button = QPushButton("Tambah Catatan")
        self.edit_finance_button = QPushButton("Edit Catatan")
        self.delete_finance_button = QPushButton("Hapus Catatan")
        button_layout.addWidget(self.add_finance_button)
        button_layout.addWidget(self.edit_finance_button)
        button_layout.addWidget(self.delete_finance_button)
        button_layout.addStretch()

        self.finance_table = QTableWidget(0, 7)
        self.finance_table.setHorizontalHeaderLabels(
            ["ID", "Tanggal", "Jenis", "Kategori", "Nominal", "Metode", "Catatan"]
        )
        self.finance_table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.finance_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.finance_table.verticalHeader().setVisible(False)
        self.finance_table.horizontalHeader().setStretchLastSection(True)
        self.finance_table.setAlternatingRowColors(True)

        layout.addLayout(summary_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.finance_table)
        return tab

    def show_about_dialog(self) -> None:
        QMessageBox.information(
            self,
            "Tentang Aplikasi",
            (
                "Nama Aplikasi: TaskCash Manager\n"
                "Deskripsi: Aplikasi gabungan to-do list dan pencatatan keuangan.\n"
                f"Nama Mahasiswa: {STUDENT_NAME}\n"
                f"NIM: {STUDENT_ID}"
            ),
        )

    def show_warning(self, title: str, message: str) -> None:
        QMessageBox.warning(self, title, message)

    def confirm_delete(self, item_name: str) -> bool:
        answer = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Apakah Anda yakin ingin menghapus {item_name}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        return answer == QMessageBox.StandardButton.Yes

    def populate_todos(self, rows: list[dict]) -> None:
        self.todo_table.setRowCount(len(rows))
        for row_index, row in enumerate(rows):
            values = [
                row["id"],
                row["title"],
                row["category"],
                row["priority"],
                row["due_date"],
                row["status"],
                row["notes"],
            ]
            for column_index, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                if column_index in (1, 6):
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
                    )
                self.todo_table.setItem(row_index, column_index, item)
        self.todo_table.setColumnHidden(0, True)

    def populate_finances(self, rows: list[dict]) -> None:
        self.finance_table.setRowCount(len(rows))
        total_income = 0.0
        total_expense = 0.0

        for row_index, row in enumerate(rows):
            amount = float(row["amount"])
            if row["record_type"] == "Pemasukan":
                total_income += amount
            else:
                total_expense += amount

            values = [
                row["id"],
                row["record_date"],
                row["record_type"],
                row["category"],
                f"Rp {amount:,.2f}",
                row["payment_method"],
                row["notes"],
            ]
            for column_index, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                if column_index == 6:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
                    )
                self.finance_table.setItem(row_index, column_index, item)

        balance = total_income - total_expense
        self.income_label.setText(f"Total Pemasukan: Rp {total_income:,.2f}")
        self.expense_label.setText(f"Total Pengeluaran: Rp {total_expense:,.2f}")
        self.balance_label.setText(f"Saldo: Rp {balance:,.2f}")
        self.finance_table.setColumnHidden(0, True)

    def selected_todo_id(self) -> int | None:
        row = self.todo_table.currentRow()
        if row < 0:
            return None
        return int(self.todo_table.item(row, 0).text())

    def selected_finance_id(self) -> int | None:
        row = self.finance_table.currentRow()
        if row < 0:
            return None
        return int(self.finance_table.item(row, 0).text())
