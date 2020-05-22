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
  int CountValidMoves(const Board& board, int player, const PieceList& used_pieces) {
			vector<pair<int, int>> valid_positions;
			Piece single_piece = Piece::getPiece(0);
			int cnt = 0;
			// optimization
			for (int r = 0; r < 14; r++) {
				for (int c = 0; c < 14; c++) {
					bool shares_edge = false;
					shares_edge |= r - 1 >= 0 && board[r - 1][c] == player;
					shares_edge |= r + 1 < 14 && board[r + 1][c] == player;
					shares_edge |= c - 1 >= 0 && board[r][c - 1] == player;
					shares_edge |= c + 1 < 14 && board[r][c + 1] == player;
					if (!board[r][c] && !shares_edge) {
						valid_positions.push_back({r, c});
					}
				}
			}
			vector<Move> valid_moves;
			for (int name = 0; name < 21; name++) {
				if (used_pieces[name]) {
					continue;
				}
				for (int flipped = 0; flipped < 2; flipped++) {
					for (int rotation = 0; rotation < 4; rotation++) {
						Piece piece = Piece::getPiece(name, flipped, rotation);
						for (auto& p : valid_positions) {
							Move move = Move(player, piece, p.first, p.second);
							if (game_util::IsMoveLegal(board, move)) ++cnt;
						}
					}
				}
			}
			return cnt;
		}
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
  vector<pair<int, int> > me, opp;
  ll dis (pair<int, int> a, pair<int, int> b) {
    return abs(a.first - b.first) + abs(a.second -b.second);
  }
  ll getWeight1 (Board x, PieceList used) {
    ll res = LLONG_MIN;
    me.clear(); opp.clear();
    for (int i = 0; i < 14; ++i) {
      for (int j = 0; j < 14; ++j) {
        if (x[i][j] == player) {
          me.push_back(make_pair(i, j));
        } else if (x[i][j] == opponent) {
          opp.push_back(make_pair(i, j));
        }
      }
    }
    for (int i = 0; i < (int) me.size(); ++i) {
      for (int j = 0; j < (int) opp.size(); ++j) {
        res = max(res, -dis(me[i], opp[j]));
      }
    }
    int sz = CountValidMoves(x, player, used);
    res += sz;
    return res;
  }
  Move move(const vector<Move>& valid_moves) {
    int len = valid_moves.size();
    Board current = current_game->board();
    ll mx = LLONG_MIN, mx2 = LLONG_MIN, mx3 = LLONG_MIN;
    int tot = 0;
    for (int i = 0; i < len; ++i) {
        Board tmp = game_util::ApplyMove(current, valid_moves[i]);
        PieceList used = (current_game->used_pieces()).first;
        int id = valid_moves[i].piece().id() / 8;
        used[id] = true;
        ll weight = getWeight2(tmp, used);
        ll weight2 = getWeight1(tmp, used);
        if (weight > mx) {
          mx = weight;
          mx2 = LLONG_MIN;
          mx3 = LLONG_MIN;
          tot = 0;
        }
        if (weight == mx && weight2 > mx2) {
          mx2 = weight2;
          mx3=LLONG_MIN;
          tot = 0;
        }
        if (weight == mx && weight2 == mx2 && sz[id] > mx3) {
          mx3 = sz[id];
          tot = 0;
        }
        if (weight == mx && weight2 == mx2 && sz[id] == mx3) arr[++tot] = i;
    }
    uniform_int_distribution<int> d(1, tot);
    return valid_moves[arr[d(g)]];
  }
};

unique_ptr<Player> get() {
  return unique_ptr<Player>(new PlayerImpl());
}
}
