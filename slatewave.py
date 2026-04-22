import sublime
import sublime_plugin


class SlatewaveActivateCommand(sublime_plugin.ApplicationCommand):
    """Set both the Slatewave color scheme and the Slatewave UI theme in one step."""

    def run(self):
        prefs = sublime.load_settings("Preferences.sublime-settings")
        prefs.set("color_scheme", "Packages/Slatewave/Slatewave.sublime-color-scheme")
        prefs.set("theme", "Slatewave.sublime-theme")
        sublime.save_settings("Preferences.sublime-settings")
        sublime.status_message("Slatewave activated")
