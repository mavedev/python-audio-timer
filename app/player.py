from playsound import playsound

from .invariants import Types


def play_audio(file: Types.Path) -> None:
    playsound(file)
