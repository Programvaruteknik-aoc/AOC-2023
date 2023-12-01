defmodule Aoc2023Test do
  import Aoc2023
  use ExUnit.Case
  doctest Aoc2023

  test "greets aoc2023" do
    assert hello() == :aoc2023
  end

  test "streams lines from file" do
    result = stream_lines("test/test_input/test_input.txt")
    |> Enum.to_list()
    assert result == ["abc123\n", "def2444"]
  end

  test "reads file" do
    assert read_file("test/test_input/test_input.txt") == {:ok, "abc123\ndef2444"}
  end
end
