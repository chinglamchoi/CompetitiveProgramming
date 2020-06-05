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
  int otot;
  int totcnt;
  pair<int, int> score;
  PieceList my, opp;
public:
  int getUsedPiece () {
    PieceList used = current_game->used_pieces().first;
    int res = 0;
    for (int i = 0; i < 21; ++i)
      if (!used[i]) res++;
    return res;
  }
  void initialize(int player_number, shared_ptr<Game> game, int seed) {
    current_game = game;
    g = mt19937(seed);
    player = player_number;
    opponent = (player == 1 ? 2 : 1);
    otot = 0;
  }
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
  long double getWeight (Board x, Move m) {
    Board new_board = game_util::ApplyMove(x, m);
    int id2 = m.piece().name();
    vector<Move> valid = game_util::GetValidMoves(new_board, opponent, opp);
    int len = (int) valid.size();
    long double res = 0;
    for (int i = 0; i < len; ++i) {
      int id = valid[i].piece().name();
      res = res - sz[id] * sz[id] * (score.first > score.second ? sz[id] : 1); 
    }
    long double mn = 1000000000;
    for (int i = 0; i < 14; ++i) {
      for (int j = 0; j < 14; ++j) {
        if (new_board[i][j] == player) {
          if (player == 1) {
            mn = min(mn, (long double) abs(13 - i) + abs(13 - j));
          } else {
            mn = min(mn, (long double) i + j);
          }
        }
      }
    }
    res = res + (14 - mn) * (14 - mn) * 0.7;
    res = res + sz[id2] * (14 * 14 - getSparse()) * 0.3;
    return res;
  }
  Move move(const vector<Move>& valid_moves) {
    tie(my, opp) = current_game->used_pieces();
    score = game_util::GetScore(current_game->board());
    long double mx = -1000000000000;
    if (player == 2) {
      swap(my, opp);
      swap(score.first, score.second);
    }
    int len = (int) valid_moves.size();
    Board x = current_game->board();
    int tot = 0;
    for (int i = 0; i < len; ++i) {
      long double weight = getWeight(x, valid_moves[i]);
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
