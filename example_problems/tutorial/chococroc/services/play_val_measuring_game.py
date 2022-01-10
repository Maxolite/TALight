#!/usr/bin/env python3
import sys

from TALinputs import TALinput
from multilanguage import Env, Lang, TALcolors

import chococroc_lib as cl

# METADATA OF THIS TAL_SERVICE:
problem="chococroc"
service="play_val_measuring_game"

args_list = [
    ('m',int),
    ('n',int),
    ('nim',int),
    ('player',int),
    ('watch_value',str)
]

ENV =Env(args_list)
TAc =TALcolors(ENV)
LANG=Lang(ENV, TAc, lambda fstring: eval(f"f'{fstring}'"))

# START CODING YOUR SERVICE:

m=ENV['m']
n=ENV['n']
nim=ENV['nim']

if ENV['watch_value'] == 'watch_winner':
    if (cl.grundy_sum(cl.grundy_val(m, n), nim) > 0):
        TAc.print(LANG.render_feedback("watch-winner-user-after-server-sum", f'You want to watch the winner: starting from this configuration ({m}, {n}) and a nim tower of height {nim} you will win the game'), "green", ["bold"])
    else:
        TAc.print(LANG.render_feedback("watch-winner-server-after-server-sum", f'You want to watch the winner: starting from this configuration ({m}, {n}) and a nim tower of height {nim} i will win the game'), "green", ["bold"])
elif ENV ['watch_value'] == 'num_winning_moves':
    win_moves = cl.winning_moves(m, n, nim)
    win_moves.discard((None, None))
    count_win_moves=cl.count_winning_moves_nim(m, n, nim)
    if (len(win_moves)+count_win_moves)>0:
        TAc.print(LANG.render_feedback("num-winning-moves-n-choco-nim", f'You want to watch the number of winning moves: for the current configuration ({m}, {n}) and the nim tower of height {nim} the number of winning moves is {len(win_moves)+count_win_moves}'), "green", ["bold"])
    else:
        TAc.print(LANG.render_feedback("num-winning-moves-n-choco-nim", f'You want to watch the number of winning moves: for the current configuration ({m}, {n}) and the nim tower of height {nim} there are not winning moves'), "green", ["bold"])
elif ENV ['watch_value'] == 'list_winning_moves':
    win_moves = cl.winning_moves(m, n, nim)
    win_moves.discard((None, None))
    win_moves_with_nim={(None,None,None)}
    for tuple in win_moves:
        tuple+=(nim,)
        win_moves_with_nim.add(tuple)
    win_moves_with_nim.discard((None,None,None))
    win_moves_with_nim.update(cl.winning_moves_nim(m, n, nim))
    if len(win_moves_with_nim) > 1:
        TAc.print(LANG.render_feedback("list-multiple-winning-moves-choco-nim", f'You want to watch the list of winning moves: for the current configuration ({m}, {n}) and the nim tower of height {nim} the winning moves are {win_moves_with_nim}'), "green", ["bold"])
    elif len(win_moves_with_nim) == 1:
        TAc.print(LANG.render_feedback("list-one-winning-moves-choco-nim", f'You want to watch the list of winning moves: for the current configuration ({m}, {n}) and the nim tower of height {nim} the winning move is {win_moves_with_nim}'), "green", ["bold"])
    else:
        TAc.print(LANG.render_feedback("list-none-winning-moves-choco-nim", f'You want to watch the list of winning moves: for the current configuration ({m}, {n}) and the nim tower of height {nim} there are not winning moves'), "green", ["bold"])
elif ENV ['watch_value'] == 'watch_grundy_val':
    TAc.print(LANG.render_feedback("watch-grundy-server-move-sum", f'You want to watch the grundy value: for the current configuration ({m}, {n}) and a nim tower of height {nim} the grundy value is {cl.grundy_sum(cl.grundy_val(m, n), nim)}'), "green", ["bold"])

