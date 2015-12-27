# hexchat-gitter-nick-completion
A HexChat addon that uses "@" for nick completion on Gitter's IRC gateway


By default HexChat uses a suffix for nick completion when pressing `<Tab>`, if
the nick is typed at the beginning of a message (it usually is a colon, set in
the preferences).

If you use Gitter from HexChat this doesn't go well with "mentions", that need
`@username` to work. This addon changes this behavior only for channels opened
using the Gitter irc server, placing the @ at the beginning of the nick and then
cycles the matching nicks as usual.

## Install
Download the file `gitter-nick-completion.py` and put it in the HexChat addons
directory (usually `~/.config/hexchat/addons` on Linux and
`%APPDATA%\HexChat\addons` on Windows), or load it from the "Plugins and
scripts" dialog you can access from the "Settings" menu.