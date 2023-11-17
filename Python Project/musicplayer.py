import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playlist = []
        self.current_track = 0
        self.volume = 0.5  # Default volume (0.0 to 1.0)

    def add_to_playlist(self, folder_path):
        if os.path.isdir(folder_path):
            self.playlist.extend([os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".mp3")])
        else:
            print("Invalid folder path.")

    def play(self):
        if not self.playlist:
            print("Playlist is empty. Add songs to the playlist.")
            return

        pygame.mixer.music.load(self.playlist[self.current_track])
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play()

        print(f"Now playing: {self.playlist[self.current_track]}")

        while pygame.mixer.music.get_busy():
            choice = input("Enter 'p' to pause, 'r' to resume, 'n' to play the next track, 'q' to quit: ").lower()

            if choice == 'p':
                pygame.mixer.music.pause()
            elif choice == 'r':
                pygame.mixer.music.unpause()
            elif choice == 'n':
                self.current_track = (self.current_track + 1) % len(self.playlist)
                pygame.mixer.music.load(self.playlist[self.current_track])
                pygame.mixer.music.play()
                print(f"Now playing: {self.playlist[self.current_track]}")
            elif choice == 'q':
                pygame.mixer.music.stop()
                break
            else:
                print("Invalid choice. Try again.")

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))  # Keep volume within the range of 0.0 to 1.0
        pygame.mixer.music.set_volume(self.volume)

if __name__ == "__main__":
    player = MusicPlayer()

    folder_path = input("Enter the path to your music folder: ")
    player.add_to_playlist(folder_path)

    volume = float(input("Enter the volume level (0.0 to 1.0): "))
    player.set_volume(volume)

    player.play()