if ENV['player'] == 1:
    if m==1 and n==1 and nim==0:
        TAc.print(LANG.render_feedback("you-have-won-play-val", f'It is my turn to move, on conf (1,1) and a nim tower of height 0. Since this configuration admits no valid move, then I have lost this match.'), "yellow", ["bold"])
        TAc.print(LANG.render_feedback("you-won", f'You won!'), "green", ["bold"])        
        exit(0)
    new_m,new_n,new_nim=cl.computer_decision_move(m,n,nim)
    TAc.print(LANG.render_feedback("server-move-play-val", f'My move is from conf ({m},{n}) to conf ({new_m},{new_n}) and from a nim tower of height {nim} to a nim tower of height {new_nim}.\nThe turn is now to you, on conf ({new_m},{new_n}) and a nim tower of height {new_nim}'), "green", ["bold"])

    if ENV['watch_value'] == 'watch_winner':
        if (cl.grundy_sum(cl.grundy_val(new_m, new_n), new_nim) > 0):
            TAc.print(LANG.render_feedback("watch-winner-user-after-server-sum", f'You want to watch the winner: starting from this configuration ({new_m}, {new_n}) and a nim tower of height {new_nim} you will win the game'), "green", ["bold"])
        else:
            TAc.print(LANG.render_feedback("watch-winner-server-after-server-sum", f'You want to watch the winner: starting from this configuration ({new_m}, {new_n}) and a nim tower of height {new_nim} i will win the game'), "green", ["bold"])
    elif ENV ['watch_value'] == 'num_winning_moves':
        win_moves = cl.winning_moves(new_m, new_n, new_nim)
        win_moves.discard((None, None))
        count_win_moves=cl.count_winning_moves_nim(new_m, new_n, new_nim)
        if (len(win_moves)+count_win_moves)>0:
            TAc.print(LANG.render_feedback("num-winning-moves-n-choco-nim", f'You want to watch the number of winning moves: for the current configuration ({new_m}, {new_n}) and the nim tower of height {new_nim} the number of winning moves is {len(win_moves)+count_win_moves}'), "green", ["bold"])
        else:
            TAc.print(LANG.render_feedback("num-winning-moves-n-choco-nim", f'You want to watch the number of winning moves: for the current configuration ({new_m}, {new_n}) and the nim tower of height {new_nim} there are not winning moves'), "green", ["bold"])
    elif ENV ['watch_value'] == 'list_winning_moves':
        win_moves = cl.winning_moves(new_m, new_n, new_nim)
        win_moves.discard((None, None))
        win_moves_with_nim={(None,None,None)}
        for tuple in win_moves:
            tuple+=(new_nim,)
            win_moves_with_nim.add(tuple)
        win_moves_with_nim.discard((None,None,None))
        win_moves_with_nim.update(cl.winning_moves_nim(new_m, new_n, new_nim))
        if len(win_moves_with_nim) > 1:
            TAc.print(LANG.render_feedback("list-multiple-winning-moves-choco-nim", f'You want to watch the list of winning moves: for the current configuration ({new_m}, {new_n}) and the nim tower of height {new_nim} the winning moves are {win_moves_with_nim}'), "green", ["bold"])
        elif len(win_moves_with_nim) == 1:
            TAc.print(LANG.render_feedback("list-one-winning-moves-choco-nim", f'You want to watch the list of winning moves: for the current configuration ({new_m}, {new_n}) and the nim tower of height {new_nim} the winning move is {win_moves_with_nim}'), "green", ["bold"])
        else:
            TAc.print(LANG.render_feedback("list-none-winning-moves-choco-nim", f'You want to watch the list of winning moves: for the current configuration ({new_m}, {new_n}) and the nim tower of height {new_nim} there are not winning moves'), "green", ["bold"])
    elif ENV ['watch_value'] == 'watch_grundy_val':
        TAc.print(LANG.render_feedback("watch-grundy-server-move-sum", f'You want to watch the grundy value: for the current configuration ({new_m}, {new_n}) and a nim tower of height {new_nim} the grundy value is {cl.grundy_sum(cl.grundy_val(new_m, new_n), new_nim)}'), "green", ["bold"])

    m,n,nim=new_m,new_n,new_nim

