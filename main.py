import flet as ft;


class NoteView():
    def __init__(self, page):
        self.page = page;
        self.textarea = ft.Ref[ft.TextField]();
        self.menubar = ft.Ref[ft.MenuBar]();
        self.filepicker = ft.FilePicker(on_result = pick_files_result);
        self.page.overlay.append(self.filepicker);
        self.create();

    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.path != None:
            print(e.path);

    def new_file(self, e):
        #self.filepicker.save_file();
        print("clicked");

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
                            content = ft.Text("New"),
                            on_click = self.new_file,
                        ),

                         ft.MenuItemButton(
                            content = ft.Text("Open")
                        ),

                         ft.MenuItemButton(
                            content = ft.Text("Save")
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

ft.app(target = main, port = 8502, view = ft.AppView.WEB_BROWSER);