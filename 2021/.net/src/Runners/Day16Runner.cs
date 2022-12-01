using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Advent.Runners
{
    public class Lib
    {
        public static string HexToBinaryString(string hex)
        {
            return string.Join("", hex.Select(c => Convert.ToString(Convert.ToInt32(c.ToString(), 16), 2).PadLeft(4, '0')));
        }
    }

    public class Node
    {
        public int Version { get; set; }
        public int Type { get; set; }
        public long Value { get; set; } = -1;
        public List<Node> Children { get; set; } = new List<Node>();
    }

    public class Day16Runner: IRunner
    {
        public void Go(string input)
        {
            var bits = Lib.HexToBinaryString(input);

            var node = GetPacket(ref bits);
            //Console.WriteLine(JsonConvert.SerializeObject(node, Formatting.Indented));

            Console.WriteLine($"version sum: {SumVersions(node)}");
            Console.WriteLine($"calculated: {Calculate(node)}");
        }

        private int SumVersions(Node node)
        {
            var sum = node.Version;
            foreach (var child in node.Children)
            {
                sum += SumVersions(child);
            }
            return sum;
        }

        private List<long> GetValues(Node node)
        {
            var values = new List<long>();
            foreach (var child in node.Children)
            {
                values.Add(Calculate(child));
            }
            return values;
        }

        private long Calculate(Node node)
        {
            switch (node.Type)
            {
                case 0: // sum
                    return GetValues(node).Sum();
                case 1: // product
                    return GetValues(node).Aggregate((total, next) => total * next);
                case 2: // min
                    return GetValues(node).Min();
                case 3: // max
                    return GetValues(node).Max();
                case 4: // value
                    return node.Value;
                case 5: // greater than
                    return Calculate(node.Children[0]) > Calculate(node.Children[1]) ? 1 : 0;
                case 6: // less than
                    return Calculate(node.Children[0]) < Calculate(node.Children[1]) ? 1 : 0;
                case 7: // equal to
                    return Calculate(node.Children[0]) == Calculate(node.Children[1]) ? 1 : 0;
                default:
                    Console.WriteLine("unrecogonized operation");
                    return -1;
            }
        }

        private string Slice(int size, ref string bits)
        {
            var slice = bits.Substring(0, size);
            bits = bits.Substring(size);
            return slice;
        }

        private int SliceToInt(int size, ref string bits)
        {
            return Convert.ToInt32(Slice(size, ref bits), 2);
        }

        private Node GetPacket(ref string bits)
        {
            var node = new Node()
            {
                Version = SliceToInt(3, ref bits),
                Type = SliceToInt(3, ref bits)
            };

            switch (node.Type) 
            {
                case 4: // literal
                    var buffer = "";
                    bool done;
                    do
                    {
                        done = SliceToInt(1, ref bits) == 0;
                        buffer += Slice(4, ref bits); // fix this
                    }
                    while (!done);
                    node.Value = Convert.ToInt64(buffer, 2);
                    break;
                default: // operation
                    // grab a number of packets
                    var grabPackets = SliceToInt(1, ref bits);
                    if (grabPackets == 1) 
                    {
                        var subPackets = SliceToInt(11, ref bits);
                        for (var i = 0; i < subPackets; i++)
                        {
                            node.Children.Add(GetPacket(ref bits));
                        }
                    } 
                    else
                    {
                        var subBits = SliceToInt(15, ref bits);
                        var slicedBits = Slice(subBits, ref bits);
                        while (slicedBits.Contains('1'))
                        {
                            node.Children.Add(GetPacket(ref slicedBits));
                        }
                    }
                    break;
            }
            return node;
        }
    }
}
