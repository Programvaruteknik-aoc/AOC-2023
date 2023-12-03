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
  Solves part2 by
  """
  def part2(input) do
    :not_implemented
  end

  def parse_game(line) do
    [game_info | moves_info] = String.split(line, ": ")
    id = game_info
          |> String.split(" ")
          |> Enum.at(1)
          |> Integer.parse()
          |> elem(0)
    moves = moves_info
            |> List.first()
            |> String.split("; ")
            |> Enum.map(&parse_move/1)
    %{id: id, moves: moves}
  end

  def parse_move(move) do
    move
    |> String.split(", ")
    |> Enum.map(&parse_cube/1)
  end

  def parse_cube(cube) do
    [count, color] = String.split(cube, " ")
    {String.to_atom(color), String.to_integer(count)}
  end

  def is_possible(%{id: _, moves: moves}) do
    Enum.all?(moves, fn move ->
      Enum.all?(move, fn {color, count} ->
        count <= Map.get(@inventory, color)
      end)
    end)
  end
end
