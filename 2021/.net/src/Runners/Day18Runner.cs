using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace Advent.Runners
{
    internal class Day18Runner : IRunner
    {
        private bool _split = false;
        private bool _explode = false;

        private class Node
        {
            public Node Parent { get; set; }
            public Node Left { get; set; }
            public Node Right { get; set; }
            public int? LeftValue { get; set; }
            public int? RightValue { get; set; }

            public Node() { }
            public Node(string value): this((JToken)JsonConvert.DeserializeObject<dynamic>(value))
            { }
            public Node(JToken value)
            {
                if (value.Type != JTokenType.Array)
                {
                    throw new Exception("booo!");
                }

                if (value[0].Type == JTokenType.Integer)
                {
                    LeftValue = (int)value[0];
                }

                if (value[0].Type == JTokenType.Array)
                {
                    Left = new Node(value[0]);
                    Left.Parent = this;
                }

                if (value[1].Type == JTokenType.Integer)
                {
                    RightValue = (int)value[1];
                }

                if (value[1].Type == JTokenType.Array)
                {
                    Right = new Node(value[1]);
                    Right.Parent = this;
                }
            }

            public string ToString()
            {
                string leftString = (LeftValue.HasValue)
                    ? LeftValue.Value.ToString()
                    : Left.ToString();
                string rightString = (RightValue.HasValue)
                    ? RightValue.Value.ToString()
                    : Right.ToString();
                return $"[{leftString},{rightString}]";
            }

            public bool IsLeaf
            {
                get 
                {
                    return LeftValue.HasValue && RightValue.HasValue;
                }
            }

            public Node GetNextLeft()
            {
                var node = this;
                while (node == node?.Parent?.Left)
                {
                    node = node.Parent;
                }
                return node.Parent;
            }

            public Node GetNextRight()
            {
                var node = this;
                while (node == node?.Parent?.Right)
                {
                    node = node.Parent;
                } 
                return node.Parent;
            }
        }

        private void Split(Node node)
        {
            if (node.Left != null)
            {
                Split(node.Left);
            }
            if (node.LeftValue.HasValue && node.LeftValue.Value >= 10 && !_split)
            {
                _split = true;
                node.Left = new Node()
                {
                    LeftValue = (int)Math.Floor((double)node.LeftValue.Value / 2),
                    RightValue = (int)Math.Ceiling((double)node.LeftValue.Value / 2),
                    Parent = node
                };
                node.LeftValue = null;
            }
            if (node.RightValue.HasValue && node.RightValue.Value >= 10 && !_split)
            {
                _split = true;
                node.Right = new Node()
                {
                    LeftValue = (int)Math.Floor((double)node.RightValue.Value / 2),
                    RightValue = (int)Math.Ceiling((double)node.RightValue.Value / 2),
                    Parent = node
                };
                node.RightValue = null;
            }
            if (node.Right != null)
            {
                Split(node.Right);
            }
        }

        private void Explode(Node node, int level = 1, int index = 0)
        {
            if (node.IsLeaf && level >= 5 && !_explode)
            {
                _explode = true;
                // grab the values and the parent
                var left = node.LeftValue.Value;
                var right = node.RightValue.Value;
                var nextLeft = node.GetNextLeft();
                var nextRight = node.GetNextRight();
                var parent = node.Parent;
                // set the parent's left or right node to '0' depending on the index value
                if (index == 0)
                {
                    parent.Left = null;
                    parent.LeftValue = 0;
                }
                if (index == 1)
                {
                    parent.Right = null;
                    parent.RightValue = 0;
                }
                // find the nearest 'left' value
                if (nextLeft != null)
                {
                    if (nextLeft.LeftValue.HasValue)
                    {
                        nextLeft.LeftValue += left;
                    }
                    else
                    {
                        nextLeft = nextLeft.Left;
                        while (!nextLeft.RightValue.HasValue)
                        {
                            nextLeft = nextLeft.Right;
                        }
                        nextLeft.RightValue += left;
                    }
                }
                // find the nearest 'right' value
                if (nextRight != null)
                {
                    if (nextRight.RightValue.HasValue)
                    {
                        nextRight.RightValue += right;
                    }
                    else
                    {
                        nextRight = nextRight.Right;
                        while (!nextRight.LeftValue.HasValue)
                        {
                            nextRight = nextRight.Left;
                        }
                        nextRight.LeftValue += right;
                    }
                }
            }            
            if (node.Left != null)
            {
                Explode(node.Left, level + 1, 0);
            }
            if (node.Right != null)
            {
                Explode(node.Right, level + 1, 1);
            }
        }

        private Node Add(Node a, Node b)
        {
            var node = new Node
            {
                Left = a,
                Right = b
            };
            node.Left.Parent = node;
            node.Right.Parent = node;
            return node;
        }

        private (int start, int end) ChangeIndexes(string a, string b)
        {
            int start = 0;
            int end = 0;
            while (start < a.Length && start < b.Length && a[start].Equals(b[start])) {
                start++;
            }
            while (end < a.Length && a[a.Length - 1 - end].Equals(b[b.Length - 1 - end]))
            {
                end++;
            }
            return (start, end);
        }

        private string StringExplode(string input)
        {
            int level = 0;
            for (int i = 0; i < input.Length; i++)
            {
                if (input[i] == '[')
                {
                    level++;
                    continue;
                }
                if (input[i] == ']')
                {
                    level--;
                    continue;
                }
                var match = Regex.Match(input.Substring(i), @"^(\d+),(\d+)");
                if (level > 4 && match.Success) 
                {
                    var capture = match.Groups[0];
                    var left = match.Groups[1];
                    var right = match.Groups[2];
                    input = input.Substring(0, i-1) + "0" + input.Substring(i + capture.Length + 1);

                    var lmatch = Regex.Match(input.Substring(0, i - 1), @"(\d+)", RegexOptions.RightToLeft);
                    if (lmatch.Success)
                    {
                        var lcap = lmatch.Captures[0];
                        var lvalue = Convert.ToInt32(left.Value) + Convert.ToInt32(lcap.Value);
                        input = input.Substring(0, lcap.Index) + (lvalue) + input.Substring(lcap.Index + lcap.Length);
                    }
                    i += 1;
                    var rmatch = Regex.Match(input.Substring(i), @"(\d+)");
                    if (rmatch.Success)
                    {
                        var rcap = rmatch.Captures[0];
                        var rvalue = Convert.ToInt32(right.Value) + Convert.ToInt32(rcap.Value);
                        input = input.Substring(0, i + rcap.Index) + (rvalue) + input.Substring(i + rcap.Index + rcap.Length);
                    }
                    break;
                }
            }
            return input;
        }

        private Node Reduce(Node node)
        {
            do
            {
                _explode = false;
                _split = false;
                Explode(node);
                if (_explode) continue;
                Split(node);
                if (_split) continue;
            } while (_explode || _split);

            return node;
        }

        private int Mag(Node node)
        {
            var left = (node.LeftValue.HasValue)
                ? node.LeftValue.Value
                : Mag(node.Left);
            var right = (node.RightValue.HasValue)
                ? node.RightValue.Value
                : Mag(node.Right);
            return left*3 + right*2;
        }

        public void Go(string input)
        {
            var numbers = input.Split("\n");
            var node = new Node(numbers[0]);
            for (var i = 1; i < numbers.Length; i++)
            {
                node = Add(node, new Node(numbers[i]));
                Reduce(node);
            }

            Console.WriteLine("part 1: " + Mag(node));

            int max = 0;
            for (var i = 0; i < numbers.Length; i++)
            {
                for (var j = i + 1; j < numbers.Length; j++)
                {
                    var nodeI = new Node(numbers[i]);
                    var nodeJ = new Node(numbers[j]);
                    var mag1 = Mag(Reduce(Add(nodeI, nodeJ)));
                    var mag2 = Mag(Reduce(Add(nodeJ, nodeI)));
                    if (mag1 > max) max = mag1;
                    if (mag2 > max) max = mag2;
                }
            }

            Console.WriteLine($"part 2: " + max);
        }
    }
}