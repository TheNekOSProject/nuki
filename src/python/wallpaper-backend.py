from NekoMimi import utils as nm

_p_picsum: str = ""
_p_nekos: str = ""
_p_konachan: str = ""
_l_dir: str = ""

#config file at $HOME/.config/NekoExperience/nuki/wallpaper-engine.conf

def __provider_picsum_handler(h: int, w: int, blur :int = 0, grayscale: bool = False) -> str:
    return "string"

def __provider_nekos_handler() -> str:
    return "string"

def __provider_konachan_handler(search_kw: str) -> str:
    return "string"

def __provider_local() -> str:
    return "string"
