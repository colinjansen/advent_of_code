using System;

namespace Advent.Runners
{
    class Day20Runner : IRunner
    {
        private string algo;

        public void Go(string input)
        {
            var split = input.Split("\n");
            algo = split[0];

            var rows = split.Length - 2;
            var cols = split[2].Trim().Length;
            var image = new char[rows, cols];

            for (var r = 0; r < rows; r++)
            {
                for (var c = 0; c < cols; c++)
                {
                    image[r, c] = split[r + 2][c];
                }
            }

            for (var i = 1; i <= 50; i++)
            {
                image = Enhance(image, i % 2 == 1 ? '.' : '#');

                if (i == 2)
                {
                    Console.WriteLine($"part 1: " + Count(image));
                }
            }
            Console.WriteLine($"part 2: " + Count(image));

            Console.WriteLine(Show(image));
        }

        private char[,] Enhance(char[,] input, char defaultCharater)
        {
            var rows = input.GetLength(0);
            var columns = input.GetLength(1);
            var output = new char[rows+2, columns+2];

            for (var r = -1; r < rows + 1; r++)
            {
                for (var c = -1; c < columns + 1; c++)
                {
                    var binary = "";
                    for (var i = -1; i <= 1; i++)
                    {
                        for (var j = -1; j <= 1; j++)
                        {
                            binary += GetCharacter(input, r + i, c + j, defaultCharater) == '#' ? "1" : "0";
                        }
                    }
                    output[r + 1, c + 1] = algo[Convert.ToInt32(binary, 2)];
                }
            }
            return output;
        }

        private char GetCharacter(char[,] input, int r, int c, char defaultCharacter)
        {
            return (r < 0 || c < 0 || r >= input.GetLength(0) || c >= input.GetLength(1))
                ? defaultCharacter
                : input[r,c];
        }

        private string Show(char[,] input)
        {
            string buffer = "";
            for (var r = 0; r < input.GetLength(0); r++)
            {
                for (var c = 0; c < input.GetLength(1); c++)
                {
                    buffer += input[r, c];
                }
                buffer += "\n";
            }
            return buffer;
        }

        private int Count(char[,] input)
        {
            var count = 0;
            for (var r = 0; r < input.GetLength(0); r++)
                for (var c = 0; c < input.GetLength(1); c++)
                    if (input[r, c] == '#') count++;
            return count;
        }
    }
}

