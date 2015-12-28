#!/usr/bin/env python
# -*- coding: utf-8 -*

__module_name__ = "Gitter Nick Completion support"
__module_version__ = "0.3"
__module_description__ = "Uses @nick for nick completion on Gitter"
__author__ = "MaurizioB"

import hexchat, re
server = 'gitter.im'
nick_check = re.compile(r'[^a-zA-Z0-9\-\[\]\\\^\{\}]').search
cx_list = {}
tracked_keys = ['65288', #backspace
                ]
ignored_keys = ['65307', #esc
                ]

def check_completion(word, word_eol, userdata):
    cx = hexchat.get_context()
    if cx.get_info('server').endswith(server) and [chan.type for chan in hexchat.get_list('channels') if chan.context==hexchat.get_context()][0] == 2:
        inputbox = cx.get_info('inputbox')
        if word[0] == '65289' and len(inputbox.split()) == 1:
         #and not bool(nick_check(inputbox.split()[0])):
            chan = cx_list.get(cx.get_info('channel'))
            if chan:
                typed = chan['typed']
                cycle = chan['cycle']+1
                matching = chan['matching']
                if cycle == len(matching):
                    cycle = 0
            else:
                typed = cx.get_info('inputbox')
                if typed.startswith('@'): typed = typed[1:]
                if bool(nick_check(typed)):
                    return hexchat.EAT_NONE
                cycle = 0
                matching = []
                for user in cx.get_list('users'):
                    nick = user.nick
                    if nick.lower().startswith(typed.lower()):
                        matching.append(nick)
            if not len(matching):
                #empty list
                if cx_list.get(cx.get_info('channel')):
                    cx_list.pop(cx.get_info('channel'))
                return hexchat.EAT_NONE
            cx_list[cx.get_info('channel')] = {'typed': typed, 'matching': matching, 'cycle': cycle}
            hexchat.command('SETTEXT @{} '.format(matching[cycle]))
            hexchat.command('SETCURSOR {}'.format(len(cx.get_info('inputbox'))))
            return hexchat.EAT_ALL
        #ignoring mod and "empty" keys, but let pass backspace to clear the context dictionary
        elif (not int(word[3]) and not word[0] in tracked_keys) or word[0] in ignored_keys:
            return hexchat.EAT_NONE
        else:
            #reset context for channel
            if cx_list.get(cx.get_info('channel')):
                cx_list.pop(cx.get_info('channel'))
            return hexchat.EAT_NONE
    else:
        return hexchat.EAT_NONE

hexchat.hook_print('Key Press', check_completion)
