#include <memory>
#include <random>
#include <types.h>
#include <game_util.h>
#include<bits/stdc++.h>
using namespace std;
using namespace game;

namespace PLAYER {
  
class PlayerImpl : public Player {
private:
  mt19937 g;
  shared_ptr<Game> current_game;
  int player;
public:
  void initialize(int player_number, shared_ptr<Game> game, int seed) {
    current_game = game;
    player = player_number;
  }
  
  Move move(const vector<Move>& valid_moves) {
    int len = valid_moves.size();
    Board current = current_game->board();
    int mx = -1, idx = -1;
    assert(len != 0);
    for (int i = 0; i < len; ++i) {
        Board tmp = current;
        game_util::ApplyMove(tmp, valid_moves[i]);
        PieceList used = (current_game->used_pieces()).first;
        used[valid_moves[i].piece().id()] = true;
        vector<Move> tmp2 = game_util::GetValidMoves(tmp, player, used);
        if ((int)tmp2.size() > mx) {
            mx = tmp2.size();
            idx = i;
        }
    }
    assert(idx != -1);
    return valid_moves[idx];
  }
};

unique_ptr<Player> get() {
  return unique_ptr<Player>(new PlayerImpl());
}
}
