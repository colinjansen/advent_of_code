using System;

namespace Advent
{
    class DayRunnerFactory
    {
        public static IRunner GetRunner(int day)
        {
            string scenario1 = $"Advent.Runners.Day{day}Runner";
            Type theType = typeof(DayRunnerFactory).Assembly.GetType(scenario1);
            return (IRunner)Activator.CreateInstance(theType);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                Console.WriteLine($"please enter day to run");
                return;
            }

            var day = int.Parse(args[0]);
            Console.WriteLine($"executing day {day}!\n--------\n\n");

            var input = System.IO.File.ReadAllText(@$"Input/day{day}.txt");
            DayRunnerFactory.GetRunner(day).Go(input);
        }
    }
}
