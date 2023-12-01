defmodule Day1 do
  import Aoc2023

  @doc """
  Solves part1 by reading lines from an input file, extracting first and last numbers,
  concatenating them, and summing them.
  """
  def part1(input) do
    stream_lines(input)
    |> Enum.map(&String.trim/1)
    |> Enum.map(&extract_numbers/1)
    |> Enum.map(&concatenate_numbers/1)
    |> Enum.sum()
  end

  def part2(input) do
    IO.puts("Not implemented #{input} ")
  end

  defp extract_numbers(line) do
    case Regex.scan(~r/\d/, line) do
      [first_num | _] = matches ->
        last_num = List.last(matches)
        {hd(first_num), hd(last_num)}
      _ -> {0, 0}
    end
  end

  defp concatenate_numbers({first, last}) do
    String.to_integer(first <> last)
  end

end
