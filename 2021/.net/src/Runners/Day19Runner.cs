using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;

namespace Advent.Runners
{
    internal class Day19Runner : IRunner
    {
        private Scanner Combine(Scanner destination, Scanner source)
        {
            foreach (Beacon beacon in source)
            {
                if (!destination.Contains(beacon))
                {
                    destination.Add(beacon);
                }
            }
            destination.RelativeScannerPositions.Add(new Coordinate { X = source.X, Y = source.Y, Z = source.Z });
            foreach (var position in source.RelativeScannerPositions)
            {
                destination.RelativeScannerPositions.Add(new Coordinate
                {
                    X = source.X + position.X,
                    Y = source.Y + position.Y,
                    Z = source.Z + position.Z
                });
            }
            return destination;
        }

        private Scanner FindMatchingTranslation(Scanner array, Scanner target, int threshold = 12)
        {
            Scanner beaconArray = null;
            int num = 0;
            foreach (Beacon beacon in array)
            {
                foreach (Beacon beacon1 in target)
                {
                    var clone = target.Clone();
                    clone = Translate(clone, beacon, beacon1);
                    int num1 = MatchingBeaconPositions(array, clone);
                    if (num1 >= threshold)
                    {
                        if (num1 > num)
                        {
                            num = num1;
                            beaconArray = clone;
                        }
                    }
                }
            }
            return beaconArray;
        }

        public void Go(string input)
        {
            var scanners = ParseIntput(input);
            bool flag = false;
            while (!flag)
            {
                flag = true;
                for (int i = 0; i < scanners.Count; i++)
                {
                    Console.Write("\n!");
                    for (int j = 0; j < scanners.Count; j++)
                    {
                        if (j != i)
                        {
                            if (TryToCombine(scanners[i], scanners[j]) == null)
                            {
                                Console.Write(".");
                            }
                            else
                            {
                                Console.Write("@");
                                flag = false;
                                scanners.RemoveAt(j);
                                if (i > j)
                                {
                                    i--;
                                }
                                j--;
                            }
                        }
                    }
                }
            }

            // 18656
            // 15118
            // 14605
            // 13398

            //var scanners_input = System.IO.File.ReadAllText("input\\day19.scanners.txt");
            //var scanner = JsonConvert.DeserializeObject<Scanner>(scanners_input);

            foreach (var scanner in scanners)
            {
                Console.WriteLine($"number of beacons: {scanner.Count}");
                Console.WriteLine(JsonConvert.SerializeObject(scanner.RelativeScannerPositions));

                var max = 0;
                scanner.RelativeScannerPositions.Add(new Coordinate { X = 0, Y = 0, Z = 0 });
                for (var i = 0; i < scanner.RelativeScannerPositions.Count; i++)
                {
                    for (var j = 0; j < scanner.RelativeScannerPositions.Count; j++)
                    {
                        int md = Math.Abs(scanner.RelativeScannerPositions[i].X - scanner.RelativeScannerPositions[j].X) +
                                 Math.Abs(scanner.RelativeScannerPositions[i].Y - scanner.RelativeScannerPositions[j].Y) +
                                 Math.Abs(scanner.RelativeScannerPositions[i].Z - scanner.RelativeScannerPositions[j].Z);
                        
                        if (md > max) max = md;
                    }
                }

                Console.WriteLine($"max manhattan distance: {max}");
            }
        }

        private int MatchingBeaconPositions(Scanner array, Scanner target)
        {
            int num = 0;
            foreach (Beacon beacon in target)
            {
                if (array.Any((Beacon t) => (t.X != beacon.X || t.Y != beacon.Y ? false : t.Z == beacon.Z)))
                {
                    num++;
                }
            }
            return num;
        }

        private List<Scanner> ParseIntput(string input)
        {
            List<Scanner> beaconArrays = new List<Scanner>();
            int num = -1;
            foreach (string str in
                from l in input.Split("\n", StringSplitOptions.None)
                select l.Trim())
            {
                if (str != "")
                {
                    if (!str.StartsWith("---"))
                    {
                        string[] strArrays = str.Split(',', StringSplitOptions.None);
                        Beacon beacon = new Beacon()
                        {
                            X = Convert.ToInt32(strArrays[0]),
                            Y = Convert.ToInt32(strArrays[1]),
                            Z = Convert.ToInt32(strArrays[2])
                        };
                        beaconArrays[num].Add(beacon);
                    }
                    else
                    {
                        num++;
                        beaconArrays.Add(new Scanner());
                    }
                }
            }
            return beaconArrays;
        }

