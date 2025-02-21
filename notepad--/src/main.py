import flet as ft;
import os;


class NoteView():
    def __init__(self, page):
        self.page = page;
        self.textarea = ft.Ref[ft.TextField]();
        self.menubar = ft.Ref[ft.MenuBar]();

        self.filepicker = ft.FilePicker(on_result = self.pick_files_result);
        self.page.overlay.append(self.filepicker);
        self.current_action = None;

        self.current_file = None;
        self.file_name = "";
        self.create();

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        if self.current_action == "create_file":
            self.current_file = f"{e.path}/{self.file_name}";
            self.create_file(self.current_file, self.textarea.current.value);
            
    def create_file(self, file, content):
        open(file, "w").write(content);
        self.current_action = "none";

    def save_clicked(self, e):
        if self.current_file is None:
            self.current_action = "create_file";
            self.ask_file_name();
        else:
            self.create_file(self.current_file, self.textarea.current.value);
    
    def file_name_submitted(self, e):
        self.file_name = e.data;
        self.filepicker.get_directory_path();

    def ask_file_name(self):
        self.page.open(ft.BottomSheet(
            content = ft.TextField(hint_text = "file name", on_submit = self.file_name_submitted),
        ));

    def create_text_area(self):
        return ft.TextField(ref = self.textarea, border = ft.InputBorder.NONE, multiline = True, hint_text = "insert notes here");

    def create_menu_bar(self):
        return ft.Row([ft.MenuBar(
            ref = self.menubar,
            expand = True,
            controls = [
                ft.SubmenuButton(
                    content = ft.Text("File"),
                    controls = [      
                         ft.MenuItemButton(
                            content = ft.Text("Save"),
                            on_click = self.save_clicked,
                        ),

                         ft.MenuItemButton(
                            content = ft.Text("Open")
                        ),
                    ]
                ),
            ]
        )]);

    def create(self):
        self.page.add(ft.Column(controls = [
            self.create_menu_bar(),
            self.create_text_area(),
        ]));

    
def main(page):
    noteview = NoteView(page);

ft.app(main);