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
  int sz[21] = {1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5};
  int dx[4] = {1, 1, -1, -1};
  int dy[4] = {-1, -1, 1, 1};
  ll getWeight (Board x, PieceList used) {
    vector<Move> t = game_util::GetValidMoves(x, player, used);
    int len = (int) t.size();
    ll res = 0;
    for (int i = 0; i < len; ++i) {
      int id = t[i].piece().id() / 8;
      res = res + sz[id] * sz[id] * sz[id] * 100;
    }
    // cout << "done" << endl;
    int cnt = 0, cnt2 = 0;
    for (int i = 0; i < 14; ++i) {
      for (int j = 0; j < 14; ++j) {
        if (x[i][j] == player) {
          for (int k = 0; k < 4; ++k) {
           int nx = i + dx[k], ny = j + dy[k]; 
           if (nx < 0 || nx >= 14 || ny < 0 || ny >= 14) continue;
           if (!x[nx][ny]) cnt++;
          }
        } else if (x[i][j] == opponent) {
          for (int k = 0; k < 4; ++k) {
           int nx = i + dx[k], ny = j + dy[k]; 
           if (nx < 0 || nx >= 14 || ny < 0 || ny >= 14) continue;
           if (!x[nx][ny]) cnt++;
          }
        }
      }
    }
    res = res + cnt * cnt * cnt - cnt2 * cnt2 * cnt2;
    int opponent = (player == 1 ? 2 : 1);
    t = game_util::GetValidMoves(x, opponent, used);
    len = (int) t.size();
    for (int i = 0; i < len; ++i) {
      int id = t[i].piece().id() / 8;
      res = res - sz[id] * sz[id] * sz[id] * 100;
    }
    return res;
  }
  Move move(const vector<Move>& valid_moves) {
    int len = valid_moves.size();
    Board current = current_game->board();
    ll mx = LLONG_MIN;
    assert(len != 0);
    int tot = 0;
    for (int i = 0; i < len; ++i) {
        Board tmp = game_util::ApplyMove(current, valid_moves[i]);
        PieceList used = (current_game->used_pieces()).first;
        used[valid_moves[i].piece().id() / 8] = true;
        ll weight = getWeight(tmp, used);
        if (weight > mx) {
          mx = weight;
          tot = 0;
        }
        if (weight == mx) arr[++tot] = i;
    }
    uniform_int_distribution<int> d(1, tot);
    return valid_moves[arr[d(g)]];
  }
};

unique_ptr<Player> get() {
  return unique_ptr<Player>(new PlayerImpl());
}
}