        private Scanner RotateX(Scanner scanner, int angle = 90)
        {
            double num = angle * 0.0174532925199433;
            double cos = Math.Cos(num);
            double sin = Math.Sin(num);
            foreach (Beacon beacon in scanner)
            {
                double y = beacon.Y * cos - beacon.Z * sin;
                double y1 = beacon.Y * sin + beacon.Z * cos;
                beacon.Y = (int)Math.Round(y);
                beacon.Z = (int)Math.Round(y1);
            }
            foreach (var p in scanner.RelativeScannerPositions)
            {
                double y = p.X * cos - p.Z * sin;
                double y1 = p.X * sin + p.Z * cos;
                p.X = (int)Math.Round(y);
                p.Z = (int)Math.Round(y1);
            }
            return scanner;
        }

        private Scanner RotateY(Scanner scanner, int angle = 90)
        {
            double num = angle * 0.0174532925199433;
            double cos = Math.Cos(num);
            double sin = Math.Sin(num);
            foreach (Beacon beacon in scanner)
            {
                double x = beacon.X * cos - beacon.Z * sin;
                double x1 = beacon.X * sin + beacon.Z * cos;
                beacon.X = (int)Math.Round(x);
                beacon.Z = (int)Math.Round(x1);
            }
            foreach (var p in scanner.RelativeScannerPositions)
            {
                double x = p.X * cos - p.Z * sin;
                double x1 = p.X * sin + p.Z * cos;
                p.X = (int)Math.Round(x);
                p.Z = (int)Math.Round(x1);
            }
            return scanner;
        }

        private Scanner RotateZ(Scanner scanner, int angle = 90)
        {
            double num = angle * 0.0174532925199433;
            double cos = Math.Cos(num);
            double sin = Math.Sin(num);
            foreach (Beacon beacon in scanner)
            {
                double x = beacon.X * cos - beacon.Y * sin;
                double x1 = beacon.X * sin + beacon.Y * cos;
                beacon.X = (int)Math.Round(x);
                beacon.Y = (int)Math.Round(x1);
            }
            foreach (var p in scanner.RelativeScannerPositions)
            {
                double x = p.X * cos - p.Y * sin;
                double x1 = p.X * sin + p.Y * cos;
                p.X = (int)Math.Round(x);
                p.Y = (int)Math.Round(x1);
            }
            return scanner;
        }

        private Scanner Translate(Scanner scanner, Beacon reference, Beacon target)
        {
            int x = reference.X - target.X;
            int y = reference.Y - target.Y;
            int z = reference.Z - target.Z;
            scanner.X = x;
            scanner.Y = y;
            scanner.Z = z;
            foreach (Beacon beacon in scanner)
            {
                beacon.X += x;
                beacon.Y += y;
                beacon.Z += z;
            }
            return scanner;
        }

