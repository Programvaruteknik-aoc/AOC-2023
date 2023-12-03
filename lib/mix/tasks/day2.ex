defmodule Mix.Tasks.Day2 do
  use Mix.Task

  @shortdoc "Run solution for Day 2"
  def run(args) do
    case args do
      ["1", file] ->
        result = Day2.part1(file)
        IO.puts("Part 1 result: #{result}")
      ["2", file] ->
        result = Day2.part2(file)
        IO.puts("Part 2 result: #{result}")
      _ ->
        IO.puts("Usage: mix day1 <part_number> <file>")
    end
  end

end
