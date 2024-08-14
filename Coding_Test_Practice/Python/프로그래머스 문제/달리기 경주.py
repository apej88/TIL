def solution(players, callings):
    player_index = {player: i for i, player in enumerate(players)}
    for calling in callings:
        idx = player_index[calling]
        if idx > 0:
            player_index[players[idx-1]], player_index[players[idx]] = idx, idx-1
            players[idx-1], players[idx] = players[idx], players[idx-1]
    return players