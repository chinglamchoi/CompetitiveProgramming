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
    g = mt19937(seed);
  }
  
  Move move(const vector<Move>& valid_moves) {
    int len = valid_moves.size();
    Board current = current_game->board();
    int mx = -1, idx = -1;
    assert(len != 0);
    vector<int> v;
    for (int i = 0; i < len; ++i) {
        Board tmp = current;
        tmp = game_util::ApplyMove(tmp, valid_moves[i]);
        PieceList used = (current_game->used_pieces()).first;
        used[valid_moves[i].piece().id()] = true;
        vector<Move> tmp2 = game_util::GetValidMoves(tmp, player, used);
        if ((int)tmp2.size() > mx) {
            mx = (int)tmp2.size();
            idx = i;
            v.clear();
        }
        if ((int) tmp2.size() == mx) v.push_back(i);
    }
    uniform_int_distribution<int> d(0, (int)v.size() - 1);
    assert(idx != -1);
    return valid_moves[v[d(g)]];
  }
};

unique_ptr<Player> get() {
  return unique_ptr<Player>(new PlayerImpl());
}
}