while True:
    if m==1 and n==1 and nim==0:
        TAc.print(LANG.render_feedback("you-have-lost-play-val", f'It is your turn to move, on conf (1,1) and a nim tower of height 0. Since this configuration admits no valid move, then you have lost this match.'), "yellow", ["bold"])
        TAc.print(LANG.render_feedback("you-lost", f'You lost!'), "green", ["bold"])        
        exit(0)
    TAc.print(LANG.render_feedback("your-turn-play-val", f'It is your turn to move from conf ({m},{n}) or from a nim tower of height {nim} to a new conf (m,n) or a nim tower of new height.'), "yellow", ["bold"])
    TAc.print(LANG.render_feedback("user-move-play-val", f'Please, insert the three integers m, n and height separated by spaces: '), "yellow", ["bold"])
    new_m,new_n,new_nim = TALinput(int, 3, TAc=TAc)
    if new_m != m and new_n != n:
        TAc.print(LANG.render_feedback("not-valid", f'No! Your move from conf ({m},{n}) to conf ({new_m},{new_n}) is not valid.'), "red", ["bold"])
        TAc.print(LANG.render_feedback("double-move", f'You are cheating. A move can not alter both the number of rows (from {m} to {new_m}) and the number of columns (from {n} to {new_n})).'), "red", ["bold"])
        if new_nim > nim:
            TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("wrong-grow-move", f'You are cheating. A move can not increase the height of the nim tower.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("wrong-nim-move", f'You are cheating. You can not modify the height of the nim tower if you move on the chococroc game.'), "red", ["bold"])
        elif new_nim < 0:
            TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("negative-move", f'You are cheating. A move can not decrease the height of the nim tower under 0.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("wrong-nim-move", f'You are cheating. You can not modify the height of the nim tower if you move on the chococroc game.'), "red", ["bold"])
        elif new_nim!=nim:
            TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("wrong-nim-move", f'You are cheating. You can not modify the height of the nim tower if you move on the chococroc game.'), "red", ["bold"])
        exit(0)
    if new_m == m and new_n == n and new_nim == nim:
        TAc.print(LANG.render_feedback("not-valid", f'No! Your move from conf ({m},{n}) to conf ({new_m},{new_n}) is not valid.'), "red", ["bold"])
        TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
        TAc.print(LANG.render_feedback("dull-nim-move", f'You are cheating. Your move must either reduce the number of rows or the number of columns or the height of the nim tower. Otherwise, you have not really moved but simply passed.'), "red", ["bold"])
        exit(0)
    if new_m == m and new_n == n and new_nim > nim:
        TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
        TAc.print(LANG.render_feedback("wrong-grow-move", f'You are cheating. A move can not increase the height of the nim tower.'), "red", ["bold"])        
        exit(0)
    if new_m == m and new_n == n and new_nim < 0:
        TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
        TAc.print(LANG.render_feedback("negative-move", f'You are cheating. A move can not decrease the height of the nim tower under 0.'), "red", ["bold"])
        exit(0)
    if new_m != m:
        pos = m
        new_pos = new_m
    else:
        pos = n
        new_pos = new_n
    if new_pos > pos:
        TAc.print(LANG.render_feedback("not-valid", f'No! Your move from conf ({m},{n}) to conf ({new_m},{new_n}) is not valid.'), "red", ["bold"])
        TAc.print(LANG.render_feedback("increasing-move", f'With a move the value of a coordinate can not increase from {pos} to {new_pos}. On the contrary, precisely one coordinate must be decreased.'), "red", ["bold"])
        if new_nim > nim:
            TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("wrong-grow-move", f'You are cheating. A move can not increase the height of the nim tower.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("wrong-nim-move", f'You are cheating. You can not modify the height of the nim tower if you move on the chococroc game.'), "red", ["bold"])
        elif new_nim < 0:
            TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("negative-move", f'You are cheating. A move can not decrease the height of the nim tower under 0.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("wrong-nim-move", f'You are cheating. You can not modify the height of the nim tower if you move on the chococroc game.'), "red", ["bold"])
        elif new_nim!=nim:
            TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("wrong-nim-move", f'You are cheating. You can not modify the height of the nim tower if you move on the chococroc game.'), "red", ["bold"])
        exit(0)
    if new_pos < pos - (pos//2):
        TAc.print(LANG.render_feedback("not-valid", f'No! Your move from conf ({m},{n}) to conf ({new_m},{new_n}) is not valid.'), "red", ["bold"])
        TAc.print(LANG.render_feedback("excessive-move", f'No! No valid move can more than halve the value of a coordinate. (Here, 2*{new_pos}={2*new_pos} < {pos}).'), "red", ["bold"])
        if new_nim > nim:
            TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("wrong-grow-move", f'You are cheating. A move can not increase the height of the nim tower.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("wrong-nim-move", f'You are cheating. You can not modify the height of the nim tower if you move on the chococroc game.'), "red", ["bold"])
        elif new_nim < 0:
            TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("negative-move", f'You are cheating. A move can not decrease the height of the nim tower under 0.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("wrong-nim-move", f'You are cheating. You can not modify the height of the nim tower if you move on the chococroc game.'), "red", ["bold"])
        elif new_nim!=nim:
            TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
            TAc.print(LANG.render_feedback("wrong-nim-move", f'You are cheating. You can not modify the height of the nim tower if you move on the chococroc game.'), "red", ["bold"])
        exit(0)
    if (new_m!=m or new_n!=n) and new_nim!=nim:
        TAc.print(LANG.render_feedback("not-valid-nim", f'No! Your move from height {nim} to new height {new_nim} is not valid.'), "red", ["bold"])
        TAc.print(LANG.render_feedback("wrong-nim-move", f'You are cheating. You can not modify the height of the nim tower if you move on the chococroc game.'), "red", ["bold"])
        exit(0)
    if new_m==1 and new_n==1 and new_nim==0:
        TAc.print(LANG.render_feedback("you-have-won-play-val", 'It is my turn to move, on conf (1,1)  and a nim tower of height 0. Since this configuration admits no valid move, then I have lost this match.'), "yellow", ["bold"])
        TAc.print(LANG.render_feedback("you-won", f'You won!'), "green", ["bold"])        
        exit(0)

    if ENV['watch_value'] == 'watch_winner':
        if (cl.grundy_sum(cl.grundy_val(new_m, new_n), new_nim) == 0):
            TAc.print(LANG.render_feedback("watch-winner-user-after-server-sum", f'You want to watch the winner: starting from this configuration ({new_m}, {new_n}) and a nim tower of height {new_nim} you will win the game'), "green", ["bold"])
        else:
            TAc.print(LANG.render_feedback("watch-winner-server-after-server-sum", f'You want to watch the winner: starting from this configuration ({new_m}, {new_n}) and a nim tower of height {new_nim} i will win the game'), "green", ["bold"])
    elif ENV ['watch_value'] == 'num_winning_moves':
        win_moves = cl.winning_moves(new_m, new_n, new_nim)
        win_moves.discard((None, None))
        count_win_moves=cl.count_winning_moves_nim(new_m, new_n, new_nim)
        if (len(win_moves)+count_win_moves)>0:
            TAc.print(LANG.render_feedback("num-winning-moves-n-choco-nim", f'You want to watch the number of winning moves: for the current configuration ({new_m}, {new_n}) and the nim tower of height {new_nim} the number of winning moves is {len(win_moves)+count_win_moves}'), "green", ["bold"])
        else:
            TAc.print(LANG.render_feedback("num-winning-moves-n-choco-nim", f'You want to watch the number of winning moves: for the current configuration ({new_m}, {new_n}) and the nim tower of height {new_nim} there are not winning moves'), "green", ["bold"])
    elif ENV ['watch_value'] == 'list_winning_moves':
        win_moves = cl.winning_moves(new_m, new_n, new_nim)
        win_moves.discard((None, None))
        win_moves_with_nim={(None,None,None)}
        for tuple in win_moves:
            tuple+=(new_nim,)
            win_moves_with_nim.add(tuple)
        win_moves_with_nim.discard((None,None,None))
        win_moves_with_nim.update(cl.winning_moves_nim(new_m, new_n, new_nim))
        if len(win_moves_with_nim) > 1:
            TAc.print(LANG.render_feedback("list-multiple-winning-moves-choco-nim", f'You want to watch the list of winning moves: for the current configuration ({new_m}, {new_n}) and the nim tower of height {new_nim} the winning moves are {win_moves_with_nim}'), "green", ["bold"])
        elif len(win_moves_with_nim) == 1:
            TAc.print(LANG.render_feedback("list-one-winning-moves-choco-nim", f'You want to watch the list of winning moves: for the current configuration ({new_m}, {new_n}) and the nim tower of height {new_nim} the winning move is {win_moves_with_nim}'), "green", ["bold"])
        else:
            TAc.print(LANG.render_feedback("list-none-winning-moves-choco-nim", f'You want to watch the list of winning moves: for the current configuration ({new_m}, {new_n}) and the nim tower of height {new_nim} there are not winning moves'), "green", ["bold"])
    elif ENV ['watch_value'] == 'watch_grundy_val':
        TAc.print(LANG.render_feedback("watch-grundy-server-move-sum", f'You want to watch the grundy value: for the current configuration ({new_m}, {new_n}) and a nim tower of height {new_nim} the grundy value is {cl.grundy_sum(cl.grundy_val(new_m, new_n), new_nim)}'), "green", ["bold"])
    
    m,n,nim=cl.computer_decision_move(new_m,new_n,new_nim)
    TAc.print(LANG.render_feedback("server-move-play-val", f'My move is from conf ({new_m},{new_n}) to conf ({m},{n}) and from a nim tower of height {new_nim} to a nim tower of height {nim}.\nThe turn is now to you, on conf ({m},{n}) and a nim tower of height {nim}'), "green", ["bold"])

    if ENV['watch_value'] == 'watch_winner':
        if (cl.grundy_sum(cl.grundy_val(m, n), nim) > 0):
            TAc.print(LANG.render_feedback("watch-winner-user-after-server-sum", f'You want to watch the winner: starting from this configuration ({m}, {n}) and a nim tower of height {nim} you will win the game'), "green", ["bold"])
        else:
            TAc.print(LANG.render_feedback("watch-winner-server-after-server-sum", f'You want to watch the winner: starting from this configuration ({m}, {n}) and a nim tower of height {nim} i will win the game'), "green", ["bold"])
    elif ENV ['watch_value'] == 'num_winning_moves':
        win_moves = cl.winning_moves(m, n, nim)
        win_moves.discard((None, None))
        count_win_moves=cl.count_winning_moves_nim(m, n, nim)
        if (len(win_moves)+count_win_moves)>0:
            TAc.print(LANG.render_feedback("num-winning-moves-n-choco-nim", f'You want to watch the number of winning moves: for the current configuration ({m}, {n}) and the nim tower of height {nim} the number of winning moves is {len(win_moves)+count_win_moves}'), "green", ["bold"])
        else:
            TAc.print(LANG.render_feedback("num-winning-moves-n-choco-nim", f'You want to watch the number of winning moves: for the current configuration ({m}, {n}) and the nim tower of height {nim} there are not winning moves'), "green", ["bold"])
    elif ENV ['watch_value'] == 'list_winning_moves':
        win_moves = cl.winning_moves(m, n, nim)
        win_moves.discard((None, None))
        win_moves_with_nim={(None,None,None)}
        for tuple in win_moves:
            tuple+=(nim,)
            win_moves_with_nim.add(tuple)
        win_moves_with_nim.discard((None,None,None))
        win_moves_with_nim.update(cl.winning_moves_nim(m, n, nim))
        if len(win_moves_with_nim) > 1:
            TAc.print(LANG.render_feedback("list-multiple-winning-moves-choco-nim", f'You want to watch the list of winning moves: for the current configuration ({m}, {n}) and the nim tower of height {nim} the winning moves are {win_moves_with_nim}'), "green", ["bold"])
        elif len(win_moves_with_nim) == 1:
            TAc.print(LANG.render_feedback("list-one-winning-moves-choco-nim", f'You want to watch the list of winning moves: for the current configuration ({m}, {n}) and the nim tower of height {nim} the winning move is {win_moves_with_nim}'), "green", ["bold"])
        else:
            TAc.print(LANG.render_feedback("list-none-winning-moves-choco-nim", f'You want to watch the list of winning moves: for the current configuration ({m}, {n}) and the nim tower of height {nim} there are not winning moves'), "green", ["bold"])
    elif ENV ['watch_value'] == 'watch_grundy_val':
        TAc.print(LANG.render_feedback("watch-grundy-server-move-sum", f'You want to watch the grundy value: for the current configuration ({m}, {n}) and a nim tower of height {nim} the grundy value is {cl.grundy_sum(cl.grundy_val(m, n), nim)}'), "green", ["bold"])