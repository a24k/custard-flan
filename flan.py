from custardkit.custard import Custard
from custardkit.custard import InputStyle, Language, Metadata
from custardkit.custard import Interface, KeyStyle, GridFitLayout, GridFitSpecifier
from custardkit.custard import KeyData, CustomKey
from custardkit.custard import KeyDesign, TextLabel, MainAndSubLabel, KeyColor
from custardkit.custard import InputAction, LongpressAction
from custardkit.custard import FlickVariationData, FlickDirection
from custardkit.custard import Variation, VariationDesign

custard = Custard(
    identifier="flan",
    language=Language.ja_JP,
    input_style=InputStyle.direct,
    metadata=Metadata(
        custard_version="1.0",
        display_name="flan v0.1.0",
    ),
    interface=Interface(
        key_style=KeyStyle.tenkey_style,
        key_layout=GridFitLayout(row_count=11, column_count=4),
        keys=[
            KeyData(  # あ行
                specifier=GridFitSpecifier(x=2, y=0, width=2),
                key=CustomKey(
                    design=KeyDesign(
                        label=MainAndSubLabel(main="あ", sub="ぁ"),
                        color=KeyColor.normal,
                    ),
                    press_actions=[InputAction("あ")],
                    longpress_actions=LongpressAction(
                        start=[InputAction("ぁ")],
                    ),
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="い")),
                                press_actions=[
                                    InputAction("い"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぃ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.top,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="う")),
                                press_actions=[
                                    InputAction("う"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぅ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.right,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="え")),
                                press_actions=[
                                    InputAction("え"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぇ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.bottom,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="お")),
                                press_actions=[
                                    InputAction("お"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぉ")]
                                ),
                            ),
                        ),
                    ],
                ),
            ),
            KeyData(  # か行
                specifier=GridFitSpecifier(x=4, y=0, width=2),
                key=CustomKey(
                    design=KeyDesign(
                        label=MainAndSubLabel(main="か", sub="が"),
                        color=KeyColor.normal,
                    ),
                    press_actions=[InputAction("か")],
                    longpress_actions=LongpressAction(
                        start=[InputAction("が")],
                    ),
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="き")),
                                press_actions=[
                                    InputAction("き"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぎ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.top,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="く")),
                                press_actions=[
                                    InputAction("く"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぐ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.right,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="け")),
                                press_actions=[
                                    InputAction("け"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("げ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.bottom,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="こ")),
                                press_actions=[
                                    InputAction("こ"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ご")]
                                ),
                            ),
                        ),
                    ],
                ),
            ),
            KeyData(  # さ行
                specifier=GridFitSpecifier(x=6, y=0, width=2),
                key=CustomKey(
                    design=KeyDesign(
                        label=MainAndSubLabel(main="さ", sub="ざ"),
                        color=KeyColor.normal,
                    ),
                    press_actions=[InputAction("さ")],
                    longpress_actions=LongpressAction(
                        start=[InputAction("ざ")],
                    ),
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="し")),
                                press_actions=[
                                    InputAction("し"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("じ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.top,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="す")),
                                press_actions=[
                                    InputAction("す"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ず")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.right,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="せ")),
                                press_actions=[
                                    InputAction("せ"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぜ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.bottom,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="そ")),
                                press_actions=[
                                    InputAction("そ"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぞ")]
                                ),
                            ),
                        ),
                    ],
                ),
            ),
            KeyData(  # た行
                specifier=GridFitSpecifier(x=2, y=1, width=2),
                key=CustomKey(
                    design=KeyDesign(
                        label=MainAndSubLabel(main="た", sub="だ"),
                        color=KeyColor.normal,
                    ),
                    press_actions=[InputAction("た")],
                    longpress_actions=LongpressAction(
                        start=[InputAction("だ")],
                    ),
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="ち")),
                                press_actions=[
                                    InputAction("ち"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぢ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.top,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="つ")),
                                press_actions=[
                                    InputAction("つ"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("っ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.right,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="て")),
                                press_actions=[
                                    InputAction("て"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("で")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.bottom,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="と")),
                                press_actions=[
                                    InputAction("と"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ど")]
                                ),
                            ),
                        ),
                    ],
                ),
            ),
            KeyData(  # な行
                specifier=GridFitSpecifier(x=4, y=1, width=2),
                key=CustomKey(
                    design=KeyDesign(
                        label=MainAndSubLabel(main="な", sub="ぱ"),
                        color=KeyColor.normal,
                    ),
                    press_actions=[InputAction("な")],
                    longpress_actions=LongpressAction(
                        start=[InputAction("ぱ")],
                    ),
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="に")),
                                press_actions=[
                                    InputAction("に"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぴ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.top,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="ぬ")),
                                press_actions=[
                                    InputAction("ぬ"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぷ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.right,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="ね")),
                                press_actions=[
                                    InputAction("ね"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぺ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.bottom,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="の")),
                                press_actions=[
                                    InputAction("の"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぽ")]
                                ),
                            ),
                        ),
                    ],
                ),
            ),
            KeyData(  # は行
                specifier=GridFitSpecifier(x=6, y=1, width=2),
                key=CustomKey(
                    design=KeyDesign(
                        label=MainAndSubLabel(main="は", sub="ば"),
                        color=KeyColor.normal,
                    ),
                    press_actions=[InputAction("は")],
                    longpress_actions=LongpressAction(
                        start=[InputAction("ば")],
                    ),
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="ひ")),
                                press_actions=[
                                    InputAction("ひ"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("び")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.top,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="ふ")),
                                press_actions=[
                                    InputAction("ふ"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぶ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.right,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="へ")),
                                press_actions=[
                                    InputAction("へ"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("べ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.bottom,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="ほ")),
                                press_actions=[
                                    InputAction("ほ"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ぼ")]
                                ),
                            ),
                        ),
                    ],
                ),
            ),
            KeyData(  # ま行
                specifier=GridFitSpecifier(x=2, y=2, width=2),
                key=CustomKey(
                    design=KeyDesign(
                        label=MainAndSubLabel(main="ま", sub=""),
                        color=KeyColor.normal,
                    ),
                    press_actions=[InputAction("ま")],
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="み")),
                                press_actions=[
                                    InputAction("み"),
                                ],
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.top,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="む")),
                                press_actions=[
                                    InputAction("む"),
                                ],
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.right,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="め")),
                                press_actions=[
                                    InputAction("め"),
                                ],
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.bottom,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="も")),
                                press_actions=[
                                    InputAction("も"),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
            KeyData(  # や行
                specifier=GridFitSpecifier(x=4, y=2, width=2),
                key=CustomKey(
                    design=KeyDesign(
                        label=MainAndSubLabel(main="や", sub="ゃ"),
                        color=KeyColor.normal,
                    ),
                    press_actions=[InputAction("や")],
                    longpress_actions=LongpressAction(
                        start=[InputAction("ゃ")],
                    ),
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="「")),
                                press_actions=[
                                    InputAction("「"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("（")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.top,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="ゆ")),
                                press_actions=[
                                    InputAction("ゆ"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ゅ")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.right,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="」")),
                                press_actions=[
                                    InputAction("」"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("）")]
                                ),
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.bottom,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="よ")),
                                press_actions=[
                                    InputAction("よ"),
                                ],
                                longpress_actions=LongpressAction(
                                    start=[InputAction("ょ")]
                                ),
                            ),
                        ),
                    ],
                ),
            ),
            KeyData(  # ら行
                specifier=GridFitSpecifier(x=6, y=2, width=2),
                key=CustomKey(
                    design=KeyDesign(
                        label=MainAndSubLabel(main="ら", sub=""),
                        color=KeyColor.normal,
                    ),
                    press_actions=[InputAction("ら")],
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="り")),
                                press_actions=[
                                    InputAction("り"),
                                ],
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.top,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="る")),
                                press_actions=[
                                    InputAction("る"),
                                ],
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.right,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="れ")),
                                press_actions=[
                                    InputAction("れ"),
                                ],
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.bottom,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="ろ")),
                                press_actions=[
                                    InputAction("ろ"),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
            KeyData(  # わ行
                specifier=GridFitSpecifier(x=4, y=3, width=2),
                key=CustomKey(
                    design=KeyDesign(
                        label=MainAndSubLabel(main="わ", sub=""),
                        color=KeyColor.normal,
                    ),
                    press_actions=[InputAction("わ")],
                    variations=[
                        FlickVariationData(
                            direction=FlickDirection.left,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="を")),
                                press_actions=[
                                    InputAction("を"),
                                ],
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.top,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="ん")),
                                press_actions=[
                                    InputAction("ん"),
                                ],
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.right,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="ー")),
                                press_actions=[
                                    InputAction("ー"),
                                ],
                            ),
                        ),
                        FlickVariationData(
                            direction=FlickDirection.bottom,
                            key=Variation(
                                design=VariationDesign(label=TextLabel(text="〜")),
                                press_actions=[
                                    InputAction("〜"),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
        ],
    ),
)

custard.write(name="flan", allow_overwrite=True)
