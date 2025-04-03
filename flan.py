from custardkit.custard import Custard
from custardkit.custard import InputStyle, Language, Metadata
from custardkit.custard import Interface, KeyStyle, GridFitLayout

custard = Custard(
    identifier="flan",
    language=Language.ja_JP,
    input_style=InputStyle.direct,
    metadata=Metadata(
        custard_version="1.0",
        display_name="flan v0.0.1",
    ),
    interface=Interface(
        key_style=KeyStyle.tenkey_style,
        key_layout=GridFitLayout(row_count=6, column_count=4),
        keys=[],
    ),
)

custard.write(name="flan", allow_overwrite=True)
