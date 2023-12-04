defmodule Day2 do
  import Aoc2023

  @inventory %{red: 12, green: 13, blue: 14}

  @doc """
  Solves part1 by reading lines from an input file, parsing the game into a map, then filtering
  out games with impossible moves, and sums the id's of those remaining.
  concatenating them, and summing them.
  """
  def part1(input) do
    stream_lines(input)
    |> Enum.map(&String.trim/1)
    |> Enum.map(&parse_game/1)
    |> Enum.filter(&is_possible/1)
    |> Enum.map(fn game -> game.id end)
    |> Enum.sum()
  end

  @doc """
  Solves part2 by doing the same, but extracting the minimum required cubes for each game,
  multiplies them, and sums them.
  """
  def part2(input) do
    stream_lines(input)
    |> Enum.map(&String.trim/1)
    |> Enum.map(&parse_game/1)
    |> Enum.map(&minimum_cubes/1)
    |> Enum.map(&power_of_set/1)
    |> Enum.sum()
  end

  def parse_game(line) do
    [game_info | sets_info] = String.split(line, ": ")
    id = game_info
          |> String.split(" ")
          |> Enum.at(1)
          |> Integer.parse()
          |> elem(0)
    sets = sets_info
            |> List.first()
            |> String.split("; ")
            |> Enum.map(&parse_set/1)
    %{id: id, sets: sets}
  end

  def parse_set(set) do
    set
    |> String.split(", ")
    |> Enum.map(&parse_cubes/1)
  end

  def parse_cubes(cubes) do
    [count, color] = String.split(cubes, " ")
    {String.to_atom(color), String.to_integer(count)}
  end

  def is_possible(%{id: _, sets: sets}) do
    Enum.all?(sets, fn set ->
      Enum.all?(set, fn {color, count} ->
        count <= Map.get(@inventory, color)
      end)
    end)
  end

  def minimum_cubes(%{sets: sets}) do
    Enum.reduce(sets, %{red: 0, green: 0, blue: 0}, fn set, accumulator ->
      Enum.reduce(set, accumulator, fn {color, count}, accumulator ->
        Map.update(accumulator, color, count, &max(count, &1))
      end)
    end)
  end

  def power_of_set(%{red: r, green: g, blue: b}), do: r * g * b

end
