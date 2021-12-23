class Driver:
    async def make_driver() -> None:
        ...

    async def connect(
        token: str,
        endpoint: str,
        session_id: str,
        guild_id: int,
        channel_id: int,
        user_id: int
    ) -> None:
        ...

    async def play(playable: Playable) -> None:
        ...

    async def leave() -> None:
        ...


class SongbirdError(Exception):
    ...


class CouldNotConnectToRTPError(SongbirdError):
    ...


class Playable:
    @staticmethod
    def bytes(bytes: bytes, stereo: bool) -> Playable:
        ...

    @staticmethod
    def ffmpeg(filename: str) -> Playable:
        ...

    @staticmethod
    def ytdl(url: str) -> Playable:
        ...

    @staticmethod
    def file(url: str) -> Playable:
        ...
