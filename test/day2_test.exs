defmodule Day2Test do
  import Day2
  use ExUnit.Case


  @simpledoc "Part 1"

  test "part 1 should return correctly" do
    assert part1("test/test_input/day2_part1.txt") == 8
  end

  test "should return parsed game" do
    assert parse_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") ==
      %{id: 1, moves: [
        [{:blue, 3}, {:red, 4}],
        [{:red, 1}, {:green, 2}, {:blue, 6}],
        [{:green, 2}]
      ]}
  end

  test "should return parsed move" do
    assert parse_move("3 blue, 4 red") == [{:blue, 3}, {:red, 4}]
  end

  test "should return parsed cube" do
    assert parse_cube("3 blue") == {:blue, 3}
  end


  @simpledoc "Part 2"

end
