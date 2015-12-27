# hexchat-gitter-nick-completion
A HexChat addon that uses "@" for Gitter Nick completion

By default HexChat uses a suffix for nick completion when pressing
<Tab>, if typed at the beginning of a message (usually a colon,
set in the preferences).

If you use Gitter from HexChat this doesn't go well with "mentions",
that need @username to work.
This addon changes this behavior only for channels opened in
Gitter irc server, placing the @ at the beginning of the nick and
then cycles the matching nicks as usual.

## Install
Download the `gitter-nick-completion.py` file and put it in the
addons directory (usually `~/.config/hexchat/addons` on Linux and
%APPDATA%\HexChat\addons on Windows), or load it from the "Plugins
and scripts" dialog you can access from the "Settings" menu.
