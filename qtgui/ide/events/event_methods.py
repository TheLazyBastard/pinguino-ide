#!/usr/bin/env python
#-*- coding: utf-8 -*-

from ..code_editor.pinguino_code_editor import PinguinoCodeEditor
from ..helpers.syntax import Snippet

from ..helpers.dialogs import Dialogs

import os
from PySide import QtCore, QtGui
from ..helpers.constants import TAB_NAME

from ..helpers.decorators import Decorator
from ..tools.code_navigator import CodeNavigator

from ..helpers import constants as Constants

from ..tools.files import Files
from ..tools.search_replace import SearchReplace

from ..child_windows.about import About
from ..child_windows.board_config import BoardConfig
from ..child_windows.stdout import Stdout

import codecs



########################################################################
class EventMethods(SearchReplace):
    """"""
    
    #----------------------------------------------------------------------
    @Decorator.connect_features()
    def new_file(self, *args, **kwargs):
        """"""
        path = kwargs.get("filename", self.__get_name__())
        filename = os.path.split(path)[1]         

        editor = PinguinoCodeEditor()
        self.main.tabWidget_files.addTab(editor, filename)
        editor.text_edit.insertPlainText(Snippet["file {snippet}"][1].replace("\t", ""))
        editor.text_edit.insertPlainText("\n")
        editor.text_edit.insertPlainText(Snippet["Bare minimum {snippet}"][1].replace("\t", ""))
        self.main.tabWidget_files.setCurrentWidget(editor)
        editor.text_edit.textChanged.connect(self.__text_changed__)
        editor.text_edit.undoAvailable.connect(self.__text_can_undo__)
        editor.text_edit.redoAvailable.connect(self.__text_can_redo__)
        editor.text_edit.copyAvailable.connect(self.__text_can_copy__)
        editor.text_edit.dropEvent = self.__drop__
        
        self.main.tabWidget_files.setTabToolTip(self.main.tabWidget_files.currentIndex(), path)
        
    #----------------------------------------------------------------------
    @Decorator.connect_features()
    def open_files(self):
        """"""
        filenames = Dialogs.set_open_file(self, ".pde")
        for filename in filenames:
            if self.__check_duplicate_file__(filename): continue
            self.new_file(os.path.split(filename)[1])
            editor = self.main.tabWidget_files.currentWidget()
            #pde_file = file(filename, mode="r")
            pde_file = codecs.open(filename, "r", "utf-8")
            content = "".join(pde_file.readlines())
            pde_file.close()
            editor.text_edit.setPlainText(content)
            setattr(editor, "path", filename)
        self.tab_changed()
        
    #----------------------------------------------------------------------
    @Decorator.connect_features()
    def open_file_from_path(self, *args, **kwargs):
        """"""
        filename = kwargs["filename"]
        if self.__check_duplicate_file__(filename): return
        self.new_file(filename=filename)
        editor = self.main.tabWidget_files.currentWidget()
        #pde_file = file(path, mode="r")
        pde_file = codecs.open(filename, "r", "utf-8")
        content = "".join(pde_file.readlines())
        pde_file.close()
        editor.text_edit.setPlainText(content)
        setattr(editor, "path", filename)
        self.tab_changed()
        
        
    #----------------------------------------------------------------------
    @Decorator.requiere_open_files()
    def comment_uncomment(self):
        """"""
        editor = self.main.tabWidget_files.currentWidget()
        cursor = editor.text_edit.textCursor()
        #prevCursor = editor.text_edit.textCursor()
        
        text = cursor.selectedText()
        lines = text.split(u'\u2029')
        firstLine = False
        for line in lines:
            if not str(line).isspace() and not str(line)=="":
                firstLine = line
                break

        if firstLine != False:
            if firstLine.startswith("//"): self.uncommentregion()
            else: self.commentregion()
            
            
    #----------------------------------------------------------------------
    @Decorator.requiere_open_files()
    def commentregion(self):
        """"""     

        editor = self.main.tabWidget_files.currentWidget()
        comment_wildcard = "// "
        
        #cursor is a COPY all changes do not affect the QPlainTextEdit's cursor!!!
        cursor = editor.text_edit.textCursor()
        
        start_ = cursor.selectionStart()
        end_ = cursor.selectionEnd()        
                
        selectionEnd = cursor.selectionEnd()
        start = editor.text_edit.document().findBlock(cursor.selectionStart()).firstLineNumber()
        end = editor.text_edit.document().findBlock(cursor.selectionEnd()).firstLineNumber()
        startPosition = editor.text_edit.document().findBlockByLineNumber(start).position()
        
        #init=(start, end)
        #Start a undo block
        cursor.beginEditBlock()
    
        #Move the COPY cursor
        cursor.setPosition(startPosition)
        #Move the QPlainTextEdit Cursor where the COPY cursor IS!
        editor.text_edit.setTextCursor(cursor)
        editor.text_edit.moveCursor(QtGui.QTextCursor.StartOfLine)
        #editor.tex
        
        for i in comment_wildcard:
            editor.text_edit.moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor)
            
        
        start = editor.text_edit.document().findBlock(cursor.selectionStart()).firstLineNumber()
        
        
        
        editor.text_edit.moveCursor(QtGui.QTextCursor.StartOfLine)
        s = editor.text_edit.cursor()
        s.pos()
        for i in xrange(start, end + 1):
            editor.text_edit.textCursor().insertText(comment_wildcard)
            #cursor.insertText(comment_wildcard)
            editor.text_edit.moveCursor(QtGui.QTextCursor.Down)
            editor.text_edit.moveCursor(QtGui.QTextCursor.StartOfLine)
            
        editor.text_edit.moveCursor(QtGui.QTextCursor.EndOfLine)
        
        
        end_ += (end + 1 - start) * 3
        cursor.setPosition(start_)
        cursor.setPosition(end_, QtGui.QTextCursor.KeepAnchor)
        editor.text_edit.setTextCursor(cursor)        
        
        
        
        #End a undo block
        cursor.endEditBlock()
        
    #----------------------------------------------------------------------
    @Decorator.requiere_open_files()
    def uncommentregion(self):
        """"""
        
        editor = self.main.tabWidget_files.currentWidget()
        comment_wildcard = "// "
    
        #cursor is a COPY all changes do not affect the QPlainTextEdit's cursor!!!
        cursor = editor.text_edit.textCursor()

        start_ = cursor.selectionStart()
        end_ = cursor.selectionEnd()         
        
        start = editor.text_edit.document().findBlock(cursor.selectionStart()).firstLineNumber()
        end = editor.text_edit.document().findBlock(cursor.selectionEnd()).firstLineNumber()
        startPosition = editor.text_edit.document().findBlockByLineNumber(start).position()

        #Start a undo block
        cursor.beginEditBlock()
    
        #Move the COPY cursor
        cursor.setPosition(startPosition)
        #Move the QPlainTextEdit Cursor where the COPY cursor IS!
        editor.text_edit.setTextCursor(cursor)
        editor.text_edit.moveCursor(QtGui.QTextCursor.StartOfLine)
        for i in xrange(start, end + 1):
            
            for i in comment_wildcard:
                editor.text_edit.moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor)
            
            text = editor.text_edit.textCursor().selectedText()
            if text == comment_wildcard:
                editor.text_edit.textCursor().removeSelectedText()
            elif u'\u2029' in text:
                #\u2029 is the unicode char for \n
                #if there is a newline, rollback the selection made above.
                editor.text_edit.moveCursor(QtGui.QTextCursor.Left, QtGui.QTextCursor.KeepAnchor)
    
            editor.text_edit.moveCursor(QtGui.QTextCursor.Down)
            editor.text_edit.moveCursor(QtGui.QTextCursor.StartOfLine)
            
        end_ -= (end + 1 - start) * 3
        cursor.setPosition(start_)
        cursor.setPosition(end_, QtGui.QTextCursor.KeepAnchor)
        editor.text_edit.setTextCursor(cursor)              
    
        #End a undo block
        cursor.endEditBlock()         
        

    #----------------------------------------------------------------------
    @Decorator.requiere_open_files()
    def close_file(self, *args, **kwargs):
        """"""
        editor = kwargs["editor"]
        if not editor: editor = self.get_tab().currentWidget()
        index = self.get_tab().currentIndex()
        filename = self.get_tab().tabText(index)
        save_path = getattr(editor, "path", None)
        
        if not save_path:
            reply = Dialogs.set_no_saved_file(self, filename)
            
            if reply == True:
                save_path, filename = Dialogs.set_save_file(self, filename)
                if not save_path: return
                setattr(editor, "path", save_path)
                self.__save_file__(editor)
                
            elif reply == None: return
            
            
        elif filename.endswith("*"):
            reply = Dialogs.set_no_saved_file(self, filename)
            #print reply
            if reply == True: self.__save_file__(editor)
            elif reply == None: return            
            
        
        self.get_tab().removeTab(index)
                
            
            
    #----------------------------------------------------------------------
    @Decorator.connect_features()
    def save_file(self, *args, **kwargs):
        """"""
        editor = self.main.tabWidget_files.currentWidget()
        index = self.main.tabWidget_files.currentIndex()
        filename = self.main.tabWidget_files.tabText(index)
        save_path = getattr(editor, "path", None)
        
        if not save_path:
            save_path, filename = Dialogs.set_save_file(self, filename)
            if not save_path: return False
            setattr(editor, "path", save_path)
            self.main.tabWidget_files.setTabText(index, filename)
        
        self.__save_file__(editor=editor)
        return True
        
        
    #----------------------------------------------------------------------
    def undo(self):
        """"""
        editor = self.main.tabWidget_files.currentWidget()
        index = self.main.tabWidget_files.currentIndex()
        editor.text_edit.undo()
        
    #----------------------------------------------------------------------
    def redo(self):
        """"""
        editor = self.main.tabWidget_files.currentWidget()
        index = self.main.tabWidget_files.currentIndex()
        editor.text_edit.redo()
        
    #----------------------------------------------------------------------
    def cut(self):
        """"""
        editor = self.main.tabWidget_files.currentWidget()
        index = self.main.tabWidget_files.currentIndex()
        editor.text_edit.cut()
        
    #----------------------------------------------------------------------
    def copy(self):
        """"""
        editor = self.main.tabWidget_files.currentWidget()
        index = self.main.tabWidget_files.currentIndex()
        editor.text_edit.copy()
        
    #----------------------------------------------------------------------
    def paste(self):
        """"""
        editor = self.main.tabWidget_files.currentWidget()
        index = self.main.tabWidget_files.currentIndex()
        editor.text_edit.paste()
        
        
    #----------------------------------------------------------------------
    @Decorator.update_toolbar()
    @Decorator.connect_features()
    def tab_changed(self, *args, **kwargs):
        """"""
        self.main.tabWidget_files.setVisible(self.main.tabWidget_files.count() > 0)
        self.main.frame_logo.setVisible(not self.main.tabWidget_files.count() > 0)
        self.main.actionClose_file.setEnabled(self.main.tabWidget_files.count() > 0)
            
        editor = self.main.tabWidget_files.currentWidget()
        if getattr(editor, "path", None): self.setWindowTitle(TAB_NAME+" - "+editor.path)
        else: self.setWindowTitle(TAB_NAME)
        
        index = self.main.tabWidget_files.currentIndex()
        filename = self.main.tabWidget_files.tabText(index)
        if filename.endswith("*"): self.main.actionSave_file.setEnabled(True)
        else: self.main.actionSave_file.setDisabled(True)
        
        #self.update_tool_bar(editor)
        self.__update_current_dir_on_files__()
        
        
    #----------------------------------------------------------------------
    def tab_close(self, index):
        """"""
        editor = self.get_tab().widget(index)
        self.close_file(editor=editor)
        
    #----------------------------------------------------------------------
    def jump_to_line(self, line):
        """"""
        self.highligh_line(line,  "#DBFFE3")
        
    #----------------------------------------------------------------------
    @Decorator.requiere_open_files()
    def highligh_line(self, line=None, color="#ff0000", text_cursor=None):
        """"""
        editor = self.main.tabWidget_files.currentWidget()
        
        if line:
            content = editor.text_edit.toPlainText()
            content = content.split("\n")[:line]
            position = len("\n".join(content))
            text_cur = editor.text_edit.textCursor()
            text_cur.setPosition(position)
            text_cur.clearSelection()
            editor.text_edit.setTextCursor(text_cur)
        else:
            text_cur = editor.text_edit.textCursor()
            text_doc = editor.text_edit.document()
            text_cur.clearSelection()
            editor.text_edit.setDocument(text_doc)
            editor.text_edit.setTextCursor(text_cur)            
            
        
        selection = QtGui.QTextEdit.ExtraSelection()
        selection.format.setBackground(QtGui.QColor(color))
        selection.format.setProperty(QtGui.QTextFormat.FullWidthSelection, True)
        selection.cursor = editor.text_edit.textCursor()
        editor.text_edit.setExtraSelections([selection])
        selection.cursor.clearSelection()
        
        if text_cursor: editor.text_edit.setTextCursor(text_cursor)
        
    #----------------------------------------------------------------------
    @Decorator.requiere_open_files()
    def clear_highlighs(self):
        """"""
        editor = self.main.tabWidget_files.currentWidget()
        editor.text_edit.setExtraSelections([])
        
    #----------------------------------------------------------------------
    @Decorator.requiere_open_files()
    def set_tab_search(self):
        """"""
        self.main.tabWidget_tools.setCurrentIndex(2)
        self.main.lineEdit_search.setFocus()
        
        
    #----------------------------------------------------------------------
    def jump_function(self, model_index):
        """"""
        column = model_index.column()
        item = self.main.tableWidget_functions.itemFromIndex(model_index).text()
        if column == 2:
            line = item[:item.find("-")]
            self.jump_to_line(int(line))

    #----------------------------------------------------------------------
    def jump_function_header(self, row):
        """"""
        item = self.main.tableWidget_functions.item(row, 2).text()
        line = item[:item.find("-")]
        self.jump_to_line(int(line))

    #----------------------------------------------------------------------
    def jump_variable(self, model_index):
        """"""
        column = model_index.column()
        item = self.main.tableWidget_variables.itemFromIndex(model_index).text()
        if column == 1:
            line = item
            self.jump_to_line(int(line))
            
    #----------------------------------------------------------------------
    def jump_variable_header(self, row):
        """"""
        item = self.main.tableWidget_variables.item(row, 1).text()
        line = item
        self.jump_to_line(int(line))

    #----------------------------------------------------------------------
    def jump_directive(self, model_index):
        """"""
        column = model_index.column()
        item = self.main.tableWidget_directives.itemFromIndex(model_index).text()
        if column == 2:
            line = item
            self.jump_to_line(int(line))

    #----------------------------------------------------------------------
    def jump_directive_header(self, row):
        """"""
        item = self.main.tableWidget_directives.item(row, 2).text()
        line = item
        self.jump_to_line(int(line))
                    
    #----------------------------------------------------------------------
    def change_dir_files(self, to_dir):
        """"""
        if to_dir == "Examples":
            self.__update_path_files__(Constants.PINGUINO_EXAMPLES_DIR)
            
        elif to_dir == "Home":
            self.__update_path_files__(Constants.HOME_DIR)
            
        elif to_dir == "Current file dir":
            editor = self.main.tabWidget_files.currentWidget()
            dir_ = getattr(editor, "path", None)
            if dir_: self.__update_path_files__(os.path.split(dir_)[0])
            
        elif to_dir == "Other...":
            open_dir = Dialogs.set_open_dir(self)
            if open_dir:
                self.__update_path_files__(open_dir)
                
                    
    #----------------------------------------------------------------------
    def change_dir_filesg(self, to_dir):
        """"""
        if to_dir == "Examples":
            self.__update_graphical_path_files__(Constants.PINGUINOG_EXAMPLES_DIR)
            
        elif to_dir == "Home":
            self.__update_graphical_path_files__(Constants.HOME_DIR)
            
        elif to_dir == "Current file dir":
            editor = self.main.tabWidget_files.currentWidget()
            dir_ = getattr(editor, "path", None)
            if dir_: self.__update_graphical_path_files__(os.path.split(dir_)[0])
            
        elif to_dir == "Other...":
            open_dir = Dialogs.set_open_dir(self)
            if open_dir:
                self.__update_graphical_path_files__(open_dir)                
                
        
    #----------------------------------------------------------------------
    def jump_dir_files(self, list_widget_item):
        """"""
        if getattr(list_widget_item, "type_file") == "dir":
            self.__update_path_files__(getattr(list_widget_item, "path_file"))
        if getattr(list_widget_item, "type_file") == "file":
            if getattr(list_widget_item, "path_file").endswith(".pde"):
                self.open_file_from_path(filename=getattr(list_widget_item, "path_file"))
        
    #----------------------------------------------------------------------
    def jump_dir_filesg(self, list_widget_item):
        """"""
        if getattr(list_widget_item, "type_file") == "dir":
            self.__update_graphical_path_files__(getattr(list_widget_item, "path_file"))
        if getattr(list_widget_item, "type_file") == "file":
            if getattr(list_widget_item, "path_file").endswith(".gpde"):
                self.open_file_from_path(filename=getattr(list_widget_item, "path_file"))
                
    #----------------------------------------------------------------------
    def get_tab(self):
        """"""
        if self.main.actionSwitch_ide.isChecked(): return self.main.tabWidget_graphical
        else: return self.main.tabWidget_files
            
    #----------------------------------------------------------------------
    def __update_path_files__(self, path):
        """"""
        Files.update_path_files(path, self.main.listWidget_files, self.main.label_path)
        
    #----------------------------------------------------------------------
    def __update_graphical_path_files__(self, path):
        """"""
        Files.update_path_files(path, self.main.listWidget_filesg, self.main.label_pathg)
        
        
    #----------------------------------------------------------------------
    def __update_current_dir_on_files__(self):
        tab = self.get_tab()
        if tab == self.main.tabWidget_files:
            if self.main.comboBox_files.currentText() == "Current file dir":
                editor = tab.currentWidget()
                dir_ = getattr(editor, "path", None)
                if dir_: self.__update_path_files__(os.path.split(dir_)[0])
                
        else:
            if self.main.comboBox_filesg.currentText() == "Current file dir":
                editor = tab.currentWidget()
                dir_ = getattr(editor, "path", None)
                if dir_: self.__update_graphical_path_files__(os.path.split(dir_)[0])
            
    #----------------------------------------------------------------------
    @Decorator.connect_features()
    def __save_file__(self, *args, **kwargs):
        """"""
        editor = kwargs.get("editor", self.get_tab())
        content = editor.text_edit.toPlainText()
        #pde_file = file(editor.path, mode="w")
        pde_file = codecs.open(editor.path, "w", "utf-8")
        pde_file.write(content)
        pde_file.close()
        self.__text_saved__()
        
    #----------------------------------------------------------------------
    def __get_name__(self, ext=".pde"):
        """"""
        index = 1
        name = "untitled-%d" % index + ext
        #filenames = [self.main.tabWidget_files.tabText(i) for i in range(self.main.tabWidget_files.count())]
        filenames = [self.get_tab().tabText(i) for i in range(self.get_tab().count())]
        while name in filenames or name + "*" in filenames:
            index += 1
            name = "untitled-%d" % index + ext
        return name + "*"
    
    #----------------------------------------------------------------------
    def __text_changed__(self, *args, **kwargs):
        """"""
        index = self.main.tabWidget_files.currentIndex()
        filename = self.main.tabWidget_files.tabText(index)
        if not filename.endswith("*"):
            self.main.tabWidget_files.setTabText(index, filename+"*")
            self.main.actionSave_file.setEnabled(True)
        self.clear_highlighs()
            
    
    #----------------------------------------------------------------------
    def __text_saved__(self, *args, **kwargs):
        """"""
        index = self.get_tab().currentIndex()
        filename = self.get_tab().tabText(index)
        if filename.endswith("*"):
            self.get_tab().setTabText(index, filename[:-1])
        self.main.actionSave_file.setEnabled(False)
        
    #----------------------------------------------------------------------
    def __text_can_undo__(self, *args, **kwargs):
        """"""
        state = not self.main.actionUndo.isEnabled()
        self.main.actionUndo.setEnabled(state)
        editor = self.main.tabWidget_files.currentWidget()
        editor.tool_bar_state["undo"] = state
        
    #----------------------------------------------------------------------
    def __text_can_redo__(self, *args, **kwargs):
        """"""
        state = not self.main.actionRedo.isEnabled()
        self.main.actionRedo.setEnabled(state)
        editor = self.main.tabWidget_files.currentWidget()
        editor.tool_bar_state["redo"] = state
        
    #----------------------------------------------------------------------
    def __text_can_copy__(self, *args, **kwargs):
        """"""
        state = not self.main.actionCopy.isEnabled()
        self.main.actionCopy.setEnabled(state)
        self.main.actionCut.setEnabled(state)
        editor = self.main.tabWidget_files.currentWidget()
        editor.tool_bar_state["copy"] = state
        
    #----------------------------------------------------------------------
    def __check_duplicate_file__(self, filename):
        """"""
        filenames = [getattr(self.main.tabWidget_files.widget(i), "path", None) for i in range(self.main.tabWidget_files.count())]
        if filename in filenames:
            Dialogs.file_duplicated(self, filename)
            self.main.tabWidget_files.setCurrentIndex(filenames.index(filename))
            return True
        return False
    
    
    #----------------------------------------------------------------------
    def __show_about__(self):
        """"""
        self.frame_about = About(self)
        self.frame_about.show()
        
    #----------------------------------------------------------------------
    def __show_board_config__(self):
        """"""
        self.frame_board = BoardConfig(self)
        self.frame_board.show()
        
    #----------------------------------------------------------------------
    def __show_stdout__(self):
        """"""
        self.frame_stdout = Stdout(self)
        self.frame_stdout.show()
        
    #----------------------------------------------------------------------
    def __show_pinguino_code__(self):
        """"""
        self.frame_pinguino_code = Stdout(self)
        self.frame_pinguino_code.show_text(self.PinguinoKIT.get_pinguino_source_code())
        self.frame_pinguino_code.show()
                
        
    #----------------------------------------------------------------------
    @Decorator.requiere_open_files()
    @Decorator.requiere_file_saved()
    def pinguino_compile(self):
        """"""
        if not self.is_graphical():
            filename = self.get_tab().currentWidget().path
        else:
            filename = self.PinguinoKIT.save_as_pde()
            filename = self.get_tab().currentWidget().path.replace(".gpde", ".pde")
            
            
        self.set_board()
        reply = Dialogs.confirm_board(self)
    
        if reply == False:
            self.__show_board_config__()
            return
        elif reply == None: return
            
        
        self.clear_output_ide()
        self.output_ide("compilling: %s"%filename)
        self.output_ide(self.get_description_board())
        
        self.pinguinoAPI.compile_file(filename)
        
        self.main.actionUpload.setEnabled(self.pinguinoAPI.compiled())
        if not self.pinguinoAPI.compiled():
            
            errors_preprocess = self.pinguinoAPI.get_errors_preprocess()
            if errors_preprocess:
                for error in errors_preprocess["preprocess"]:
                    self.output_ide(error)
            
            errors_c = self.pinguinoAPI.get_errors_compiling_c()
            if errors_c:
                self.output_ide(errors_c["complete_message"])
                line_errors = errors_c["line_numbers"]
                for line_error in line_errors:
                    self.highligh_line(line_error, "#ff7f7f")
            
            errors_asm = self.pinguinoAPI.get_errors_compiling_asm()
            if errors_asm:
                for error in errors_asm["error_symbols"]:
                    self.output_ide(error)
            
            errors_linking = self.pinguinoAPI.get_errors_linking()
            if errors_linking:
                for error in errors_linking["linking"]:
                    self.output_ide(error)
                    
            if errors_asm or errors_c:
                if Dialogs.error_while_compiling(self): self.__show_stdout__()
            elif errors_linking:
                if Dialogs.error_while_linking(self): self.__show_stdout__()
            elif errors_preprocess:
                if Dialogs.error_while_preprocess(self): self.__show_stdout__()                
                
                
        else:
            result = self.pinguinoAPI.get_result()
            self.output_ide("compilation done")
            self.output_ide(result["code_size"])
            self.output_ide("%s seconds process time"%result["time"])
            
            if Dialogs.compilation_done(self): self.pinguino_upload()
            
        if self.is_graphical(): os.remove(filename)
            
        
    #----------------------------------------------------------------------
    @Decorator.requiere_open_files()
    def pinguino_upload(self):
        """"""
        uploaded, result = self.pinguinoAPI.upload()
        self.output_ide(result)
        
        if uploaded: Dialogs.upload_done(self)
        else:
            if Dialogs.upload_fail(self, result): self.pinguino_upload()
        
                        
    #----------------------------------------------------------------------
    def __drop__(self, event):
        mine = event.mimeData()
        if mine.hasUrls():
            for path in mine.urls():
                self.open_file_from_path(path.path())
                
                #[self.chargepde(url.path()) for url in mine.urls()]
                
                
    #----------------------------------------------------------------------
    @Decorator.requiere_open_files()
    def save_screen_image(self):
        """"""
        editor = self.get_tab().currentWidget()
        scroll_area = editor.scroll_area
        image = QtGui.QPixmap.grabWidget(scroll_area,
                                         QtCore.QRect(0, 0,
                                                      scroll_area.width()-13,
                                                      scroll_area.height()-13))   
        
        filename = self.get_tab().tabText(self.get_tab().currentIndex())
        filename = os.path.splitext(filename)[0] + ".png"
        filename = Dialogs.set_save_image(self, filename)
        if filename: image.save(filename, "png")