        private Scanner TryToCombine(Scanner array, Scanner target)
        {
            Scanner beaconArray;
            Scanner beaconArray1 = FindMatchingTranslation(array, target, 12);
            if (beaconArray1 == null)
            {
                RotateY(target, 90);
                beaconArray1 = FindMatchingTranslation(array, target, 12);
                if (beaconArray1 == null)
                {
                    RotateY(target, 90);
                    beaconArray1 = FindMatchingTranslation(array, target, 12);
                    if (beaconArray1 == null)
                    {
                        RotateY(target, 90);
                        beaconArray1 = FindMatchingTranslation(array, target, 12);
                        if (beaconArray1 == null)
                        {
                            RotateY(target, 90);
                            RotateX(target, 180);
                            beaconArray1 = FindMatchingTranslation(array, target, 12);
                            if (beaconArray1 == null)
                            {
                                RotateY(target, 90);
                                beaconArray1 = FindMatchingTranslation(array, target, 12);
                                if (beaconArray1 == null)
                                {
                                    RotateY(target, 90);
                                    beaconArray1 = FindMatchingTranslation(array, target, 12);
                                    if (beaconArray1 == null)
                                    {
                                        RotateY(target, 90);
                                        beaconArray1 = FindMatchingTranslation(array, target, 12);
                                        if (beaconArray1 == null)
                                        {
                                            RotateY(target, 90);
                                            RotateX(target, 180);
                                            RotateX(target, 90);
                                            beaconArray1 = FindMatchingTranslation(array, target, 12);
                                            if (beaconArray1 == null)
                                            {
                                                RotateZ(target, 90);
                                                beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                if (beaconArray1 == null)
                                                {
                                                    RotateZ(target, 90);
                                                    beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                    if (beaconArray1 == null)
                                                    {
                                                        RotateZ(target, 90);
                                                        beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                        if (beaconArray1 == null)
                                                        {
                                                            RotateZ(target, 90);
                                                            RotateX(target, 270);
                                                            RotateX(target, 180);
                                                            beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                            if (beaconArray1 == null)
                                                            {
                                                                RotateZ(target, 90);
                                                                beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                                if (beaconArray1 == null)
                                                                {
                                                                    RotateZ(target, 90);
                                                                    beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                                    if (beaconArray1 == null)
                                                                    {
                                                                        RotateZ(target, 90);
                                                                        beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                                        if (beaconArray1 == null)
                                                                        {
                                                                            RotateZ(target, 90);
                                                                            RotateX(target, 180);
                                                                            RotateZ(target, 90);
                                                                            beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                                            if (beaconArray1 == null)
                                                                            {
                                                                                RotateX(target, 90);
                                                                                beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                                                if (beaconArray1 == null)
                                                                                {
                                                                                    RotateX(target, 90);
                                                                                    beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                                                    if (beaconArray1 == null)
                                                                                    {
                                                                                        RotateX(target, 90);
                                                                                        beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                                                        if (beaconArray1 == null)
                                                                                        {
                                                                                            RotateX(target, 90);
                                                                                            RotateZ(target, 270);
                                                                                            RotateZ(target, 180);
                                                                                            beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                                                            if (beaconArray1 == null)
                                                                                            {
                                                                                                RotateX(target, 90);
                                                                                                beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                                                                if (beaconArray1 == null)
                                                                                                {
                                                                                                    RotateX(target, 90);
                                                                                                    beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                                                                    if (beaconArray1 == null)
                                                                                                    {
                                                                                                        RotateX(target, 90);
                                                                                                        beaconArray1 = FindMatchingTranslation(array, target, 12);
                                                                                                        if (beaconArray1 == null)
                                                                                                        {
                                                                                                            RotateX(target, 90);
                                                                                                            RotateZ(target, 180);
                                                                                                            beaconArray = null;
                                                                                                        }
                                                                                                        else
                                                                                                        {
                                                                                                            Combine(array, beaconArray1);
                                                                                                            beaconArray = beaconArray1;
                                                                                                        }
                                                                                                    }
                                                                                                    else
                                                                                                    {
                                                                                                        Combine(array, beaconArray1);
                                                                                                        beaconArray = beaconArray1;
                                                                                                    }
                                                                                                }
                                                                                                else
                                                                                                {
                                                                                                    Combine(array, beaconArray1);
                                                                                                    beaconArray = beaconArray1;
                                                                                                }
                                                                                            }
                                                                                            else
                                                                                            {
                                                                                                Combine(array, beaconArray1);
                                                                                                beaconArray = beaconArray1;
                                                                                            }
                                                                                        }
                                                                                        else
                                                                                        {
                                                                                            Combine(array, beaconArray1);
                                                                                            beaconArray = beaconArray1;
                                                                                        }
                                                                                    }
                                                                                    else
                                                                                    {
                                                                                        Combine(array, beaconArray1);
                                                                                        beaconArray = beaconArray1;
                                                                                    }
                                                                                }
                                                                                else
                                                                                {
                                                                                    Combine(array, beaconArray1);
                                                                                    beaconArray = beaconArray1;
                                                                                }
                                                                            }
                                                                            else
                                                                            {
                                                                                Combine(array, beaconArray1);
                                                                                beaconArray = beaconArray1;
                                                                            }
                                                                        }
                                                                        else
                                                                        {
                                                                            Combine(array, beaconArray1);
                                                                            beaconArray = beaconArray1;
                                                                        }
                                                                    }
                                                                    else
                                                                    {
                                                                        Combine(array, beaconArray1);
                                                                        beaconArray = beaconArray1;
                                                                    }
                                                                }
                                                                else
                                                                {
                                                                    Combine(array, beaconArray1);
                                                                    beaconArray = beaconArray1;
                                                                }
                                                            }
                                                            else
                                                            {
                                                                Combine(array, beaconArray1);
                                                                beaconArray = beaconArray1;
                                                            }
                                                        }
                                                        else
                                                        {
                                                            Combine(array, beaconArray1);
                                                            beaconArray = beaconArray1;
                                                        }
                                                    }
                                                    else
                                                    {
                                                        Combine(array, beaconArray1);
                                                        beaconArray = beaconArray1;
                                                    }
                                                }
                                                else
                                                {
                                                    Combine(array, beaconArray1);
                                                    beaconArray = beaconArray1;
                                                }
                                            }
                                            else
                                            {
                                                Combine(array, beaconArray1);
                                                beaconArray = beaconArray1;
                                            }
                                        }
                                        else
                                        {
                                            Combine(array, beaconArray1);
                                            beaconArray = beaconArray1;
                                        }
                                    }
                                    else
                                    {
                                        Combine(array, beaconArray1);
                                        beaconArray = beaconArray1;
                                    }
                                }
                                else
                                {
                                    Combine(array, beaconArray1);
                                    beaconArray = beaconArray1;
                                }
                            }
                            else
                            {
                                Combine(array, beaconArray1);
                                beaconArray = beaconArray1;
                            }
                        }
                        else
                        {
                            Combine(array, beaconArray1);
                            beaconArray = beaconArray1;
                        }
                    }
                    else
                    {
                        Combine(array, beaconArray1);
                        beaconArray = beaconArray1;
                    }
                }
                else
                {
                    Combine(array, beaconArray1);
                    beaconArray = beaconArray1;
                }
            }
            else
            {
                Combine(array, beaconArray1);
                beaconArray = beaconArray1;
            }
            return beaconArray;
        }

