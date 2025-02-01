from enum import StrEnum, unique
from typing import Literal, TypeAlias, TypedDict, overload


@unique
class CardTypeEnum(StrEnum):
    info = "info"
    cta = "cta"
    # poll = "poll"


# Almost the same as Enum, the `match` statement fail if we don't handle a new value
CardTypeLiteral: TypeAlias = Literal["info", "cta"]


class CardInfoInput(TypedDict):
    info: str


class CardCtaInput(TypedDict):
    cta_txt: str
    cta_link: str


class CardInfoResult(TypedDict):
    txt: str


class CardCtaResult(TypedDict):
    txt: str
    link: str


@overload
def send(card_type: Literal["info"], card_info: CardInfoInput) -> CardInfoResult:
    ...


@overload
def send(card_type: Literal["cta"], card_info: CardCtaInput) -> CardCtaResult:
    ...


def send(
    card_type: CardTypeLiteral, card_info: CardInfoInput | CardCtaInput
) -> CardInfoResult | CardCtaResult:
    match card_type:
        case "info":
            return {"txt": card_info["info"]}
        case "cta":
            return {"txt": card_info["cta_txt"], "link": card_info["cta_link"]}


# Auto-completion ✨
res = send(card_type="info", card_info={"info": "blablabla"})
res["txt"]
# res["link"]  # <-- "link" is not a defined key in "CardInfoResult" ❌

# Auto-completion ✨
res = send(card_type="cta", card_info={"cta_link": "link.com", "cta_txt": "lien"})
res["txt"]
res["link"]  # ✅

# All of this doesn't work with pyright
# res = send(card_type="non_existing", card_info={"info": "blablabla"})  # ❌
# res = send(card_type="cta", card_info={"info": "blablabla"})  # ❌
# res = send(card_type="cta", card_info={"cta_link": "link.com"})  # ❌
