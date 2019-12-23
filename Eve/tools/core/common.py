from PySide2 import QtCore

# PySide Eve Data Model
class Model(QtCore.QAbstractListModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent):
        ''' How many items the model contains '''

        return len(self._data)

    def data(self, index, role):
        ''' Handling each row data '''

        if not index.isValid():
            return

        # Get selected row
        row_index = index.row()
        data = self._data[row_index]

        if role == QtCore.Qt.DisplayRole:  # Display name in UI
            return data.name
        if role == QtCore.Qt.UserRole + 1:  # Return ID
            return data.id
        if role == QtCore.Qt.UserRole + 2:  # Return NAME
            return data.name
