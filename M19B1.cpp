#include <memory>
#include <random>
#include <types.h>
#include <game_util.h>

using namespace std;
using namespace game;

namespace PLAYER {
  
class PlayerImpl : public Player {
private:
  mt19937 g;
public:
  void initialize(int player_number, shared_ptr<Game> game, int seed) {
    g = mt19937(seed);
  }
  
  Move move(const vector<Move>& valid_moves) {
    uniform_int_distribution<int> d(0, (int)valid_moves.size() - 1);
    return valid_moves[d(g)];
  }
};

unique_ptr<Player> get() {
  return unique_ptr<Player>(new PlayerImpl());
}
}
