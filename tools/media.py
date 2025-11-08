import dbus

class Media:
    def __init__(self):
        try:
            self.session_bus = dbus.SessionBus()
            self.spotify_bus = self.session_bus.get_object(
                "org.mpris.MediaPlayer2.spotify",
                "/org/mpris/MediaPlayer2"
            )
            self.spotify_properties = dbus.Interface(
                self.spotify_bus,
                "org.freedesktop.DBus.Properties"
            )
        except dbus.exceptions.DBusException:
            self.spotify_bus = None
            self.spotify_properties = None

    def get_now_playing(self):
        """
        Gets the currently playing song from Spotify.
        """
        if self.spotify_properties:
            metadata = self.spotify_properties.Get(
                "org.mpris.MediaPlayer2.Player",
                "Metadata"
            )
            if metadata:
                artist = metadata.get("xesam:artist")[0]
                title = metadata.get("xesam:title")
                return f"Currently playing: {title} by {artist}"
        return "Nothing is currently playing."

    def play_pause(self):
        """
        Toggles play/pause on Spotify.
        """
        if self.spotify_bus:
            player = dbus.Interface(self.spotify_bus, "org.mpris.MediaPlayer2.Player")
            player.PlayPause()
            return "Toggled play/pause."
        return "Could not connect to Spotify."

    def next_track(self):
        """
        Skips to the next track on Spotify.
        """
        if self.spotify_bus:
            player = dbus.Interface(self.spotify_bus, "org.mpris.MediaPlayer2.Player")
            player.Next()
            return "Skipped to the next track."
        return "Could not connect to Spotify."

    def previous_track(self):
        """
        Goes to the previous track on Spotify.
        """
        if self.spotify_bus:
            player = dbus.Interface(self.spotify_bus, "org.mpris.MediaPlayer2.Player")
            player.Previous()
            return "Went to the previous track."
        return "Could not connect to Spotify."
