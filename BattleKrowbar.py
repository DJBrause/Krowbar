from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton, MDFillRoundFlatIconButton
from kivymd.uix.textfield import MDTextFieldRect, MDTextField
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle, Color
from kivymd.toast import toast        # for android add .androidtoast.androidtoast
from kivy.graphics.instructions import Canvas

class KrowBarApp(MDApp):

    def build(self):
        screen_manager = ScreenManager()
        self.loaded_values = [1, 0, 0, 0, 0, 0] # round num, cp, primary obj, 1st secondary, 2nd secondary, 3rd secondary
        self.update_values()
        self.theme_cls.primary_palette = "Green"

        # Game counters screen and backgrgound color

        counters = Screen(name="Counters")
        with counters.canvas:
            c = Color(0, 25.1/100, 12.16/100, 1) # R, G, B, Transparency
            Rectangle(pos = (0,0), size = Window.size, color = c)

        screen_manager.add_widget(counters)

        # SCROLLVIEW

        scroll = ScrollView()
        counters.add_widget(scroll)

        # MAIN GRID
        app_grid = GridLayout(cols=1, spacing=100, size_hint_y=None)
        app_grid.padding = [Window.width/40,Window.height/20,Window.width/40,Window.height/4]  # [left,top,right,bottom]
        app_grid.bind(minimum_height=app_grid.setter('height'))
        scroll.add_widget(app_grid)

        # ROUND COUNTER

        round_parent_grid = MDGridLayout()
        round_parent_grid.cols = 1
        round_parent_grid.rows = 2
        round_parent_grid.adaptive_height = True

        round_label = MDLabel(text='Round number:')
        round_label.halign = 'center'
        round_parent_grid.add_widget(round_label)
        app_grid.add_widget(round_parent_grid)

        grid_round = GridLayout()
        grid_round.cols = 3

        increase_round = MDIconButton(icon="arrow-right-bold", on_press=self.increase_round)
        self.round_counter = MDLabel(text=str(self.loaded_values[0]))
        self.round_counter.halign = 'center'
        self.round_counter.valign = 'middle'
        decrease_round = MDIconButton(icon="arrow-left-bold", on_press=self.decrease_round)

        grid_round.add_widget(decrease_round)
        grid_round.add_widget(self.round_counter)
        grid_round.add_widget(increase_round)
        round_parent_grid.add_widget(grid_round)

        # COMMAND POINTS

        cp_parent_grid = MDGridLayout()
        cp_parent_grid.cols = 1
        cp_parent_grid.rows = 2
        cp_parent_grid.adaptive_height = True

        cp_label = MDLabel(text='Command Points Left:')
        cp_label.halign = 'center'
        cp_parent_grid.add_widget(cp_label)
        app_grid.add_widget(cp_parent_grid)

        grid_cp = MDGridLayout()
        grid_cp.cols = 3

        increase_cp = MDIconButton(icon="arrow-right-bold", on_press=self.increase_cp)
        self.cp_counter = MDLabel(text=str(self.loaded_values[1]))
        self.cp_counter.halign = 'center'
        self.cp_counter.valign = 'middle'
        decrease_cp = MDIconButton(icon="arrow-left-bold", on_press=self.decrease_cp)

        grid_cp.add_widget(decrease_cp)
        grid_cp.add_widget(self.cp_counter)
        grid_cp.add_widget(increase_cp)
        cp_parent_grid.add_widget(grid_cp)

        # VP PRIMARY

        prim_parent_grid = MDGridLayout()
        prim_parent_grid.cols = 1
        prim_parent_grid.rows = 2
        prim_parent_grid.adaptive_height = True

        prim_label = MDLabel(text='Primary Objective Points:')
        prim_label.halign = 'center'
        prim_parent_grid.add_widget(prim_label)
        app_grid.add_widget(prim_parent_grid)

        grid_prim = MDGridLayout()
        grid_prim.cols = 3

        increase_prim = MDIconButton(icon="arrow-right-bold", on_press=self.increase_prim)
        self.prim_counter = MDLabel(text=str(self.loaded_values[2]))
        self.prim_counter.halign = 'center'
        self.prim_counter.valign = 'middle'
        decrease_prim = MDIconButton(icon="arrow-left-bold", on_press=self.decrease_prim)

        grid_prim.add_widget(decrease_prim)
        grid_prim.add_widget(self.prim_counter)
        grid_prim.add_widget(increase_prim)
        prim_parent_grid.add_widget(grid_prim)

        # VP SECONDARY 1

        sec1_parent_grid = MDGridLayout()
        sec1_parent_grid.cols = 1
        sec1_parent_grid.rows = 2
        sec1_parent_grid.adaptive_height = True


        sec1_label = MDTextField()
        sec1_label.hint_text ='1st Secondary Objective Points:'
        sec1_label.multiline = False
        #sec1_label = MDLabel(text='1st Secondary Objective Points:')
        sec1_label.halign = 'center'
        sec1_parent_grid.add_widget(sec1_label)
        app_grid.add_widget(sec1_parent_grid)

        grid_sec1 = MDGridLayout()
        grid_sec1.cols = 3

        increase_sec1 = MDIconButton(icon="arrow-right-bold", on_press=self.increase_sec1)
        self.sec1_counter = MDLabel(text=str(self.loaded_values[3]))
        self.sec1_counter.halign = 'center'
        self.sec1_counter.valign = 'middle'
        decrease_sec1 = MDIconButton(icon="arrow-left-bold", on_press=self.decrease_sec1)

        grid_sec1.add_widget(decrease_sec1)
        grid_sec1.add_widget(self.sec1_counter)
        grid_sec1.add_widget(increase_sec1)
        sec1_parent_grid.add_widget(grid_sec1)

        # VP SECONDARY 2


        sec2_parent_grid = MDGridLayout()
        sec2_parent_grid.cols = 1
        sec2_parent_grid.rows = 2
        sec2_parent_grid.adaptive_height = True

        sec2_label = MDTextField()
        sec2_label.hint_text = '2nd Secondary Objective Points:'
        sec2_label.multiline = False
        #sec2_label = MDLabel(text='2nd Secondary Objective Points:')
        sec2_label.halign = 'center'
        sec2_parent_grid.add_widget(sec2_label)
        app_grid.add_widget(sec2_parent_grid)

        grid_sec2 = MDGridLayout()
        grid_sec2.cols = 3

        increase_sec2 = MDIconButton(icon="arrow-right-bold", on_press=self.increase_sec2)
        self.sec2_counter = MDLabel(text=str(self.loaded_values[4]))
        self.sec2_counter.halign = 'center'
        self.sec2_counter.valign = 'middle'
        decrease_sec2 = MDIconButton(icon="arrow-left-bold", on_press=self.decrease_sec2)

        grid_sec2.add_widget(decrease_sec2)
        grid_sec2.add_widget(self.sec2_counter)
        grid_sec2.add_widget(increase_sec2)
        sec2_parent_grid.add_widget(grid_sec2)

        # VP SECONDARY 3

        sec3_parent_grid = MDGridLayout()
        sec3_parent_grid.cols = 1
        sec3_parent_grid.rows = 2
        sec3_parent_grid.adaptive_height = True

        sec3_label = MDTextField()
        sec3_label.hint_text = '3rd Secondary Objective Points:'
        sec3_label.multiline = False
        #sec3_label = MDLabel(text='3rd Secondary Objective Points:')
        sec3_label.halign = 'center'
        sec3_parent_grid.add_widget(sec3_label)
        app_grid.add_widget(sec3_parent_grid)

        grid_sec3 = MDGridLayout()
        grid_sec3.cols = 3

        increase_sec3 = MDIconButton(icon="arrow-right-bold", on_press=self.increase_sec3)
        self.sec3_counter = MDLabel(text=str(self.loaded_values[5]))
        self.sec3_counter.halign = 'center'
        self.sec3_counter.valign = 'middle'
        decrease_sec3 = MDIconButton(icon="arrow-left-bold", on_press=self.decrease_sec3)

        grid_sec3.add_widget(decrease_sec3)
        grid_sec3.add_widget(self.sec3_counter)
        grid_sec3.add_widget(increase_sec3)
        sec3_parent_grid.add_widget(grid_sec3)

        # Empty grid to create space

        empty_grid = MDGridLayout()
        app_grid.add_widget(empty_grid)

        # Bottom grid for Score and Reset buttons

        bottom_grid = MDGridLayout()
        bottom_grid.cols = 2
        app_grid.add_widget(bottom_grid)

        # SCORE TOAST

        score_button = MDFillRoundFlatIconButton(icon='flag-plus-outline', text="Show score",on_press=self.sum_up)
        button_anchor = AnchorLayout()
        button_anchor.anchor_y = 'bottom'
        button_anchor.add_widget(score_button)
        bottom_grid.add_widget(button_anchor)

        # RESET

        reset_button = MDFillRoundFlatIconButton(icon='backup-restore', text="Reset", on_press=self.reset_values)
        reset_button_anchor = AnchorLayout()
        reset_button_anchor.anchor_y = 'bottom'
        reset_button_anchor.add_widget(reset_button)
        bottom_grid.add_widget(reset_button_anchor)

        return screen_manager

    def increase_round(self, obj):
        if self.loaded_values[0] <= 4:
            self.loaded_values[0] += 1
            self.loaded_values[1] += 1
            self.round_counter.text = str(self.loaded_values[0])
            self.cp_counter.text = str(self.loaded_values[1])
        else:
            pass

    def decrease_round(self, obj):
        if self.loaded_values[0] >= 2:
            self.loaded_values[0] -= 1
            if self.loaded_values[1] > 0:
                self.loaded_values[1] -= 1
            self.round_counter.text = str(self.loaded_values[0])
            self.cp_counter.text = str(self.loaded_values[1])
        else:
            pass

    def increase_cp(self, obj):
        if self.loaded_values[1] <= 255:
            self.loaded_values[1] += 1
            self.cp_counter.text = str(self.loaded_values[1])
        else:
            pass

    def decrease_cp(self, obj):
        if self.loaded_values[1] >= 1:
            self.loaded_values[1] -= 1
            self.cp_counter.text = str(self.loaded_values[1])
        else:
            pass

    def increase_prim(self, obj):
        if self.loaded_values[2] <= 119:
            self.loaded_values[2] += 5
            self.prim_counter.text = str(self.loaded_values[2])
        else:
            pass

    def decrease_prim(self, obj):
        if self.loaded_values[2] >= 1:
            self.loaded_values[2] -= 5
            self.prim_counter.text = str(self.loaded_values[2])
        else:
            pass

    def increase_sec1(self, obj):
        if self.loaded_values[3] <= 14:
            self.loaded_values[3] += 1
            self.sec1_counter.text = str(self.loaded_values[3])
        else:
            pass

    def decrease_sec1(self, obj):
        if self.loaded_values[3] >= 1:
            self.loaded_values[3] -= 1
            self.sec1_counter.text = str(self.loaded_values[3])
        else:
            pass

    def increase_sec2(self, obj):
        if self.loaded_values[4] <= 14:
            self.loaded_values[4] += 1
            self.sec2_counter.text = str(self.loaded_values[4])
        else:
            pass

    def decrease_sec2(self, obj):
        if self.loaded_values[4] >= 1:
            self.loaded_values[4] -= 1
            self.sec2_counter.text = str(self.loaded_values[4])
        else:
            pass

    def increase_sec3(self, obj):
        if self.loaded_values[5] <= 14:
            self.loaded_values[5] += 1
            self.sec3_counter.text = str(self.loaded_values[5])
        else:
            pass

    def decrease_sec3(self, obj):
        if self.loaded_values[5] >= 1:
            self.loaded_values[5] -= 1
            self.sec3_counter.text = str(self.loaded_values[5])
        else:
            pass

    def sum_up(self, obj):
        final_score = 0
        o = 2
        while o <= 5:
            final_score += self.loaded_values[o]
            o += 1
        toast("Final score is: " + str(final_score))

    def update_values(self):
        try:
            file = open("Krowbar.txt", "r")
            z = 0
            for x in file:
                self.loaded_values[z] = (int(x))
                z += 1
            file.close()
        except FileNotFoundError:
            file = open("Krowbar.txt", "x")
            file.close()

    def on_stop(self):
        self.save(obj=None)

    def save(self, obj):
        file = open("Krowbar.txt", "w")
        for i in self.loaded_values:
            file.write((str(i)+'\n'))

        file.close()

    def reset_values(self, obj):
        self.loaded_values = [1, 0, 0, 0, 0, 0]
        self.round_counter.text = str(self.loaded_values[0])
        self.cp_counter.text = str(self.loaded_values[1])
        self.prim_counter.text = str(self.loaded_values[2])
        self.sec1_counter.text = str(self.loaded_values[3])
        self.sec2_counter.text = str(self.loaded_values[4])
        self.sec3_counter.text = str(self.loaded_values[5])

    def wakawaka(self, object):
        print("waka waka")


if __name__ == "__main__":
    app = KrowBarApp()
    app.run()
