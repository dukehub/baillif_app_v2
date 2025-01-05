from PySide6.QtCore import QAbstractItemModel, Qt, QModelIndex
from PySide6.QtGui import QIcon
from core import state_manager, data_manager


class TreeNode:
    def __init__(self, data, parent=None, is_dossier=False, is_box=False):
        self.data = data
        self.parent = parent
        self.children = []
        self.is_dossier = is_dossier
        self.is_box = is_box
        self.hidden_data = {}

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def child(self, row):
        return self.children[row]

    def child_count(self):
        return len(self.children)

    def column_count(self):
        return len(self.data)

    def data_at(self, column):
        if 0 <= column < len(self.data):
            return self.data[column]
        return None

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        return 0
    def set_hidden_data(self, key, value):
        self.hidden_data[key] = value

    def get_hidden_data(self, key):
        return self.hidden_data.get(key)

class ArchiveTreeModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.root_node = TreeNode(["علبة الارشيف","رقم المحضر", "الطالب","المطلوب"])
        
        self._archive_boxes = data_manager._update_archive_boxes_state()
        self.box_icon = QIcon(":/icons/icons/binder.png")
        self.document_icon = QIcon(":/icons/icons/folder.png")
        state_manager.subscribe("archive_boxes", self.on_archive_boxes_updated)
        self.load_data(self._archive_boxes)

    def on_archive_boxes_updated(self, archive_boxes):
        """Appelé quand l'état des boîtes d'archives change"""
        self.root_node = TreeNode(["علبة الارشيف","رقم المحضر", "الطالب","المطلوب"])
        self.load_data(archive_boxes)

    def load_data(self, archive_boxes):
        self.layoutAboutToBeChanged.emit()

        if archive_boxes:
            for box in archive_boxes:
                box_node = TreeNode([box.name], is_box=True)
                for dossier in box.dossiers:
                    dossier_node = TreeNode(["",dossier.code, dossier.demandeur.nom, dossier.defendeur.nom], is_dossier=True)
                    dossier_node.set_hidden_data('full_data', dossier)
                    box_node.add_child(dossier_node)
                self.root_node.add_child(box_node)
        self.layoutChanged.emit()

    def rowCount(self, parent=QModelIndex()):
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            return self.root_node.child_count()
        return parent.internalPointer().child_count()

    def columnCount(self, parent=QModelIndex()):
        return self.root_node.column_count()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        
        node = index.internalPointer()
        
        if role == Qt.DisplayRole:
            if node.is_dossier:
                return node.data_at(index.column())
            elif node.is_box:
                return node.data_at(index.column()) if index.column() < 2 else None
            return None
        elif role == Qt.DecorationRole and index.column() == 0:
            if not node.is_dossier and node.parent == self.root_node:
                return self.box_icon
            else:
                return self.document_icon
        
        
        return None

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        if not parent.isValid():
            parent_node = self.root_node
        else:
            parent_node = parent.internalPointer()
        child_node = parent_node.child(row)
        if child_node:
            return self.createIndex(row, column, child_node)
        return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        node = index.internalPointer()
        parent_node = node.parent
        if parent_node == self.root_node:
            return QModelIndex()
        return self.createIndex(parent_node.row(), 0, parent_node)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            headers = ["علبة الارشيف","رقم المحضر", "الطالب","المطلوب"]
            return headers[section]
        return None
    def get_hidden_data(self, index, key):
        if not index.isValid():
            return None
        node = index.internalPointer()
        return node.get_hidden_data(key)
  