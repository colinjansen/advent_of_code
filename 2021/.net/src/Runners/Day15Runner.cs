using System;
using System.Collections.Generic;
using System.Linq;

namespace Advent.Runners
{
    public class Day15Runner : IRunner
    {
        private int solve(int[][] array, int tiles = 1)
        {
            int rowCount = array.Length;
            int columnCount = array[0].Length;
            var queue = new Queue<(int, int, int)>();
            var dangers = new int[rowCount * tiles, columnCount * tiles];
            // fill the danger grid with -1s
            for (var r = 0; r < rowCount * tiles; r++)
            {
                for (var c = 0; c < columnCount * tiles; c++)
                {
                    dangers[r, c] = -1;
                }
            }
            var rowDirections = new[] { -1, 0, 1, 0 };
            var columnDirections = new[] { 0, -1, 0, 1 };

            queue.Enqueue((0, 0, 0));
            long itterations = 0;
            while (queue.Count > 0)
            {
                itterations++;
                var (distance, row, column) = queue.Dequeue();
                if (row < 0 || row >= tiles * rowCount || column < 0 || column >= tiles * columnCount)
                {
                    continue;
                }
                var val = array[row % rowCount][column % columnCount] + (row / rowCount) + (column / columnCount);
                while (val > 9)
                {
                    val -= 9;
                }
                var cost = distance + val;
                if (dangers[row, column] == -1 || cost < dangers[row, column])
                {
                    dangers[row, column] = cost;
                }
                else
                {
                    continue;
                }
                for (var i = 0; i < 4; i++)
                {
                    queue.Enqueue((dangers[row, column], row + rowDirections[i], column + columnDirections[i]));
                }
            }

            //string buffer = "";
            //for (var r = 0; r < rowCount; r++)
            //{
            //    for (var c = 0; c < columnCount; c++)
            //    {
            //        buffer += dangers[r, c].ToString().PadLeft(4);
            //    }
            //    buffer += "\n";
            //}
            //Console.WriteLine(buffer);
            //Console.WriteLine($"\rdone.              \n");

            return dangers[(tiles * rowCount) - 1, (tiles * columnCount) - 1] - array[0][0];
        }

        public void Go(string input)
        {
            int[][] array = (
                from row in input.Split("\n", StringSplitOptions.None)
                select (
                    from c in row.Trim()
                    select Convert.ToInt32(new string(c, 1))).ToArray<int>()).ToArray<int[]>();

            Console.WriteLine($"solve for 1 tile: {solve(array, 1)}");
            Console.WriteLine($"solve for 5 tiles: {solve(array, 5)}");
        }
    }
}