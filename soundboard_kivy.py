from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
import requests
import tempfile

# all your sound maps
sound_map = {
    "Ahh Fade": "https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/ahhh_fading_scream.mp3",
    "I Love": "https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/i_love_repo.mp3",
    "Dissapear":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/disappearing_man.mp3",
    "Leave Me Alone":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/leave_me_alone_akira.mp3",
    "Noooo":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/reed_no.mp3",
    "My Leg":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/my_leg.mp3",
    "Swallowed Up":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/swallowed_up.mp3",
    "That's Gotta Be Racist":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/thats_gotta_be_racist.mp3",
    "Dissapointed":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/spongebob_disappointed_sound.mp3",
    "Kono Dio Dia":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/kono_dio_da.mp3",
    "The Alien":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/the_alien_ben_salisbury.mp3",
    "Can I Pet That Dawg":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/can_i_pet_that_dawg.mp3",
    "Bass Drop":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/bass-drop.mp3",
    "Dolphin Laugh":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/dolphin_laugh.mp3",
    "Edp Bell":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/edp-bell.mp3",
    "GET OUT":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/get-out.mp3",
    "Fortnite Down":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/fortnite-down.mp3",
    "GTA Wasted":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/gta-wasted.mp3",
    "Hell's Kitchen Suspense":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/hells-kitchen-suspense.mp3",
    "KMS":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/kms.mp3",
    "Legalize Nukes":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/legalize-nuclear-bombs.mp3",
    "Mcdonald's Beeping":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/mcdonalds-beeping.mp3",
    "mistful plays":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/mistful-plays-untitled.mp3",
    "Oh My God Bruh":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/oh-my-god-bruh.mp3",
    "Oh Brother This Guy Stinks":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/oh-brother-this-guy-stinks.mp3",
    "Price is Right Trombone":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/price-is-right-trombone.mp3",
    "Rizz":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/rizz-sound.mp3",
    "Same Shit Different Day":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/same-shit-different-day.mp3",
    "Prowler":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/the-prowler-theme.mp3",
    "The Spanish Vote":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/the-spanish-vote.mp3",
    "Ultra Instinct":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/ultra-instinct.mp3",
    "Uncle Ruckus":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/uncle-ruckus-theme.mp3",
    "Vine Boom":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/vine-boom.mp3",
    "Clap If Your Care":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/wendy-williams-clap-if-you-care.mp3",
    "What the Dog Doin":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/what_the_dog_doin.mp3",
    "What the Hell":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/what_the_hell.mp3",
    "Windows Shutdown":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/windows-shutdown.mp3",
    "Woo Yeah Baby":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/woo-yeah-charlie.mp3",
    "You Need to Leave":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/you-need-to-leave.mp3",
    "WTHelly":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/wthelly.mp3",
    "Moaning Plankton":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/moaning-plankton.mp3"
}

sitcom_sounds = {
  "Aww":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/sitcom-awww.mp3",
  "Gasp":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/sitcom-gasp.mp3",
  "Laugh":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/sitcom-laugh-track.mp3",
  "Ohhh":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/sitcom-ohhh.mp3",
  "Wooo":"https://zechariahdbucket.s3.us-east-2.amazonaws.com/Sound+Board+sounds/sitcom-woo.mp3",
}

temp_files = {}

class SoundBoardApp(App):
    def build(self):
        self.current_sound = None

        root = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Scrollable area
        scroll_view = ScrollView(size_hint=(1, 1))

        # Container for all scrollable content
        content = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))

        # Meme sounds section
        content.add_widget(Label(text="Meme Sound Effects", font_size=20, size_hint_y=None, height=50, padding=5))
        meme_grid = GridLayout(cols=3, spacing=5, size_hint_y=None)
        meme_grid.bind(minimum_height=meme_grid.setter('height'))

        for label in sound_map:
            btn = Button(text=label, size_hint_y=None, height=40)
            btn.bind(on_press=lambda inst, l=label: self.play_sound(l, sound_map))
            meme_grid.add_widget(btn)

        content.add_widget(meme_grid)

        # Sitcom section
        content.add_widget(Label(text="Sitcom Sound Effects", font_size=20, size_hint_y=None, height=40))
        sitcom_grid = GridLayout(cols=2, spacing=5, size_hint_y=None)
        sitcom_grid.bind(minimum_height=sitcom_grid.setter('height'))

        for label in sitcom_sounds:
            btn = Button(text=label, size_hint_y=None, height=40)
            btn.bind(on_press=lambda inst, l=label: self.play_sound(l, sitcom_sounds))
            sitcom_grid.add_widget(btn)

        content.add_widget(sitcom_grid)
        scroll_view.add_widget(content)
        root.add_widget(scroll_view)
        # Stop button
        stop_btn = Button(text="STOP SOUND", background_color=(1,0,0,1), size_hint_y=None, height=50)
        stop_btn.bind(on_press=self.stop_sound)
        root.add_widget(stop_btn)


        return root

    def play_sound(self, label, map):
        url = map[label]
        if label not in temp_files:
            print(f"Downloading {label}...")
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
                    tmp.write(response.content)
                    tmp.close()
                    temp_files[label] = tmp.name
                else:
                    print("Download failed.")
                    return
            except Exception as e:
                print(f"Error: {e}")
                return

        if self.current_sound:
            self.current_sound.stop()
        self.current_sound = SoundLoader.load(temp_files[label])
        if self.current_sound:
            self.current_sound.play()

    def stop_sound(self, instance):
        if self.current_sound:
            self.current_sound.stop()

if __name__ == "__main__":
    SoundBoardApp().run()
