#include <memory>
#include <random>
#include <types.h>
#include <game_util.h>
#include<bits/stdc++.h>
using namespace std;
using namespace game;
#define ll long long

namespace PLAYER {
  
class PlayerImpl : public Player {
private:
  mt19937 g;
  shared_ptr<Game> current_game;
  int player;
public:
  void initialize(int player_number, shared_ptr<Game> game, int seed) {
    current_game = game;
    g = mt19937(seed);
    player = player_number;
  }
  int sz[21] = {1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5};
  int dx[4] = {1, 1, -1, -1};
  int dy[4] = {-1, -1, 1, 1};
  ll getWeight (Board x, PieceList used) {
    vector<Move> t = game_util::GetValidMoves(x, player, used);
    int len = (int) t.size();
    ll res = 0;
    for (int i = 0; i < len; ++i) {
      int id = t[i].piece().id() / 8;
      // cout << id << endl;
      assert(id < 21 && id >= 0);
      res = res + sz[id] * sz[id] * sz[id] * 100;
    }
    // cout << "done" << endl;
    int chatou = 0;
    for (int i = 0; i < 14; ++i) {
      for (int j = 0; j < 14; ++j) {
        if (x[i][j] != player) continue;
        for (int k = 0; k < 4; ++k) {
          int nx = i + dx[k], ny = j + dy[k]; 
          if (nx < 0 || nx >= 14 || ny < 0 || ny >= 14) continue;
          if (!x[nx][ny]) chatou++;
        }
      }
    }
    // cout << "dnlm " << endl;
    res = res + chatou * chatou * chatou;
    int opponent = (player == 1 ? 2 : 1);
    chatou = 0;
    for (int i = 0; i < 14; ++i) {
      for (int j = 0; j < 14; ++j) {
        if (x[i][j] != opponent) continue;
        // cout << i << " " << j << endl;
        for (int k = 0; k < 4; ++k) {
          int nx = i + dx[k], ny = j + dy[k]; 
          if (nx < 0 || nx >= 14 || ny < 0 || ny >= 14) continue;
          if (!x[nx][ny]) chatou++;
        }
      }
    }
    res = res - chatou * chatou * chatou;
    t = game_util::GetValidMoves(x, opponent, used);
    len = (int) t.size();
    for (int i = 0; i < len; ++i) {
      int id = t[i].piece().id() / 8;
      // cout << id << endl;
      res = res - sz[id] * sz[id] * sz[id] * 100;
    }
    // cout << "done2" << endl;
    return res;
  }
  Move move(const vector<Move>& valid_moves) {
    int len = valid_moves.size();
    Board current = current_game->board();
    ll mx = LLONG_MIN, idx = -1;
    assert(len != 0);
    vector<int> v;
    for (int i = 0; i < len; ++i) {
        Board tmp = game_util::ApplyMove(current, valid_moves[i]);
        PieceList used = (current_game->used_pieces()).first;
        used[valid_moves[i].piece().id() / 8] = true;
        ll weight = getWeight(tmp, used);
        if (weight > mx) mx = weight, idx = i;
    }
    assert(idx != -1);
    return valid_moves[idx];
  }
};

unique_ptr<Player> get() {
  return unique_ptr<Player>(new PlayerImpl());
}
}
