from PySide6.QtWidgets import QDialog

from app.database.db_manager import DatabaseManager
from app.views.dialogs import FinanceDialog, TodoDialog
from app.views.main_window import MainWindow


class MainController:
    def __init__(self) -> None:
        self.database = DatabaseManager()
        self.window = MainWindow()
        self._connect_signals()
        self.refresh_all_data()

    def _connect_signals(self) -> None:
        self.window.about_action.triggered.connect(self.window.show_about_dialog)

        self.window.add_todo_button.clicked.connect(self.add_todo)
        self.window.edit_todo_button.clicked.connect(self.edit_todo)
        self.window.delete_todo_button.clicked.connect(self.delete_todo)

        self.window.add_finance_button.clicked.connect(self.add_finance)
        self.window.edit_finance_button.clicked.connect(self.edit_finance)
        self.window.delete_finance_button.clicked.connect(self.delete_finance)

    def show(self) -> None:
        self.window.show()

    def refresh_all_data(self) -> None:
        self.refresh_todos()
        self.refresh_finances()

    def refresh_todos(self) -> None:
        rows = self.database.fetch_todos()
        self.window.populate_todos(rows)

    def refresh_finances(self) -> None:
        rows = self.database.fetch_finances()
        self.window.populate_finances(rows)

    def add_todo(self) -> None:
        dialog = TodoDialog(self.window)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        data = dialog.get_data()
        if not data["title"]:
            self.window.show_warning("Input Tidak Valid", "Judul to-do wajib diisi.")
            return

        self.database.add_todo(data)
        self.refresh_todos()

    def edit_todo(self) -> None:
        item_id = self.window.selected_todo_id()
        if item_id is None:
            self.window.show_warning(
                "Data Belum Dipilih", "Pilih satu data to-do yang ingin diedit."
            )
            return

        selected_row = self.database.get_todo_by_id(item_id)
        if not selected_row:
            return

        dialog = TodoDialog(self.window, selected_row)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        data = dialog.get_data()
        if not data["title"]:
            self.window.show_warning("Input Tidak Valid", "Judul to-do wajib diisi.")
            return

        self.database.update_todo(item_id, data)
        self.refresh_todos()

    def delete_todo(self) -> None:
        item_id = self.window.selected_todo_id()
        if item_id is None:
            self.window.show_warning(
                "Data Belum Dipilih", "Pilih satu data to-do yang ingin dihapus."
            )
            return

        if not self.window.confirm_delete("data to-do ini"):
            return

        self.database.delete_todo(item_id)
        self.refresh_todos()

    def add_finance(self) -> None:
        dialog = FinanceDialog(self.window)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        data = dialog.get_data()
        if data["amount"] <= 0:
            self.window.show_warning(
                "Input Tidak Valid", "Nominal transaksi harus lebih dari 0."
            )
            return

        self.database.add_finance(data)
        self.refresh_finances()

    def edit_finance(self) -> None:
        item_id = self.window.selected_finance_id()
        if item_id is None:
            self.window.show_warning(
                "Data Belum Dipilih", "Pilih satu catatan keuangan yang ingin diedit."
            )
            return

        selected_row = self.database.get_finance_by_id(item_id)
        if not selected_row:
            return

        dialog = FinanceDialog(self.window, selected_row)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        data = dialog.get_data()
        if data["amount"] <= 0:
            self.window.show_warning(
                "Input Tidak Valid", "Nominal transaksi harus lebih dari 0."
            )
            return

        self.database.update_finance(item_id, data)
        self.refresh_finances()

    def delete_finance(self) -> None:
        item_id = self.window.selected_finance_id()
        if item_id is None:
            self.window.show_warning(
                "Data Belum Dipilih",
                "Pilih satu catatan keuangan yang ingin dihapus.",
            )
            return

        if not self.window.confirm_delete("catatan keuangan ini"):
            return

        self.database.delete_finance(item_id)
        self.refresh_finances()
