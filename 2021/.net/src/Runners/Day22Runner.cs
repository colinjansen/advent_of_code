using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace Advent.Runners
{
    class Cuboid
    {
        public long X1 { get; set; }
        public long Y1 { get; set; }
        public long Z1 { get; set; }
        public long X2 { get; set; }
        public long Y2 { get; set; }
        public long Z2 { get; set; }

        public List<Cuboid> OverLaps = new();

        public override string ToString()
        {
            return $"{X1} {Y1} {Z1} {X2} {Y2} {Z2}";
        }

        public long Volume
        {
            get
            {
                return (X2 - X1 + 1) * (Y2 - Y1 + 1) * (Z2 - Z1 + 1);
            }
        }
    }

    class Day22Runner : IRunner
    {
        Dictionary<Cuboid, int> cubes = new();

        public void Go(string input)
        {
            foreach (var line in input.Split("\n"))
            {
                var match = Regex.Match(line, @"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)");
                var cuboid = new Cuboid
                {
                    X1 = Convert.ToInt32(match.Groups[2].Value),
                    X2 = Convert.ToInt32(match.Groups[3].Value),
                    Y1 = Convert.ToInt32(match.Groups[4].Value),
                    Y2 = Convert.ToInt32(match.Groups[5].Value),
                    Z1 = Convert.ToInt32(match.Groups[6].Value),
                    Z2 = Convert.ToInt32(match.Groups[7].Value)
                };
                var on = match.Groups[1].Value == "on";
                Add(cuboid, on);
            }

            long total = 0;
            foreach (var c in cubes.Keys)
            {
                total += c.Volume * cubes[c];
            }
            Console.WriteLine($"total: {total}");
        }

        /// <summary>
        /// https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
        /// insane
        /// </summary>
        /// <param name="cuboid"></param>
        /// <param name="on"></param>
        private void Add(Cuboid cuboid, bool on)
        {
            var newCuboids = new Dictionary<Cuboid, int>();

            foreach (Cuboid c in cubes.Keys)
            {
                var overlap = Intersection(cuboid, c);
                if (overlap != null)
                {
                    if (!newCuboids.ContainsKey(overlap))
                    {
                        newCuboids[overlap] = 0;
                    }
                    newCuboids[overlap] -= cubes[c];
                }
            }

            if (on)
            {
                if (!newCuboids.ContainsKey(cuboid))
                {
                    newCuboids[cuboid] = 0;
                }
                newCuboids[cuboid] += 1;
            }

            foreach (Cuboid c in newCuboids.Keys)
            {
                if (!cubes.ContainsKey(c))
                {
                    cubes[c] = 0;
                }
                cubes[c] += newCuboids[c];
            }
        }

        private Cuboid Intersection(Cuboid a, Cuboid b)
        {
            if (a.X1 > b.X2 || a.X2 < b.X1 || a.Y1 > b.Y2 || a.Y2 < b.Y1 || a.Z1 > b.Z2 || a.Z2 < b.Z1)
            {
                return null;
            }

            return new Cuboid
            {
                X1 = Math.Max(a.X1, b.X1),
                X2 = Math.Min(a.X2, b.X2),
                Y1 = Math.Max(b.Y1, a.Y1),
                Y2 = Math.Min(b.Y2, a.Y2),
                Z1 = Math.Max(b.Z1, a.Z1),
                Z2 = Math.Min(b.Z2, a.Z2),
            };
        }
    }
}
