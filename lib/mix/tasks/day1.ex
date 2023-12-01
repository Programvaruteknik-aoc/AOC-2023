defmodule Mix.Tasks.Day1 do
  use Mix.Task

  @shortdoc "Run solution for Day 1"
  def run(args) do
    case args do
      ["1", file] ->
        result = Day1.part1(file)
        IO.puts("Part 1 result: #{result}")
      ["2", file] ->
        result = Day1.part2(file)
        IO.puts("Part 2 result: #{result}")
      _ ->
        IO.puts("Usage: mix day1 <part_number> <file>")
    end
  end

end
