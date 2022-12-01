using System;
using System.Collections.Generic;

namespace Advent.Runners
{
    class Day21Runner : IRunner
    {
        private int rolls = 0;
        private int deterministic_die = 0;
        private Dictionary<(int, int, int, int), (long, long)> states = new();

        public void Go(string input)
        {
            part1(10, 2);
            part2(10, 2);
        }

        private void part1(int p_1, int p_2)
        {
            var s_1 = 0;
            var s_2 = 0;

            while (s_1 < 1000 && s_2 < 1000)
            {
                p_1 = TakeTurn(p_1);
                s_1 += p_1;

                if (s_1 >= 1000) break;

                p_2 = TakeTurn(p_2);
                s_2 += p_2;
            }

            var lost = Math.Min(s_1, s_2);

            Console.WriteLine($"part 1: {lost * rolls}");
        }

        private void part2(int p_1, int p_2)
        {
            var (p1_wins, p2_wins) = play(p_1, p_2, 0, 0);
            Console.WriteLine($"part 2: {Math.Max(p1_wins, p2_wins)}");
        }

        private (long, long) play(int p_1, int p_2, int s_1, int s_2)
        {
            if (s_1 >= 21) return (1, 0);
            if (s_2 >= 21) return (0, 1);
            if (states.ContainsKey((p_1, p_2, s_1, s_2))) return states[(p_1, p_2, s_1, s_2)];

            (long, long) wins = (0, 0);
            for (int i = 1; i <= 3; i++)
                for (int j = 1; j <= 3; j++)
                    for (int k = 1; k <= 3; k++)
                    {
                        var p = p_1 + i + j + k;
                        if (p > 10) p -= 10;
                        var s = s_1 + p;
                        var (x, y) = play(p_2, p, s_2, s);
                        wins = (wins.Item1 + y, wins.Item2 + x);
                    }
            states.Add((p_1, p_2, s_1, s_2), wins);
            return wins;
        }

        private int roll()
        {
            deterministic_die++;
            rolls++;
            if (deterministic_die > 100) deterministic_die -= 100;
            return deterministic_die;
        }

        private int TakeTurn(int from)
        {
            var rolls = roll() + roll() + roll();
            var to = from + (rolls % 10);
            if (to > 10) to -= 10;
            return to;
        }
    }
}