using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;

namespace Advent.Runners
{
    internal class Probe
    {
        public int X { get; set; } = 0;

        public int XVelocity { get; set; } = 0;

        public int Y { get; set; } = 0;

        public int YVelocity { get; set; } = 0;

        public Probe()
        {
        }

        public void Step()
        {
            int num;
            X += XVelocity;
            Y += YVelocity;
            int xVelocity = XVelocity;
            if (XVelocity == 0)
            {
                num = 0;
            }
            else
            {
                num = (XVelocity > 0 ? 1 : -1);
            }
            XVelocity = xVelocity - num;
            YVelocity--;
        }
    }

    internal class Target
    {
        public int MaxX
        {
            get;
            set;
        }

        public int MaxY
        {
            get;
            set;
        }

        public int MinX
        {
            get;
            set;
        }

        public int MinY
        {
            get;
            set;
        }

        public Target()
        {
        }

        public bool Contains(Probe probe)
        {
            return (probe.X < MinX || probe.X > MaxX || probe.Y < MinY ? false : probe.Y <= MaxY);
        }

        public (int x, int y) Diff(Probe probe)
        {
            ValueTuple<int, int> valueTuple;
            int x = 0;
            int y = 0;
            if (!Contains(probe))
            {
                if (probe.X < MinX)
                {
                    x = probe.X - MinX;
                }
                if (probe.X > MaxX)
                {
                    x = probe.X - MaxX;
                }
                if (probe.Y < MinY)
                {
                    y = probe.Y - MinY;
                }
                if (probe.Y > MaxY)
                {
                    y = probe.Y - MaxY;
                }
                valueTuple = new ValueTuple<int, int>(x, y);
            }
            else
            {
                valueTuple = new ValueTuple<int, int>(x, y);
            }
            return valueTuple;
        }
    }

    internal class Solution
    {
        public int MaxHeight
        {
            get;
            set;
        }

        public int X
        {
            get;
            set;
        }

        public int Y
        {
            get;
            set;
        }

        public Solution()
        {
        }
    }

    internal class Day17Runner : IRunner
    {
        public Day17Runner()
        {
        }

        private Target CreateTarget(string input)
        {
            int[][] array = (
                from x in input.Split(':', StringSplitOptions.None)[1].Split(',', StringSplitOptions.None)
                select x.Split('=', StringSplitOptions.None)[1] into x
                select (
                    from c in x.Split("..", StringSplitOptions.None)
                    select Convert.ToInt32(c)).ToArray<int>()).ToArray<int[]>();
            return new Target()
            {
                MaxX = array[0][1],
                MinX = array[0][0],
                MaxY = array[1][1],
                MinY = array[1][0]
            };
        }

        private List<Solution> GetSolutions(Target target)
        {
            List<Solution> solutions = new List<Solution>();
            for (int i = 0; i <= target.MaxX + 1; i++)
            {
                Console.Write(string.Format("\rgathering solutions... {0}%", Math.Round(100 * ((double)i / (double)target.MaxX))));
                for (int j = target.MinY; j <= 1000; j++)
                {
                    int y = 0;
                    Probe probe = new Probe()
                    {
                        XVelocity = i,
                        YVelocity = j
                    };
                    while (true)
                    {
                        probe.Step();
                        if (probe.Y > y)
                        {
                            y = probe.Y;
                        }
                        ValueTuple<int, int> valueTuple = target.Diff(probe);
                        if (valueTuple.Item2 < 0)
                        {
                            break;
                        }
                        else if ((valueTuple.Item1 != null ? false : valueTuple.Item2 == 0))
                        {
                            solutions.Add(new Solution()
                            {
                                X = i,
                                Y = i,
                                MaxHeight = y
                            });
                            break;
                        }
                    }
                }
            }
            Console.Write("\n");
            return solutions;
        }

        public void Go(string input)
        {
            Target target = CreateTarget(input);
            Console.WriteLine(string.Format("target X:\t{0}\t{1}", target.MaxX, target.MinX));
            Console.WriteLine(string.Format("target Y:\t{0}\t{1}\n", target.MaxY, target.MinY));
            List<Solution> solutions = GetSolutions(target);
            Console.WriteLine(string.Format("Max Height: {0}", (
                from s in solutions
                select s.MaxHeight).Max()));
            Console.WriteLine(string.Format("Possible Velocities: {0}", solutions.Count));
        }
    }
}