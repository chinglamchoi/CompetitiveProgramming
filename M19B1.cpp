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
  int player, opponent;
  int arr[100005];
public:
  void initialize(int player_number, shared_ptr<Game> game, int seed) {
    current_game = game;
    g = mt19937(seed);
    opponent = (player == 1 ? 2 : 1);
    player = player_number;
  }
  int getUsedPiece () {
    PieceList used = current_game->used_pieces().first;
    int res = 0;
    for (int i = 0; i < 21; ++i)
      if (!used[i]) res++;
    return res;
  }
  int getSparse () {
    Board x = current_game->board();
    int res = 0;
    for (int i = 0; i < 14; ++i)
      for (int j = 0; j< 14; ++j)
        if (!x[i][j]) res++;
    return res;
  }
  int sz[21] = {1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5};
  int dx[4] = {1, 1, -1, -1};
  int dy[4] = {-1, -1, 1, 1};
  ll getWeight2 (Board x, PieceList used) {
    int opponent = (player == 1 ? 2 : 1);
    vector<Move> t = game_util::GetValidMoves(x, opponent, used);
    int len = (int) t.size();
    ll res = 0;
    for (int i = 0; i < len; ++i) {
      int id = t[i].piece().id() / 8;
      res = res - sz[id] * sz[id] * sz[id] * 100;
    }
    return res;
  }
  ll getWeight1 (Board x, PieceList used) {
    vector<Move> t = game_util::GetValidMoves(x, player, used);
    int len = (int) t.size();
    ll res = 0;
    for (int i = 0; i < len; ++i) {
      int id = t[i].piece().id() / 8;
      res = res + sz[id] * sz[id] * sz[id] * 100;
    }
    return res;
  }
  Move move(const vector<Move>& valid_moves) {
    int len = valid_moves.size();
    Board current = current_game->board();
    ll mx = LLONG_MIN, mx2 = LLONG_MIN;
    assert(len != 0);
    int tot = 0;
    for (int i = 0; i < len; ++i) {
        Board tmp = game_util::ApplyMove(current, valid_moves[i]);
        PieceList used = (current_game->used_pieces()).first;
        used[valid_moves[i].piece().id() / 8] = true;
        ll weight = getWeight2(tmp, used);
        ll weight2 = getWeight1(tmp, used);
        if (weight > mx) {
          mx = weight;
          mx2 = LLONG_MIN;
          tot = 0;
        }
        if (weight == mx && weight2 > mx2) {
          mx2 = weight2;
          tot = 0;
        }
        if (weight == mx && weight2 == mx2) arr[++tot] = i;
    }
    uniform_int_distribution<int> d(1, tot);
    return valid_moves[arr[d(g)]];
  }
};

unique_ptr<Player> get() {
  return unique_ptr<Player>(new PlayerImpl());
}
}