        private class Beacon : IEquatable<Beacon>
        {
            public int X { get; set; }
            public int Y { get; set; }
            public int Z { get; set; }

            public bool Equals(Beacon beacon)
            {
                return X == beacon.X && Y == beacon.Y && Z == beacon.Z;
            }

            public override string ToString()
            {
                string[] strArrays = new string[5];
                int x = X;
                strArrays[0] = x.ToString().PadLeft(5, ' ');
                strArrays[1] = ",";
                x = Y;
                strArrays[2] = x.ToString().PadLeft(5, ' ');
                strArrays[3] = ",";
                x = Z;
                strArrays[4] = x.ToString().PadLeft(5, ' ');
                return string.Concat(strArrays);
            }
        }

        private class Coordinate
        {
            public int X { get; set; }
            public int Y { get; set; }
            public int Z { get; set; }
        }

        private class Scanner : List<Beacon>
        {
            public int X { get; set; }
            public int Y { get; set; }
            public int Z { get; set; }

            public List<Coordinate> RelativeScannerPositions = new List<Coordinate>();

            public Scanner Clone()
            {
                Scanner clone = new Scanner();
                foreach (Beacon beacon in this)
                {
                    clone.Add(new Beacon()
                    {
                        X = beacon.X,
                        Y = beacon.Y,
                        Z = beacon.Z
                    });
                }
                foreach (var position in RelativeScannerPositions)
                {
                    clone.RelativeScannerPositions.Add(position);
                }
                return clone;
            }

            public override string ToString()
            {
                string str = "";
                foreach (Beacon beacon in this)
                {
                    str = string.Concat(str, string.Format(" [{0}]", beacon));
                }
                return string.Concat("Beacons: ", str);
            }
        }
    }
}