import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk, Pango

class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.Gtk4App")

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self)
        window.set_title("Install MacOS XFCE theme")
        window.set_default_size(720, 480)
        window.set_name("main")
        
        css = b"""
        #main {
            background-color: #ececec;
            padding-bottom: 0px;
        }
        
        #installBox {
            border: 1px solid #D4D4D4;
            padding: 0px;
            /*width: 20px;*/
            background-color: white;
        }
        
        #installerTxt {
            color: black;
            font-size: 15px;
            margin: 16px;
            margin-left: 10px;
            margin-right: 3px;
        }
        
        #installerBtn {
            border-radius: 5px;
            border: 0.4px solid #a3a3a3;
            min-height: 3px;
            color: black;
            background-color: white;
            outline: none;
            padding-top: -500px;
            padding-bottom: -50px;
        }
        
        button#installerBtn:active {
            /*background-color: #3879f6;*/
            /*background: #2B6EF6;*/
            background: linear-gradient(0deg, rgba(43, 110, 246, 1) 0%, rgba(112, 160, 243, 1) 100%);
            background-color: transparent;
            /*box-shadow: none;
            filter: none;
            -gtk-icon-filter: none;*/
            color: white;
        }
        
        #installerControlsContainer {
            padding: 0px;
            margin-bottom: 0px;
        }
        
        #leftBox {
            padding-top: 30px;
        }
        
        #installerTitle {
            color: black;
            font-size: 15px;
        }
        """

        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)

        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),   # ✅ correct
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        box.set_margin_top(20)
        box.set_margin_bottom(20)
        box.set_margin_start(20)
        box.set_margin_end(20)
        
        
        leftBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        leftBox.set_name("leftBox")
        leftBox.set_size_request(215, 0)
        leftBox.set_halign(Gtk.Align.END)
        leftBox.set_hexpand(True)
        leftBox.set_vexpand(True)
        box.append(leftBox)
        
        installationStepContainer1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        installationStepContainer1.set_halign(Gtk.Align.END)
        installationStepContainer1.set_hexpand(True)
        leftBox.append(installationStepContainer1)
        
        
        
        rightBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        #rightBox.set_name("installBox")
        #rightBox.set_size_request(380, 0)
        rightBox.set_halign(Gtk.Align.END)
        rightBox.set_hexpand(True)
        rightBox.set_vexpand(True)
        box.append(rightBox)
        
        self.label = Gtk.Label()
        self.label.set_text("Welcome to the Installer")
        self.label.set_halign(Gtk.Align.START)
        self.label.set_name("installerTitle")
        self.label.set_margin_start(5)
        rightBox.append(self.label)
        
        installBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        installBox.set_name("installBox")
        installBox.set_size_request(470, 380)
        installBox.set_halign(Gtk.Align.END)
        rightBox.append(installBox)
        
        #installBoxTxt = Gtk.Label(label="You will be guided through the steps necessary to install this softwareeeeeeeee.")
        installBoxTxt = Gtk.Label()
        installBoxTxt.set_text("You will be guided through the steps necessary to install this software.")
        installBoxTxt.set_halign(Gtk.Align.START)
        installBoxTxt.set_vexpand(True)
        installBoxTxt.set_valign(Gtk.Align.START)
        installBoxTxt.set_wrap(True)
        installBoxTxt.set_wrap_mode(Gtk.WrapMode.WORD)
        installBoxTxt.set_max_width_chars(80)
        #installBoxTxt.set_size_request(465, 375)
        installBoxTxt.set_name("installerTxt")
        installBox.append(installBoxTxt)
        
        installerControlsContainer = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        installerControlsContainer.set_name("installerControlsContainer")
        installerControlsContainer.set_size_request(420, 1)
        installerControlsContainer.set_halign(Gtk.Align.END)
        rightBox.append(installerControlsContainer)

        continueBtn = Gtk.Button(label="Continue")
        backBtn = Gtk.Button(label="Go Back")
        continueBtn.connect("clicked", self.on_continueBtn_clicked)
        backBtn.connect("clicked", self.on_continueBtn_clicked)
        continueBtn.set_halign(Gtk.Align.END)
        backBtn.set_halign(Gtk.Align.END)
        continueBtn.set_name("installerBtn")
        backBtn.set_name("installerBtn")
        backBtn.set_hexpand(True)
        
        installerControlsContainer.append(backBtn)
        installerControlsContainer.append(continueBtn)
                
        window.set_child(box)
        window.present()
        
    global installerStep
    global screenTitles
    installerStep = 0
    screenTitles = ["Welcome to the Installer", "Choose theme components"]
    
    def on_continueBtn_clicked(self, continueBtn):
        global installerStep
        global screenTitles
        
        installerStep += 1
        if installerStep < len(screenTitles):
            self.label.set_text(screenTitles[installerStep])

app = MyApp()
app.run()